from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, Header, Depends, HTTPException
from typing import Dict
import pandas as pd

from app.settings import Settings

settings = Settings()

class UserRequestIn(BaseModel):
    """ Example model for a user request with text parameter."""

    text: str = Field(...,
                        max_length=500,
                        description="Placeholder"
                     )


class EntityOut(BaseModel):
    """ Example model for a user response with text parameter."""

    text: str = Field(...,
                        max_length=500,
                        description="Placeholder"
                     )


class EntitiesOut(BaseModel):
    """ Example model for a user response with dict parameter."""

    user_text: Dict[str, str] = Field(...,
                                         max_length=500,
                                         description="Placeholder"
                                    )

class ElectricityInput(BaseModel):
    timestamp: str
    power: float


class ElectricityOutput(BaseModel):
    timestamp: str
    power: float
    classification: str


class DeviceClassificationRequest(BaseModel):
    electricity: Dict[str, ElectricityInput]


class DeviceClassificationResponse(BaseModel):
    electricity: Dict[str, ElectricityOutput]


def check_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key