from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field

# --- User Schemas ---
class UserBase(BaseModel):
    email: str
    name: str
    profile_data: Optional[Dict[str, Any]] = None

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# --- Preference Schemas ---
class PreferenceBase(BaseModel):
    category: str # salary, role, location, work_arrangement, hours, culture, benefits, commute
    value: str
    preference_type: str = "soft" # hard, soft, learned, unknown
    source: str = "explicit" # explicit, confirmed, inferred
    confidence: float = 1.0
    status: str = "active"
    raw_query: Optional[str] = None

class PreferenceCreate(PreferenceBase):
    pass

class PreferenceUpdate(BaseModel):
    value: Optional[str] = None
    preference_type: Optional[str] = None
    source: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None

class PreferenceResponse(PreferenceBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# --- Message & Conversation Schemas ---
class MessageBase(BaseModel):
    role: str
    content: str
    metadata_info: Optional[Dict[str, Any]] = None

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: str
    conversation_id: str
    timestamp: datetime

    class Config:
        from_attributes = True

class ConversationBase(BaseModel):
    title: Optional[str] = "Job Search Conversation"
    context_data: Optional[Dict[str, Any]] = None

class ConversationCreate(ConversationBase):
    pass

class ConversationResponse(ConversationBase):
    id: str
    user_id: str
    messages: List[MessageResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class SendMessageRequest(BaseModel):
    content: str
    user_id: Optional[str] = None


# --- Job Schemas ---
class JobBase(BaseModel):
    title: str
    company: str
    description: str
    location: Optional[str] = "Remote"
    work_arrangement: Optional[str] = "remote"
    employment_type: Optional[str] = "full-time"
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    salary_currency: Optional[str] = "BDT"
    commute_time_minutes: Optional[int] = None
    workday_hours: Optional[float] = None
    required_skills: Optional[List[str]] = []
    benefits: Optional[List[str]] = []
    culture_notes: Optional[str] = None
    application_url: Optional[str] = None
    status: Optional[str] = "active"

class JobResponse(JobBase):
    id: str
    first_seen_at: datetime
    last_seen_at: datetime

    class Config:
        from_attributes = True


# --- Match Schemas ---
class MatchResponse(BaseModel):
    id: str
    user_id: str
    job_id: str
    score: float
    eligibility_status: str
    satisfied_preferences: List[str] = []
    violated_preferences: List[str] = []
    unknown_information: List[str] = []
    trade_offs: List[str] = []
    explanation: Optional[str] = None
    job: Optional[JobResponse] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class MatchDecisionRequest(BaseModel):
    decision: str # interested, saved, rejected, applied
    reason: Optional[str] = None


# --- Application Schemas ---
class ApplicationBase(BaseModel):
    job_id: str
    tailored_notes: Optional[str] = None
    cover_letter: Optional[str] = None
    submission_data: Optional[Dict[str, Any]] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: str
    user_id: str
    status: str # draft, review, approved, submitted, cancelled
    job: Optional[JobResponse] = None
    submitted_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ApplicationApproveRequest(BaseModel):
    confirm_submission: bool = True


# --- Notification Schemas ---
class NotificationResponse(BaseModel):
    id: str
    user_id: str
    notification_type: str
    title: str
    content: str
    related_job_id: Optional[str] = None
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


# --- Conversational Turn Response ---
class ChatResponse(BaseModel):
    conversation_id: str
    message: MessageResponse
    extracted_preferences: List[PreferenceResponse] = []
    matched_jobs: List[MatchResponse] = []
    suggested_chips: List[str] = []
