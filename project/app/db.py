import os

from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
metadata = MetaData()


# databases query builder
def get_engine():
    engine = create_engine(DATABASE_URL)
    return engine


database = Database(DATABASE_URL)
