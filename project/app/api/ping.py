from fastapi import APIRouter


router = APIRouter()


# health-check
@router.get("/ping")
async def pong():
    return {"ping": "pong!"}
