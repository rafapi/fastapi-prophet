from fastapi import APIRouter, BackgroundTasks

from app.model import train
from app.models.pydantic import StockIn

router = APIRouter()


@router.post("/", status_code=201)
async def train_prediction(
    payload: StockIn,
    background_tasks: BackgroundTasks,
):

    background_tasks.add_task(train, payload.ticker)

    return payload
