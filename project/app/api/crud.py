from databases import Database
from app.models.pydantic import StockIn
from app.models.sqlalchemy import predictions


async def post(payload: StockIn, db: Database):
    query = predictions.insert().values(ticker=payload.ticker)
    await db.connect()
    return await db.execute(query=query)


async def get(id: int, db: Database):
    query = predictions.select().where(id == predictions.c.id)
    await db.connect()
    return await db.fetch_one(query=query)


async def get_all(db: Database):
    query = predictions.select()
    await db.connect()
    return await db.fetch_all(query=query)


async def delete(id: int, db: Database):
    query = predictions.delete().where(id == predictions.c.id)
    return await db.execute(query=query)
