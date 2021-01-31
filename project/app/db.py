import os

from databases import Database
from sqlalchemy import create_engine, MetaData

# create database schema
metadata = MetaData()


def mk_engine(echo=False):
    dburl = os.getenv("DATABASE_URL")
    engine = create_engine(dburl, echo=echo)
    return engine


def setup_db():
    dburl = os.getenv("DATABASE_URL")
    database = Database(dburl)
    return database
