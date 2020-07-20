import json

from app.model import convert, predict
from app.db import predictions, database


async def generate_prediction(id: int, ticker: str):
    prediction_list = await predict(ticker)
    prediction_data = json.dumps(convert(prediction_list))

    query = predictions.update().where(
            id == predictions.c.id).values(ticker=ticker,
                                           prediction=prediction_data)
    return await database.execute(query=query)
