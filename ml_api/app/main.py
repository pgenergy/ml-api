import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.ml_api.v3 import ml_api as ml_api_v3
from app.routers.ml_api.v4 import ml_api as ml_api_v4
from app.settings import Settings

settings = Settings()

app = FastAPI(
    dependencies=[],
    title="Energyleaf ML-API",
    description="""Energyleaf ML-API""",
    version=settings.api_version,
    terms_of_service="#",
    contact={
        "name": "Energyleaf Uni Oldenburg",
        "url": "https://energyleaf.de",
    },
)

origins = [
    "http://localhost:4200",
]
if settings.origin:
    origins.append(settings.origin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(ml_api_v3.router, prefix="/v3", deprecated=True)
app.include_router(ml_api_v4.router, prefix="/v4")


@app.on_event("startup")
async def startup_event():
    logging.info("Starting API")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Stopping API")
