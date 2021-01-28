import os

from databases import Database
from sqlalchemy import create_engine, MetaData


# SQLAlchemy
metadata = MetaData()


def get_engine():
    # databases query builder
    return create_engine(os.getenv("DATABASE_URL"))


database = Database(os.getenv("DATABASE_URL"))
