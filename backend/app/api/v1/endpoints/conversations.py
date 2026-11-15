from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import Conversation, Message
from backend.app.schemas import (
    ConversationResponse, ConversationCreate, SendMessageRequest, ChatResponse, MessageResponse
)
from backend.app.api.v1.endpoints.auth import get_or_create_default_user
from backend.app.agent.orchestrator import HeeraMonAgent

router = APIRouter()

@router.get("", response_model=List[ConversationResponse])
def get_conversations(db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    return db.query(Conversation).filter(Conversation.user_id == user.id).all()

@router.post("", response_model=ConversationResponse)
def create_conversation(data: ConversationCreate, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    conv = Conversation(user_id=user.id, title=data.title or "New Conversation")
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conv

@router.get("/{conversation_id}", response_model=ConversationResponse)
def get_conversation_by_id(conversation_id: str, db: Session = Depends(get_db)):
    user = get_or_create_default_user(db)
    conv = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == user.id
    ).first()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conv

@router.post("/{conversation_id}/messages", response_model=ChatResponse)
async def send_message_to_conversation(
    conversation_id: str,
    payload: SendMessageRequest,
    db: Session = Depends(get_db)
):
    user = get_or_create_default_user(db)
    agent = HeeraMonAgent(db)
    turn_result = await agent.process_user_turn(
        conversation_id=conversation_id,
        user_message=payload.content,
        user_id=user.id
    )
    return turn_result
