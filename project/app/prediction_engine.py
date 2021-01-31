import json

from app.models.pydantic import StockIn
from app.models.sqlalchemy import predictions
from app.prophet import convert, predict


async def generate_prediction(id: int, ticker: StockIn, db):
    prediction_list = await predict(ticker)
    prediction_data = json.dumps(convert(prediction_list))

    query = (
        predictions.update()
        .where(id == predictions.c.id)
        .values(ticker=ticker, prediction=prediction_data)
    )
    await db.connect()
    return await db.execute(query=query)
