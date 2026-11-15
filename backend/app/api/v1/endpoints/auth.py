from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import User, Conversation
from backend.app.schemas import UserResponse
from backend.app.config import settings

router = APIRouter()

def get_or_create_default_user(db: Session) -> User:
    user = db.query(User).filter(User.email == settings.DEFAULT_USER_EMAIL).first()
    if not user:
        user = User(
            email=settings.DEFAULT_USER_EMAIL,
            name=settings.DEFAULT_USER_NAME,
            profile_data={
                "skills": ["Python", "Machine Learning", "FastAPI", "PyTorch", "System Design"],
                "experience_years": 2,
                "current_location": "Dhaka, Bangladesh",
                "target_role": "AI/ML Engineer"
            }
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # Ensure at least one default conversation exists
    conv = db.query(Conversation).filter(Conversation.user_id == user.id).first()
    if not conv:
        conv = Conversation(
            user_id=user.id,
            title="Finding Meaningful Work"
        )
        db.add(conv)
        db.commit()

    return user

@router.get("/me", response_model=UserResponse)
def get_current_user(db: Session = Depends(get_db)):
    return get_or_create_default_user(db)
