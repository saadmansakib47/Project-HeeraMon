from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import Notification
from backend.app.schemas import NotificationResponse
from backend.app.api.v1.endpoints.auth import get_or_create_default_user
from backend.app.scheduler.runner import background_runner

router = APIRouter()

@router.get("", response_model=List[NotificationResponse])
def get_notifications(db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    return db.query(Notification).filter(
        Notification.user_id == user.id
    ).order_by(Notification.created_at.desc()).all()

@router.patch("/{notification_id}/read")
def mark_notification_read(notification_id: str, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    notif = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == user.id
    ).first()
    if not notif:
        raise HTTPException(status_code=404, detail="Notification not found")
    notif.is_read = True
    db.commit()
    return {"status": "success", "id": notification_id, "is_read": True}

@router.post("/trigger-background-search")
async def trigger_background_search():
    summary = await background_runner.execute_cycle()
    return {"status": "completed", "summary": summary}
