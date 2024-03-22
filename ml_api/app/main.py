import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.ml_api import ml_api
from app.settings import Settings

settings = Settings()

app = FastAPI(
    dependencies=[],
    title="Energyleaf ML-API",
    description="""Energyleaf ML-API""",
    version=settings.api_version,
    terms_of_service="#",
    contact={
        "company": "Energyleaf Uni Oldenburg",
        "url": "...",
        "email": "...",
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

app.include_router(ml_api.router)


@app.on_event("startup")
async def startup_event():
    logging.info("Starting API")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Stopping API")
