from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import Application, Job, User, Preference
from backend.app.schemas import (
    ApplicationResponse, ApplicationCreate, ApplicationApproveRequest
)
from backend.app.api.v1.endpoints.auth import get_or_create_default_user
from backend.app.llm.factory import get_llm_provider

router = APIRouter()

@router.get("", response_model=List[ApplicationResponse])
def get_user_applications(db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    return db.query(Application).filter(Application.user_id == user.id).order_by(Application.created_at.desc()).all()

@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application_by_id(application_id: str, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    app_record = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == user.id
    ).first()
    if not app_record:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_record

@router.post("/prepare", response_model=ApplicationResponse)
async def prepare_application(
    payload: ApplicationCreate,
    db: Session = Depends(get_db)
):
    user = get_or_create_default_user(db)
    job = db.query(Job).filter(Job.id == payload.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Fetch active preferences
    prefs = db.query(Preference).filter(
        Preference.user_id == user.id,
        Preference.status == "active"
    ).all()
    pref_dicts = [{"category": p.category, "value": p.value} for p in prefs]

    # Use LLM provider to craft grounded tailored package
    llm = get_llm_provider()
    draft = await llm.draft_application_package(
        job={
            "title": job.title,
            "company": job.company,
            "work_arrangement": job.work_arrangement
        },
        user_profile=user.profile_data or {"name": user.name, "email": user.email},
        preferences=pref_dicts
    )

    now = datetime.now(timezone.utc)
    # Check if application already exists
    app_record = db.query(Application).filter(
        Application.user_id == user.id,
        Application.job_id == job.id
    ).first()

    if not app_record:
        app_record = Application(
            user_id=user.id,
            job_id=job.id,
            status="review", # Waiting for explicit human review
            tailored_notes=draft["tailored_notes"],
            cover_letter=draft["cover_letter"],
            submission_data={"ready_for_review": True},
            created_at=now,
            updated_at=now
        )
        db.add(app_record)
    else:
        app_record.status = "review"
        app_record.tailored_notes = draft["tailored_notes"]
        app_record.cover_letter = draft["cover_letter"]
        app_record.updated_at = now

    db.commit()
    db.refresh(app_record)
    return app_record

@router.post("/{application_id}/approve", response_model=ApplicationResponse)
def approve_and_submit_application(
    application_id: str,
    payload: ApplicationApproveRequest,
    db: Session = Depends(get_db)
):
    user = get_or_create_default_user(db)
    app_record = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == user.id
    ).first()
    if not app_record:
        raise HTTPException(status_code=404, detail="Application not found")

    if not payload.confirm_submission:
        raise HTTPException(status_code=400, detail="Submission confirmation required")

    now = datetime.now(timezone.utc)
    app_record.status = "submitted" # Approved by human and dispatched
    app_record.submitted_at = now
    app_record.updated_at = now
    db.commit()
    db.refresh(app_record)
    return app_record
