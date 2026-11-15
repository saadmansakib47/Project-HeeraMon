from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import Match, UserDecision, Preference, Notification, Job
from backend.app.schemas import MatchResponse, MatchDecisionRequest
from backend.app.api.v1.endpoints.auth import get_or_create_default_user

router = APIRouter()

@router.get("", response_model=List[MatchResponse])
def get_user_matches(db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    matches = db.query(Match).filter(
        Match.user_id == user.id
    ).order_by(Match.score.desc()).all()
    return matches

@router.get("/{match_id}", response_model=MatchResponse)
def get_match_by_id(match_id: str, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    match = db.query(Match).filter(
        Match.id == match_id,
        Match.user_id == user.id
    ).first()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match

@router.post("/{match_id}/decision")
def record_match_decision(
    match_id: str,
    payload: MatchDecisionRequest,
    db: Session = Depends(get_db)
):
    user = get_or_create_default_user(db)
    match = db.query(Match).filter(
        Match.id == match_id,
        Match.user_id == user.id
    ).first()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    now = datetime.now(timezone.utc)
    decision = UserDecision(
        user_id=user.id,
        job_id=match.job_id,
        decision=payload.decision,
        reason=payload.reason,
        timestamp=now
    )
    db.add(decision)
    db.commit()

    # Preference Learning Engine (Milestone 5)
    # Detect repeated patterns from user decisions
    if payload.decision == "rejected":
        recent_rejections = db.query(UserDecision).filter(
            UserDecision.user_id == user.id,
            UserDecision.decision == "rejected"
        ).order_by(UserDecision.timestamp.desc()).limit(3).all()

        if len(recent_rejections) >= 3:
            # Check if all rejected jobs share common attributes (e.g. onsite or lower salary)
            rejected_jobs = [db.query(Job).filter(Job.id == d.job_id).first() for d in recent_rejections]
            rejected_jobs = [j for j in rejected_jobs if j is not None]

            # Pattern: onsite rejections
            if all(j.work_arrangement == "onsite" for j in rejected_jobs):
                # Suggest Remote-Only learned preference
                existing_pref = db.query(Preference).filter(
                    Preference.user_id == user.id,
                    Preference.category == "work_arrangement",
                    Preference.status == "active"
                ).first()

                if not existing_pref or existing_pref.value != "Remote":
                    notif = Notification(
                        user_id=user.id,
                        notification_type="preference_suggestion",
                        title="Learned Preference Suggestion",
                        content="You have declined several on-site roles recently. Would you like HeeraMon to prioritize strictly Remote positions?",
                        related_job_id=match.job_id,
                        is_read=False,
                        created_at=now
                    )
                    db.add(notif)
                    db.commit()

    return {"status": "success", "decision": payload.decision, "recorded_at": now.isoformat()}
