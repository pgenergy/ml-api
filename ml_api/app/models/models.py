from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from fastapi import HTTPException, Security
from typing import Dict, List
from starlette import status

from app.settings import Settings

settings = Settings()

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


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


unauthorized_response = {
    status.HTTP_401_UNAUTHORIZED: {
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"
                }
            }
        }
    }
}

internalservererror_response = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"
                }
            }
        }
    }
}
