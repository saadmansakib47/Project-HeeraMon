import uuid
from datetime import datetime, timezone
from sqlalchemy import (
    Column, String, Integer, Float, Boolean, Text, DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import relationship
from backend.app.database import Base

def generate_uuid():
    return str(uuid.uuid4())

def utc_now():
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    profile_data = Column(JSON, default=dict) # e.g. skills, current_location, cv_summary
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    preferences = relationship("Preference", back_populates="user", cascade="all, delete-orphan")
    conversations = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")
    matches = relationship("Match", back_populates="user", cascade="all, delete-orphan")
    decisions = relationship("UserDecision", back_populates="user", cascade="all, delete-orphan")
    applications = relationship("Application", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")


class Preference(Base):
    __tablename__ = "preferences"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    category = Column(String(64), nullable=False) # salary, role, location, work_arrangement, hours, culture, benefits, commute
    value = Column(String(255), nullable=False)
    preference_type = Column(String(32), default="soft") # hard, soft, learned, unknown
    source = Column(String(32), default="explicit") # explicit, confirmed, inferred
    confidence = Column(Float, default=1.0)
    status = Column(String(32), default="active") # active, superseded, archived
    raw_query = Column(String(500), nullable=True) # conversational snippet that triggered it
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    user = relationship("User", back_populates="preferences")


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    title = Column(String(255), default="Job Search Conversation")
    context_data = Column(JSON, default=dict)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan", order_by="Message.timestamp")


class Message(Base):
    __tablename__ = "messages"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    conversation_id = Column(String(36), ForeignKey("conversations.id"), index=True, nullable=False)
    role = Column(String(32), nullable=False) # user, assistant, system
    content = Column(Text, nullable=False)
    metadata_info = Column(JSON, default=dict) # e.g. extracted_preferences, tool_calls, matched_jobs
    timestamp = Column(DateTime(timezone=True), default=utc_now)

    conversation = relationship("Conversation", back_populates="messages")


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    title = Column(String(255), index=True, nullable=False)
    company = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(255), default="Remote")
    work_arrangement = Column(String(32), default="remote") # remote, hybrid, onsite
    employment_type = Column(String(32), default="full-time")
    salary_min = Column(Float, nullable=True)
    salary_max = Column(Float, nullable=True)
    salary_currency = Column(String(16), default="BDT")
    commute_time_minutes = Column(Integer, nullable=True)
    workday_hours = Column(Float, nullable=True)
    required_skills = Column(JSON, default=list)
    benefits = Column(JSON, default=list)
    culture_notes = Column(Text, nullable=True)
    application_url = Column(String(512), nullable=True)
    status = Column(String(32), default="active")
    dedup_hash = Column(String(64), unique=True, index=True, nullable=True)
    first_seen_at = Column(DateTime(timezone=True), default=utc_now)
    last_seen_at = Column(DateTime(timezone=True), default=utc_now)

    source_records = relationship("JobSourceRecord", back_populates="job", cascade="all, delete-orphan")
    matches = relationship("Match", back_populates="job", cascade="all, delete-orphan")
    decisions = relationship("UserDecision", back_populates="job", cascade="all, delete-orphan")
    applications = relationship("Application", back_populates="job", cascade="all, delete-orphan")


class JobSource(Base):
    __tablename__ = "job_sources"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(128), unique=True, nullable=False) # e.g. "RemoteOK", "Arbeitnow", "Curated Tech"
    source_type = Column(String(32), nullable=False) # api, rss, curated
    source_url = Column(String(512), nullable=True)
    status = Column(String(32), default="active")
    last_sync_at = Column(DateTime(timezone=True), nullable=True)
    error_info = Column(Text, nullable=True)

    records = relationship("JobSourceRecord", back_populates="source")


class JobSourceRecord(Base):
    __tablename__ = "job_source_records"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    job_id = Column(String(36), ForeignKey("jobs.id"), index=True, nullable=False)
    source_id = Column(String(36), ForeignKey("job_sources.id"), index=True, nullable=False)
    external_job_id = Column(String(255), index=True, nullable=True)
    source_url = Column(String(512), nullable=True)
    raw_data = Column(JSON, default=dict)
    first_seen_at = Column(DateTime(timezone=True), default=utc_now)
    last_seen_at = Column(DateTime(timezone=True), default=utc_now)

    job = relationship("Job", back_populates="source_records")
    source = relationship("JobSource", back_populates="records")


class Match(Base):
    __tablename__ = "matches"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    job_id = Column(String(36), ForeignKey("jobs.id"), index=True, nullable=False)
    score = Column(Float, default=0.0)
    eligibility_status = Column(String(32), default="eligible") # eligible, ineligible, review
    satisfied_preferences = Column(JSON, default=list)
    violated_preferences = Column(JSON, default=list)
    unknown_information = Column(JSON, default=list)
    trade_offs = Column(JSON, default=list)
    explanation = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    user = relationship("User", back_populates="matches")
    job = relationship("Job", back_populates="matches")


class UserDecision(Base):
    __tablename__ = "user_decisions"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    job_id = Column(String(36), ForeignKey("jobs.id"), index=True, nullable=False)
    decision = Column(String(32), nullable=False) # interested, saved, rejected, applied
    reason = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True), default=utc_now)

    user = relationship("User", back_populates="decisions")
    job = relationship("Job", back_populates="decisions")


class Application(Base):
    __tablename__ = "applications"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    job_id = Column(String(36), ForeignKey("jobs.id"), index=True, nullable=False)
    status = Column(String(32), default="draft") # draft, review, approved, submitted, cancelled
    tailored_notes = Column(Text, nullable=True)
    cover_letter = Column(Text, nullable=True)
    submission_data = Column(JSON, default=dict)
    submitted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    notification_type = Column(String(32), nullable=False) # new_match, preference_suggestion, alert
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    related_job_id = Column(String(36), ForeignKey("jobs.id"), nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=utc_now)

    user = relationship("User", back_populates="notifications")


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    task_type = Column(String(64), nullable=False) # background_search, preference_learning, ingestion
    status = Column(String(32), default="completed") # running, completed, failed
    input_context = Column(JSON, default=dict)
    result_summary = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    started_at = Column(DateTime(timezone=True), default=utc_now)
    completed_at = Column(DateTime(timezone=True), default=utc_now)
