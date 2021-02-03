import os
import pathlib
from typing import List

from fastapi import APIRouter, BackgroundTasks, HTTPException, Path

from app.api import crud
from app.models.pydantic import PredictionSchema, StockIn, StockOut
from app.prediction_engine import generate_prediction
from app.utils import pred_to_dict

router = APIRouter()


BASE_DIR = pathlib.Path(__file__).resolve(strict=True).parent.parent
TRAINED_DIR = pathlib.Path(BASE_DIR) / "trained"


@router.post("/", response_model=StockOut, status_code=201)
async def create_prediction(
    payload: StockIn,
    background_tasks: BackgroundTasks,
):
    model_file = TRAINED_DIR / f"{payload.ticker}.joblib"
    for entry in os.listdir(TRAINED_DIR):
        if os.path.isfile(os.path.join(TRAINED_DIR, entry)):
            print(entry)
    if not model_file.exists():
        raise HTTPException(status_code=404, detail="No train model found")
    prediction_id = await crud.post(payload)

    background_tasks.add_task(
        generate_prediction, prediction_id, payload.ticker
    )

    response_object = {"id": prediction_id, "ticker": payload.ticker}

    return response_object


@router.get("/{id}/", response_model=PredictionSchema)
async def get_prediction(id: int = Path(..., gt=0)) -> PredictionSchema:
    prediction_items = await crud.get(id)
    if not prediction_items:
        raise HTTPException(status_code=404, detail="Prediction not found")

    return pred_to_dict(prediction_items)


@router.get("/", response_model=List[PredictionSchema])
async def get_all_predictions() -> List[PredictionSchema]:
    prediction_items = await crud.get_all()
    if not prediction_items:
        raise HTTPException(status_code=404, detail="Predictions not found")
    return [pred_to_dict(pred) for pred in prediction_items]


@router.delete("/{id}/", response_model=PredictionSchema)
async def delete_prediction(id: int = Path(..., gt=0)) -> PredictionSchema:
    prediction = await crud.get(id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")

    await crud.delete(id)

    return pred_to_dict(prediction)
