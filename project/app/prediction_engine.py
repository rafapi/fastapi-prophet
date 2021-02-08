import json

from app.models.pydantic import StockIn
from app.models.sqlalchemy import predictions
from app.prophet import convert, predict

from fastapi import HTTPException


async def generate_prediction(id: int, ticker: StockIn, database):
    prediction_list = await predict(ticker)
    if not prediction_list:
        raise HTTPException(status_code=404, detail="No train model found")
    prediction_data = json.dumps(convert(prediction_list))

    query = (
        predictions.update()
        .where(id == predictions.c.id)
        .values(ticker=ticker, prediction=prediction_data)
    )
    return await database.execute(query=query)
