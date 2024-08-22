from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from fastapi import HTTPException, Security
from typing import List
from starlette import status
from app.settings import Settings

settings = Settings()
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


class ElectricityInput(BaseModel):
    timestamp: str
    power: float


class PeakInput(BaseModel):
    peak_id: str
    electricity: List[ElectricityInput]


class DeviceClassificationRequest(BaseModel):
    peaks: List[PeakInput]


class ClassifiedDevices(BaseModel):
    name: str
    confidence: float


class PeakOutput(BaseModel):
    peak_id: str
    devices: List[ClassifiedDevices]


class DeviceClassificationResponse(BaseModel):
    peaks: List[PeakOutput]


def check_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key")
    return api_key


general_responses = {
    status.HTTP_401_UNAUTHORIZED: {
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"
                }
            }
        }
    },
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
