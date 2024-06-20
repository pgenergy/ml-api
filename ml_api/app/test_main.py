from starlette import status
from fastapi.testclient import TestClient

from .main import app, settings

client = TestClient(app)


def test_v4_classify_devices_without_apikey():
    response = client.post("/v4/classify_devices")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_v4_classify_devices_without_body():
    """422 so that it is equal with v3"""
    response = client.post("/v4/classify_devices", headers={"X-API-Key": settings.api_key})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
