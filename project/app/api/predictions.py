from typing import List

from databases import Database
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Path

from app.api import crud
from app.db import setup_db
from app.models.pydantic import PredictionSchema, StockIn, StockOut
from app.prediction_engine import generate_prediction
from app.utils import pred_to_dict

router = APIRouter()


@router.post("/", response_model=StockOut, status_code=201)
async def create_prediction(
    payload: StockIn,
    background_tasks: BackgroundTasks,
    db: Database = Depends(setup_db),
):
    prediction_id = await crud.post(payload, db)

    background_tasks.add_task(generate_prediction, prediction_id, payload.ticker, db)

    response_object = {"id": prediction_id, "ticker": payload.ticker}

    return response_object


@router.get("/{id}/", response_model=PredictionSchema)
async def get_prediction(
    id: int = Path(..., gt=0), db: Database = Depends(setup_db)
) -> PredictionSchema:
    prediction_items = await crud.get(id, db)
    if not prediction_items:
        raise HTTPException(status_code=404, detail="Prediction not found")

    return pred_to_dict(prediction_items)


@router.get("/", response_model=List[PredictionSchema])
async def get_all_predictions(
    db: Database = Depends(setup_db),
) -> List[PredictionSchema]:
    prediction_items = await crud.get_all(db)
    if not prediction_items:
        raise HTTPException(status_code=404, detail="Predictions not found")
    return [pred_to_dict(pred) for pred in prediction_items]


@router.delete("/{id}/", response_model=PredictionSchema)
async def delete_prediction(
    id: int = Path(..., gt=0), db: Database = Depends(setup_db)
) -> PredictionSchema:
    prediction = await crud.get(id, db)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")

    await crud.delete(id, db)
    return pred_to_dict(prediction)
