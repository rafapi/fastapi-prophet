# import os
from typing import Optional

from databases import Database
from sqlalchemy import create_engine

from app.config import get_settings

database = Optional[Database]


settings = get_settings()


def get_eng():
    db_url = settings.database_url
    if settings.testing:
        engine = create_engine(db_url, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(db_url)
    return engine


def get_db() -> Database:
    global database
    db_url = settings.database_url
    if settings.testing:
        database = Database(db_url, force_rollback=True)
    else:
        database = Database(db_url)

    return database
