from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import Job
from backend.app.schemas import JobResponse
from backend.app.ingestion.service import IngestionService

router = APIRouter()

@router.get("", response_model=List[JobResponse])
def get_jobs(
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    return db.query(Job).filter(Job.status == "active").order_by(Job.first_seen_at.desc()).offset(offset).limit(limit).all()

@router.get("/{job_id}", response_model=JobResponse)
def get_job_by_id(job_id: str, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/ingest")
async def trigger_job_ingestion(db: Session = Depends(get_db)):
    service = IngestionService(db)
    stats = await service.run_ingestion()
    return {"status": "success", "stats": stats}
