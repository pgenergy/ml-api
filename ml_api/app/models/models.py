from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field
from fastapi import HTTPException, Security
from typing import Dict, List
from starlette import status

from app.settings import Settings

settings = Settings()

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


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
    dominant_classification: str
    classification: Dict[str, float]


class DeviceClassificationRequest(BaseModel):
    electricity: List[ElectricityInput]


class DeviceClassificationResponse(BaseModel):
    electricity: List[ElectricityOutput]


def check_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key")
    return api_key
