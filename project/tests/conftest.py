import os

# import asyncio
import pytest

# import nest_asyncio

from fastapi.testclient import TestClient

from app.db import mk_engine, setup_db
from app.config import Settings, get_settings
from app.main import create_application

# nest_asyncio.apply()


def get_settings_override():
    return Settings(testing=1, database_url=os.getenv("DATABASE_TEST_URL"))


@pytest.fixture(autouse=True, scope="module")
def test_app():
    settings = get_settings()
    settings.testing = True
    settings.environment = "test"
    settings.database_url = os.getenv("DATABASE_TEST_URL")
    app = create_application()
    with TestClient(app) as test_client:
        yield test_client


# @pytest.fixture(scope="session")
# def event_loop():
#     yield asyncio.get_event_loop()


@pytest.fixture(scope="module")
def db(test_app):
    mk_engine()
    db = setup_db()
    try:
        yield db
    finally:
        db.disconnect()
