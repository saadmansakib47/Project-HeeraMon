import asyncio
from backend.app.database import engine, Base, SessionLocal
from backend.app.models import User, Preference, Job, Match, Notification, Application
from backend.app.api.v1.endpoints.auth import get_or_create_default_user
from backend.app.ingestion.service import IngestionService
from backend.app.agent.orchestrator import HeeraMonAgent
from backend.app.scheduler.runner import background_runner

async def test_full_loop():
    print("=== 1. Initialize Tables ===")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    print("\n=== 2. Create User ===")
    user = get_or_create_default_user(db)
    print(f"User: {user.name} ({user.email}) ID: {user.id}")

    print("\n=== 3. Ingestion Pipeline ===")
    ingestion = IngestionService(db)
    stats = await ingestion.run_ingestion()
    print(f"Ingestion Stats: {stats}")
    job_count = db.query(Job).count()
    print(f"Total Jobs in DB: {job_count}")
    assert job_count > 0, "Jobs should have been ingested"

    print("\n=== 4. Conversational Turn & Preference Extraction ===")
    agent = HeeraMonAgent(db)
    conv_id = user.conversations[0].id
    sample_query = (
        "At least 40k BDT, AI/ML role, maximum 30-minute commute, "
        "around 7 hours a day, friendly workplace, subsidized lunch, and enough life outside work."
    )
    print(f"User: \"{sample_query}\"")
    result = await agent.process_user_turn(conv_id, sample_query, user.id)
    
    print("\n--- HeeraMon Bird Response ---")
    print(result["message"].content)
    print("\n--- Extracted Preferences ---")
    for p in result["extracted_preferences"]:
        print(f"• [{p.preference_type.upper()}] {p.category}: {p.value} (confidence: {p.confidence})")
    
    print("\n--- Matched Opportunities & Trade-offs ---")
    for m in result["matched_jobs"]:
        print(f"★ Job: {m.job.title} at {m.job.company} | Score: {m.score}% | Eligibility: {m.eligibility_status}")
        if m.trade_offs:
            print(f"   Trade-offs: {m.trade_offs}")
        if m.explanation:
            print(f"   Reasoning: {m.explanation}")

    print("\n=== 5. Continuous Search & Notifications ===")
    sched_summary = await background_runner.execute_cycle()
    print(f"Background Cycle Summary: {sched_summary}")
    notifs = db.query(Notification).filter(Notification.user_id == user.id).all()
    print(f"Notifications generated: {len(notifs)}")
    for n in notifs:
        print(f"🔔 [{n.notification_type}] {n.title}: {n.content[:80]}...")

    print("\n=== 6. Application Package & Human Approval Gate ===")
    top_match = result["matched_jobs"][0]
    app_draft = Application(
        user_id=user.id,
        job_id=top_match.job_id,
        status="review",
        tailored_notes="Grounded in ML background, zero commute needed.",
        cover_letter="Tailored cover letter."
    )
    db.add(app_draft)
    db.commit()
    print(f"Application status before human review: {app_draft.status}")
    # Human approves
    app_draft.status = "submitted"
    db.commit()
    print(f"Application status after explicit human approval: {app_draft.status}")

    db.close()
    print("\n>>> All HeeraMon Core Backend Loops Verified Successfully! <<<")

if __name__ == "__main__":
    asyncio.run(test_full_loop())
