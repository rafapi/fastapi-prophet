from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


# health-check
@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
