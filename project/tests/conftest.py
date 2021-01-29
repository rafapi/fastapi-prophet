import os

import pytest
from starlette.testclient import TestClient

from app.main import create_application
from app import config


def get_settings_override():
    return config.Settings(
        testing=1, database_url=os.environ.get("DATABASE_TEST_URL")
    )


app = create_application()
app.dependency_overrides[config.get_settings] = get_settings_override


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as test_client:
        yield test_client
