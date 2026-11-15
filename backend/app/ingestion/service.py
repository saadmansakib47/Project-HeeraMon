import hashlib
from datetime import datetime, timezone
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from backend.app.models import Job, JobSource, JobSourceRecord
from backend.app.ingestion.adapters.curated_tech import CuratedTechAdapter
from backend.app.ingestion.adapters.arbeitnow import ArbeitnowAdapter

def generate_dedup_hash(title: str, company: str, location: str) -> str:
    key = f"{title.lower().strip()}_{company.lower().strip()}_{location.lower().strip()}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()

class IngestionService:
    def __init__(self, db: Session):
        self.db = db
        self.adapters = [
            CuratedTechAdapter(),
            ArbeitnowAdapter()
        ]

    async def run_ingestion(self) -> Dict[str, Any]:
        stats = {
            "sources_processed": 0,
            "jobs_fetched": 0,
            "jobs_created": 0,
            "jobs_updated": 0,
            "errors": []
        }

        now = datetime.now(timezone.utc)

        for adapter in self.adapters:
            # 1. Find or create JobSource in DB
            source = self.db.query(JobSource).filter(JobSource.name == adapter.source_name).first()
            if not source:
                source = JobSource(
                    name=adapter.source_name,
                    source_type=adapter.source_type,
                    status="active"
                )
                self.db.add(source)
                self.db.commit()
                self.db.refresh(source)

            # 2. Fetch raw jobs
            try:
                raw_jobs = await adapter.fetch_jobs()
                stats["sources_processed"] += 1
                stats["jobs_fetched"] += len(raw_jobs)
                source.last_sync_at = now
                source.error_info = None
            except Exception as e:
                source.error_info = str(e)
                stats["errors"].append(f"{adapter.source_name}: {str(e)}")
                self.db.commit()
                continue

            # 3. Normalize & Deduplicate
            for raw in raw_jobs:
                try:
                    norm = adapter.normalize_job(raw)
                    dedup_hash = generate_dedup_hash(
                        norm["title"], norm["company"], norm["location"]
                    )

                    existing_job = self.db.query(Job).filter(Job.dedup_hash == dedup_hash).first()

                    if existing_job:
                        # Update freshness
                        existing_job.last_seen_at = now
                        stats["jobs_updated"] += 1
                        job_id = existing_job.id
                    else:
                        new_job = Job(
                            title=norm["title"],
                            company=norm["company"],
                            description=norm["description"],
                            location=norm["location"],
                            work_arrangement=norm["work_arrangement"],
                            employment_type=norm["employment_type"],
                            salary_min=norm.get("salary_min"),
                            salary_max=norm.get("salary_max"),
                            salary_currency=norm.get("salary_currency", "BDT"),
                            commute_time_minutes=norm.get("commute_time_minutes"),
                            workday_hours=norm.get("workday_hours"),
                            required_skills=norm.get("required_skills", []),
                            benefits=norm.get("benefits", []),
                            culture_notes=norm.get("culture_notes"),
                            application_url=norm.get("application_url"),
                            status="active",
                            dedup_hash=dedup_hash,
                            first_seen_at=now,
                            last_seen_at=now
                        )
                        self.db.add(new_job)
                        self.db.flush()
                        stats["jobs_created"] += 1
                        job_id = new_job.id

                    # Record source link
                    src_rec = self.db.query(JobSourceRecord).filter(
                        JobSourceRecord.job_id == job_id,
                        JobSourceRecord.source_id == source.id
                    ).first()

                    if not src_rec:
                        src_rec = JobSourceRecord(
                            job_id=job_id,
                            source_id=source.id,
                            external_job_id=norm.get("external_id"),
                            source_url=norm.get("application_url"),
                            raw_data=raw,
                            first_seen_at=now,
                            last_seen_at=now
                        )
                        self.db.add(src_rec)
                    else:
                        src_rec.last_seen_at = now

                except Exception as ex:
                    stats["errors"].append(f"Error processing job: {str(ex)}")

            self.db.commit()

        return stats
