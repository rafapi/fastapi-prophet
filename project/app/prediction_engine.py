import json

from app.models.pydantic import StockIn
from app.db import database
from app.models.sqlalchemy import predictions
from app.prophet import convert, predict


async def generate_prediction(id: int, ticker: StockIn):
    prediction_list = await predict(ticker)
    prediction_data = json.dumps(convert(prediction_list))

    query = (
        predictions.update()
        .where(id == predictions.c.id)
        .values(ticker=ticker, prediction=prediction_data)
    )
    return await database.execute(query=query)
