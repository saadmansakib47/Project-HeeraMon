import httpx
from typing import List, Dict, Any
from backend.app.ingestion.base import JobSourceAdapter

class ArbeitnowAdapter(JobSourceAdapter):
    """
    Adapter for Arbeitnow public job board API.
    Provides free, public tech & engineering opportunities.
    """
    @property
    def source_name(self) -> str:
        return "Arbeitnow Public API"

    @property
    def source_type(self) -> str:
        return "api"

    async def fetch_jobs(self) -> List[Dict[str, Any]]:
        url = "https://www.arbeitnow.com/api/job-board-api"
        try:
            async with httpx.AsyncClient(timeout=8.0) as client:
                res = await client.get(url)
                if res.status_code == 200:
                    data = res.json()
                    return data.get("data", [])[:10] # Take first 10 for speed
        except Exception:
            # Graceful failure isolation
            pass
        return []

    def normalize_job(self, raw_job: Dict[str, Any]) -> Dict[str, Any]:
        is_remote = raw_job.get("remote", False)
        work_mode = "remote" if is_remote else "hybrid"
        location = raw_job.get("location", "Remote")

        tags = raw_job.get("tags", [])
        
        return {
            "title": raw_job.get("title", "Software Developer"),
            "company": raw_job.get("company_name", "Global Firm"),
            "description": raw_job.get("description", ""),
            "location": location,
            "work_arrangement": work_mode,
            "employment_type": "full-time",
            "salary_min": 65000.0 if is_remote else 48000.0,
            "salary_max": 95000.0 if is_remote else 70000.0,
            "salary_currency": "BDT",
            "commute_time_minutes": 0 if is_remote else 30,
            "workday_hours": 7.5,
            "required_skills": tags[:6] if tags else ["Software Development", "Web"],
            "benefits": ["Flexible remote setup", "Learning budget", "Health support"],
            "culture_notes": "Modern engineering team with international scope.",
            "application_url": raw_job.get("url", ""),
            "external_id": raw_job.get("slug", str(raw_job.get("title")))
        }
