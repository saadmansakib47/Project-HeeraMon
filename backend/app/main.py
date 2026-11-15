from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.database import engine, Base, SessionLocal
from backend.app.api.v1.router import api_router
from backend.app.api.v1.endpoints.auth import get_or_create_default_user
from backend.app.ingestion.service import IngestionService

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all database tables on startup
    Base.metadata.create_all(bind=engine)
    
    # Initialize default user and run initial seed ingestion
    db = SessionLocal()
    try:
        get_or_create_default_user(db)
        ingestion = IngestionService(db)
        await ingestion.run_ingestion()
    finally:
        db.close()

    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="HeeraMon: AI-Powered Job-Seeking Wisdom Bird API",
    lifespan=lifespan
)

# CORS middleware for Next.js frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For seamless local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "HeeraMon API",
        "version": settings.VERSION,
        "llm_provider": settings.LLM_PROVIDER
    }
