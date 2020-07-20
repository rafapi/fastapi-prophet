from app.api.models import StockIn
from app.db import predictions, database


async def post(payload: StockIn):
    query = predictions.insert().values(ticker=payload.ticker)
    return await database.execute(query=query)


async def get(id: int):
    query = predictions.select().where(id == predictions.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = predictions.select()
    return await database.fetch_all(query=query)
