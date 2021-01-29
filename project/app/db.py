from fastapi import Depends
from databases import Database
from sqlalchemy import create_engine, MetaData
from app.config import Settings, get_settings


async def get_env(settings: Settings = Depends(get_settings)):
    return {
        "database_url": settings.database_url,
    }


DATABASE_URL = get_env()

# create database schema
metadata = MetaData()


def get_engine():
    # create engine to communicate with the database
    return create_engine(DATABASE_URL)


# databases query builder
database = Database(DATABASE_URL)
