import os

from databases import Database
from sqlalchemy import create_engine
from app.models.sqlalchemy import metadata


def mk_engine():
    dburl = os.getenv("DATABASE_URL")
    if os.getenv("TESTING"):
        engine = create_engine(
            dburl, connect_args={"check_same_thread": False}
        )
    else:
        engine = create_engine(dburl)

    metadata.create_all(engine)


def setup_db() -> Database:
    dburl = os.getenv("DATABASE_URL")
    if os.getenv("TESTING"):
        database = Database(dburl, force_rollback=True)
    else:
        database = Database(dburl)
    return database
