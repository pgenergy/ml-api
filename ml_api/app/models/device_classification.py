from typing import List

from pydantic import BaseModel


# region Request

class ElectricityInput(BaseModel):
    timestamp: str
    power: float


class PeakInput(BaseModel):
    id: str
    electricity: List[ElectricityInput]


class DeviceClassificationRequest(BaseModel):
    peaks: List[PeakInput]


# endregion


# region Response

class ClassifiedDevices(BaseModel):
    name: str
    confidence: float


class PeakOutput(BaseModel):
    id: str
    devices: List[ClassifiedDevices]


class DeviceClassificationResponse(BaseModel):
    peaks: List[PeakOutput]


# endregion
