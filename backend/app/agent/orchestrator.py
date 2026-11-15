from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from backend.app.models import User, Conversation, Message, Preference, Match
from backend.app.llm.base import BaseLLMProvider
from backend.app.llm.factory import get_llm_provider
from backend.app.matching.engine import MatchingEngine

class HeeraMonAgent:
    def __init__(self, db: Session, llm_provider: Optional[BaseLLMProvider] = None):
        self.db = db
        self.llm = llm_provider or get_llm_provider()
        self.matching_engine = MatchingEngine(db, self.llm)

    async def process_user_turn(
        self,
        conversation_id: str,
        user_message: str,
        user_id: str
    ) -> Dict[str, Any]:
        """
        Core conversational reasoning turn:
        1. Record incoming user message.
        2. Extract candidate preferences from message.
        3. Persist confirmed / new preferences.
        4. Trigger matching engine if preferences exist.
        5. Formulate HeeraMon wisdom-bird conversational reply with trade-offs & suggestion chips.
        6. Persist assistant response message.
        """
        now = datetime.now(timezone.utc)

        # 1. Fetch user & conversation
        user = self.db.query(User).filter(User.id == user_id).first()
        conversation = self.db.query(Conversation).filter(Conversation.id == conversation_id).first()
        if not conversation:
            conversation = Conversation(id=conversation_id, user_id=user_id, title="Career Exploration")
            self.db.add(conversation)
            self.db.commit()

        # Save user message
        user_msg = Message(
            conversation_id=conversation.id,
            role="user",
            content=user_message,
            timestamp=now
        )
        self.db.add(user_msg)
        self.db.commit()

        # 2. Extract preferences
        existing_prefs = self.db.query(Preference).filter(
            Preference.user_id == user_id,
            Preference.status == "active"
        ).all()

        existing_pref_dicts = [
            {"category": p.category, "value": p.value, "preference_type": p.preference_type}
            for p in existing_prefs
        ]

        extracted = await self.llm.extract_preferences(user_message, existing_pref_dicts)
        saved_prefs = []

        # 3. Upsert newly extracted preferences
        for item in extracted:
            # Check if category already exists
            existing = self.db.query(Preference).filter(
                Preference.user_id == user_id,
                Preference.category == item["category"],
                Preference.status == "active"
            ).first()

            if existing:
                existing.value = item["value"]
                existing.preference_type = item["preference_type"]
                existing.confidence = item.get("confidence", 1.0)
                existing.raw_query = item.get("raw_query")
                existing.updated_at = now
                saved_prefs.append(existing)
            else:
                new_pref = Preference(
                    user_id=user_id,
                    category=item["category"],
                    value=item["value"],
                    preference_type=item["preference_type"],
                    source="explicit",
                    confidence=item.get("confidence", 1.0),
                    status="active",
                    raw_query=item.get("raw_query"),
                    created_at=now,
                    updated_at=now
                )
                self.db.add(new_pref)
                saved_prefs.append(new_pref)

        self.db.commit()

        # Refresh all active preferences
        all_active_prefs = self.db.query(Preference).filter(
            Preference.user_id == user_id,
            Preference.status == "active"
        ).all()

        # 4. If we have preferences, evaluate matches
        recent_matches = []
        if all_active_prefs:
            matches = await self.matching_engine.match_all_jobs_for_user(user_id)
            recent_matches = [
                {
                    "id": m.id,
                    "score": m.score,
                    "eligibility_status": m.eligibility_status,
                    "satisfied": m.satisfied_preferences,
                    "violated": m.violated_preferences,
                    "unknown": m.unknown_information,
                    "trade_offs": m.trade_offs,
                    "explanation": m.explanation,
                    "job": {
                        "id": m.job.id,
                        "title": m.job.title,
                        "company": m.job.company,
                        "location": m.job.location,
                        "salary_min": m.job.salary_min,
                        "salary_max": m.job.salary_max,
                        "salary_currency": m.job.salary_currency,
                        "work_arrangement": m.job.work_arrangement,
                        "workday_hours": m.job.workday_hours,
                        "commute_time_minutes": m.job.commute_time_minutes,
                        "benefits": m.job.benefits,
                        "culture_notes": m.job.culture_notes,
                        "description": m.job.description
                    } if m.job else {}
                }
                for m in matches[:3]
            ]

        # 5. Fetch recent conversation history
        history_msgs = self.db.query(Message).filter(
            Message.conversation_id == conversation.id
        ).order_by(Message.timestamp.desc()).limit(6).all()
        history = [{"role": m.role, "content": m.content} for m in reversed(history_msgs)]

        user_name = user.name if user else "Comrade"
        active_pref_dicts = [
            {"category": p.category, "value": p.value, "preference_type": p.preference_type}
            for p in all_active_prefs
        ]

        llm_reply = await self.llm.generate_response(
            user_message=user_message,
            conversation_history=history,
            preferences=active_pref_dicts,
            recent_matches=recent_matches,
            user_name=user_name
        )

        # 6. Save assistant message
        asst_msg = Message(
            conversation_id=conversation.id,
            role="assistant",
            content=llm_reply["content"],
            metadata_info={
                "extracted_count": len(extracted),
                "suggested_chips": llm_reply.get("suggested_chips", []),
                "matches_count": len(recent_matches)
            },
            timestamp=datetime.now(timezone.utc)
        )
        self.db.add(asst_msg)
        self.db.commit()
        self.db.refresh(asst_msg)

        return {
            "conversation_id": conversation.id,
            "message": asst_msg,
            "extracted_preferences": all_active_prefs,
            "matched_jobs": [m for m in self.db.query(Match).filter(Match.user_id == user_id).order_by(Match.score.desc()).limit(5).all()],
            "suggested_chips": llm_reply.get("suggested_chips", [])
        }
