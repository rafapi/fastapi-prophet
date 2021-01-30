import os

from databases import Database
from sqlalchemy import create_engine, MetaData


DATABASE_URL = os.getenv("DATABASE_URL")

# create database schema
metadata = MetaData()


def get_engine():
    # create engine to communicate with the database
    return create_engine(DATABASE_URL)


# databases query builder
if DATABASE_URL is not None:
    database = Database(DATABASE_URL)
else:
    database = None
