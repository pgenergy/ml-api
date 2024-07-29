import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, Security
from fastapi_health import health
from fastapi.middleware.cors import CORSMiddleware

from app.models.models import check_api_key
from app.routers.ml_api.v3 import ml_api as ml_api_v3
from app.routers.ml_api.v4 import ml_api as ml_api_v4
from app.settings import Environments, Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)])
    logger = logging.getLogger()

    logger.info(f"Starting API in {settings.environment.value}")
    yield
    logger.info("Stopping API")


settings = Settings()

app = FastAPI(
    debug=settings.environment == Environments.Development,
    openapi_url="/openapi.json" if settings.environment == Environments.Development else None,
    lifespan=lifespan,
    title="Energyleaf ML-API",
    description="""Energyleaf ML-API""",
    version=settings.api_version,
    terms_of_service="https://github.com/pgenergy/ml-api/blob/main/LICENSE",
    contact={
        "name": "Energyleaf Uni Oldenburg",
        "url": "https://energyleaf.de",
    },
    openapi_tags=[
        {
            "name": "v3",
            "description": "JSON version"
        },
        {
            "name": "v4",
            "description": "Protobuf version",
            "externalDocs": {
                "description": "Energyleaf ML Protobuf definitions for Request and Response",
                "url": "https://github.com/pgenergy/Protocol/blob/main/proto/Energyleaf-ML.proto",
            }
        }
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)


def mock_health():
    return True


app.add_api_route("/health", health([mock_health]), dependencies=[Security(check_api_key)])
app.include_router(ml_api_v3.router, prefix="/v3", tags=["v3"], deprecated=True)
app.include_router(ml_api_v4.router, prefix="/v4", tags=["v4"])
