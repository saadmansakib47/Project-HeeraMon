import asyncio
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from backend.app.models import User, Match, Notification, AgentRun, Job
from backend.app.ingestion.service import IngestionService
from backend.app.matching.engine import MatchingEngine

class BackgroundSearchRunner:
    """
    Background Continuous Job-Seeking Agent.
    Runs independently of browser sessions to ingest new jobs,
    evaluate matches, and generate notifications.
    """
    def __init__(self):
        self.is_running = False

    async def execute_cycle(self) -> dict:
        db: Session = SessionLocal()
        start_time = datetime.now(timezone.utc)
        run_record = AgentRun(
            task_type="continuous_background_search",
            status="running",
            input_context={"trigger": "scheduled_runner"},
            started_at=start_time
        )
        db.add(run_record)
        db.commit()

        summary = {"ingestion": {}, "new_matches": 0, "notifications_sent": 0}

        try:
            # 1. Run Ingestion
            ingestion_service = IngestionService(db)
            ingest_stats = await ingestion_service.run_ingestion()
            summary["ingestion"] = ingest_stats

            # 2. Evaluate for each active user
            users = db.query(User).all()
            matching_engine = MatchingEngine(db)

            for user in users:
                matches = await matching_engine.match_all_jobs_for_user(user.id)
                high_matches = [m for m in matches if m.score >= 70.0 and m.eligibility_status == "eligible"]
                summary["new_matches"] += len(high_matches)

                # 3. Create notifications for top matches if not already notified
                for m in high_matches[:2]:
                    existing_notif = db.query(Notification).filter(
                        Notification.user_id == user.id,
                        Notification.related_job_id == m.job_id
                    ).first()

                    if not existing_notif:
                        job_title = m.job.title if m.job else "New Position"
                        company = m.job.company if m.job else "Partner Firm"
                        
                        notif = Notification(
                            user_id=user.id,
                            notification_type="new_match",
                            title=f"New Opportunity: {job_title}",
                            content=f"HeeraMon found a promising match at {company} (Fit: {m.score:.0f}%). {m.explanation}",
                            related_job_id=m.job_id,
                            is_read=False,
                            created_at=datetime.now(timezone.utc)
                        )
                        db.add(notif)
                        summary["notifications_sent"] += 1

            run_record.status = "completed"
            run_record.result_summary = str(summary)
            run_record.completed_at = datetime.now(timezone.utc)
            db.commit()

        except Exception as e:
            db.rollback()
            run_record.status = "failed"
            run_record.error_message = str(e)
            run_record.completed_at = datetime.now(timezone.utc)
            db.commit()
            summary["error"] = str(e)
        finally:
            db.close()

        return summary

background_runner = BackgroundSearchRunner()
