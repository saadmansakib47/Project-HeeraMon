from abc import ABC, abstractmethod
from typing import List, Dict, Any

class JobSourceAdapter(ABC):
    @property
    @abstractmethod
    def source_name(self) -> str:
        """Name of the job source."""
        pass

    @property
    @abstractmethod
    def source_type(self) -> str:
        """Type of source: api, rss, or curated."""
        pass

    @abstractmethod
    async def fetch_jobs(self) -> List[Dict[str, Any]]:
        """
        Fetch raw job items from the source.
        Returns a list of raw dictionaries.
        """
        pass

    @abstractmethod
    def normalize_job(self, raw_job: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize a raw job record into HeeraMon's standardized job schema:
        title, company, description, location, work_arrangement,
        employment_type, salary_min, salary_max, salary_currency,
        commute_time_minutes, workday_hours, required_skills, benefits,
        culture_notes, application_url, external_id.
        """
        pass
