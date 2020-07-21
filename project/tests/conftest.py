import pytest
from starlette.testclient import TestClient

from app.main import create_application


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    client = TestClient(app)
    yield client
