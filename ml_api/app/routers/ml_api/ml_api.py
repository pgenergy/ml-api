from pydantic import BaseModel, Field
from typing import Dict

from copy import deepcopy

from fastapi import APIRouter
import app

from app.models.models import UserRequestIn, EntitiesOut
from app.models.models import DeviceClassificationRequest, DeviceClassificationResponse



from src.classification.classify_devices import predict


router = APIRouter()

@router.post("/ml_api", response_model=EntitiesOut)
def classify_input(user_request: UserRequestIn):
    text = user_request.text

    return {"user_text": {"Testanfrage" : text}}


@router.post("/classify_devices", response_model=DeviceClassificationResponse)
def classify_input(user_request: DeviceClassificationRequest):
    print(user_request)

    test = predict()

    test = {
        "timestamp": "2024-05-10T12:35:00",
        "power": 1800.0,
        "classification": "Gefrierschrank"
    }

    return {"user_text": {"electricity" : test}}