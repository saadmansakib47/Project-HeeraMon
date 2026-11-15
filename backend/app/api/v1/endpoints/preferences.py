from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import Preference
from backend.app.schemas import PreferenceResponse, PreferenceCreate, PreferenceUpdate
from backend.app.api.v1.endpoints.auth import get_or_create_default_user

router = APIRouter()

@router.get("", response_model=List[PreferenceResponse])
def get_preferences(db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    return db.query(Preference).filter(
        Preference.user_id == user.id,
        Preference.status == "active"
    ).all()

@router.post("", response_model=PreferenceResponse)
def create_preference(data: PreferenceCreate, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    now = datetime.now(timezone.utc)
    pref = Preference(
        user_id=user.id,
        category=data.category,
        value=data.value,
        preference_type=data.preference_type,
        source=data.source,
        confidence=data.confidence,
        status="active",
        raw_query=data.raw_query,
        created_at=now,
        updated_at=now
    )
    db.add(pref)
    db.commit()
    db.refresh(pref)
    return pref

@router.patch("/{preference_id}", response_model=PreferenceResponse)
def update_preference(preference_id: str, data: PreferenceUpdate, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    pref = db.query(Preference).filter(
        Preference.id == preference_id,
        Preference.user_id == user.id
    ).first()
    if not pref:
        raise HTTPException(status_code=404, detail="Preference not found")

    if data.value is not None:
        pref.value = data.value
    if data.preference_type is not None:
        pref.preference_type = data.preference_type
    if data.source is not None:
        pref.source = data.source
    if data.confidence is not None:
        pref.confidence = data.confidence
    if data.status is not None:
        pref.status = data.status

    pref.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(pref)
    return pref

@router.delete("/{preference_id}")
def delete_preference(preference_id: str, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    pref = db.query(Preference).filter(
        Preference.id == preference_id,
        Preference.user_id == user.id
    ).first()
    if not pref:
        raise HTTPException(status_code=404, detail="Preference not found")

    pref.status = "archived" # Soft delete
    db.commit()
    return {"message": "Preference archived successfully"}
