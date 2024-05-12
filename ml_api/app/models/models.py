from pydantic import BaseModel, Field
from typing import Dict

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
    classification_results: Dict[str, str]  # Beispiel: {"Reading1": "Kühlschrank", "Reading2": "Gefrierschrank", ...}
