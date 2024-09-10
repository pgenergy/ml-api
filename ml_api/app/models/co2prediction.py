from datetime import datetime
from typing import List
from enum import StrEnum

from pydantic import BaseModel


class Models(StrEnum):
    default = 'default'
    historic_average = 'historic-average'


class Co2PredictionInput(BaseModel):
    timestamp: datetime
    value: float


class Co2PredictionRequest(BaseModel):
    data: List[Co2PredictionInput]


class Co2PredictionOutput(BaseModel):
    timestamp: datetime
    value: float

class Co2PredictionResponse(BaseModel):
    used_model: Models
    data: list[Co2PredictionOutput]
