from app.models.pydantic import StockIn
from app.db import database
from app.models.sqlalchemy import predictions


async def inser_record(payload: StockIn):
    query = predictions.insert().values(ticker=payload.ticker)
    return await database.execute(query=query)


async def get_record(id: int):
    query = predictions.select().where(id == predictions.c.id)
    return await database.fetch_one(query=query)


async def get_all_records():
    query = predictions.select()
    return await database.fetch_all(query=query)
