import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient, ASGITransport
from starlette import status

from .main import app, settings


@pytest.fixture
def anyio_backend():
    # we don't use trio
    return 'asyncio'


@pytest.fixture
async def client():
    async with LifespanManager(app) as manager:
        async with AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as client:
            yield client


@pytest.mark.anyio
async def test_v4_classify_devices_without_apikey(client: AsyncClient):
    response = await client.post("/v4/classify_devices")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.anyio
async def test_v4_classify_devices_without_body(client: AsyncClient):
    """422 so that it is equal with v3"""
    response = await client.post("/v4/classify_devices", headers={"X-API-Key": settings.api_key})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
