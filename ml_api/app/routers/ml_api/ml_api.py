from pydantic import BaseModel, Field
from typing import Dict

from copy import deepcopy

from fastapi import APIRouter
import app

from app.models.models import EntitiesOut
from app.models.models import UserRequestIn

from src.classification.classify_devices import predict


router = APIRouter()

@router.post("/ml_api", response_model=EntitiesOut)
def classify_input(user_request: UserRequestIn):
    text = user_request.text

    return {"user_text": {"Testanfrage" : text}}


@router.post("/classify_devices", response_model=EntitiesOut)
def classify_input(user_request: UserRequestIn):
    text = user_request.text

    test = predict()

    return {"user_text": {"Testanfrage" : text}}