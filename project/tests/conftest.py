import os

# import asyncio
import pytest
from fastapi.testclient import TestClient

from app.config import get_settings
from app.db import get_eng, get_db
from app.main import create_application
from app.models.sqlalchemy import metadata


settings = get_settings()


# @pytest.fixture(scope="module")
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture(scope="module")
def test_app():
    settings.testing = True
    settings.environment = "test"
    settings.database_url = os.getenv("DATABASE_TEST_URL")
    app = create_application()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def db():
    metadata.create_all(get_eng())
    database = get_db()
    yield database
