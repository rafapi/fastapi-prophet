from typing import List

from app.api import crud
from app.api.models import StockIn, StockOut
from fastapi import APIRouter, HTTPException, BackgroundTasks


router = APIRouter()


@router.post("/", response_model=StockOut, status_code=201)
async def create_prediction(payload: StockIn):
    prediction = await crud.post(payload)

    response_object = {
            "id": prediction.id,
            "ticker": payload.ticker,
            "prediction": payload.prediction
            }

    return response_object


@router.get("/{id}/")
async def get_prediction(id: int):
    prediction = await crud.get(id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction


@router.get("/", response_model=List[StockOut])
async def get_all_predictions():
    return await crud.get_all()
