from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from backend.app.models import User, Preference, Job, Match
from backend.app.llm.base import BaseLLMProvider
from backend.app.llm.factory import get_llm_provider

class MatchingEngine:
    def __init__(self, db: Session, llm_provider: Optional[BaseLLMProvider] = None):
        self.db = db
        self.llm = llm_provider or get_llm_provider()

    async def evaluate_user_job_match(
        self, 
        user_id: str, 
        job: Job, 
        active_preferences: Optional[List[Preference]] = None
    ) -> Match:
        """
        Evaluate a single job against user's preferences and store/update the Match record.
        """
        if active_preferences is None:
            active_preferences = self.db.query(Preference).filter(
                Preference.user_id == user_id,
                Preference.status == "active"
            ).all()

        pref_dicts = [
            {
                "category": p.category,
                "value": p.value,
                "preference_type": p.preference_type,
                "confidence": p.confidence
            }
            for p in active_preferences
        ]

        job_dict = {
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "description": job.description,
            "location": job.location,
            "work_arrangement": job.work_arrangement,
            "salary_min": job.salary_min,
            "salary_max": job.salary_max,
            "salary_currency": job.salary_currency,
            "commute_time_minutes": job.commute_time_minutes,
            "workday_hours": job.workday_hours,
            "required_skills": job.required_skills,
            "benefits": job.benefits,
            "culture_notes": job.culture_notes
        }

        eval_result = await self.llm.evaluate_tradeoffs(job_dict, pref_dicts)

        # Check existing match
        match = self.db.query(Match).filter(
            Match.user_id == user_id,
            Match.job_id == job.id
        ).first()

        now = datetime.now(timezone.utc)
        if not match:
            match = Match(
                user_id=user_id,
                job_id=job.id,
                score=eval_result["score"],
                eligibility_status=eval_result["eligibility_status"],
                satisfied_preferences=eval_result["satisfied"],
                violated_preferences=eval_result["violated"],
                unknown_information=eval_result["unknown"],
                trade_offs=eval_result["trade_offs"],
                explanation=eval_result["explanation"],
                created_at=now,
                updated_at=now
            )
            self.db.add(match)
        else:
            match.score = eval_result["score"]
            match.eligibility_status = eval_result["eligibility_status"]
            match.satisfied_preferences = eval_result["satisfied"]
            match.violated_preferences = eval_result["violated"]
            match.unknown_information = eval_result["unknown"]
            match.trade_offs = eval_result["trade_offs"]
            match.explanation = eval_result["explanation"]
            match.updated_at = now

        self.db.commit()
        self.db.refresh(match)
        return match

    async def match_all_jobs_for_user(self, user_id: str) -> List[Match]:
        """
        Evaluate all active jobs for a user and return the ranked matches.
        """
        active_prefs = self.db.query(Preference).filter(
            Preference.user_id == user_id,
            Preference.status == "active"
        ).all()

        jobs = self.db.query(Job).filter(Job.status == "active").all()
        matches = []

        for job in jobs:
            match = await self.evaluate_user_job_match(user_id, job, active_prefs)
            matches.append(match)

        # Sort by score descending
        matches.sort(key=lambda m: m.score, reverse=True)
        return matches
