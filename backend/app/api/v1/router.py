from fastapi import APIRouter
from backend.app.api.v1.endpoints import (
    auth, conversations, preferences, jobs, matches, notifications, applications
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(conversations.router, prefix="/conversations", tags=["Conversations"])
api_router.include_router(preferences.router, prefix="/preferences", tags=["Preferences"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
api_router.include_router(matches.router, prefix="/matches", tags=["Matches"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
api_router.include_router(applications.router, prefix="/applications", tags=["Applications"])
