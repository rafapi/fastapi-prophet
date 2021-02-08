# import os
from typing import Optional

from databases import Database
from sqlalchemy import create_engine

from app.config import get_settings

database = Optional[Database]


def get_eng():
    settings = get_settings()
    dburl = settings.database_url
    if settings.testing:
        engine = create_engine(dburl, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(dburl)
    return engine


def get_db() -> Database:
    global database
    settings = get_settings()
    dburl = settings.database_url
    # if database.is_connected:
    #     database = database.connection()
    if settings.testing:
        database = Database(dburl, force_rollback=True)
    else:
        database = Database(dburl)

    return database
