from pydantic import BaseModel, Field
from typing import Dict

from copy import deepcopy

from fastapi import APIRouter
import app

from app.models.models import EntitiesOut
from app.models.models import UserRequestIn


router = APIRouter()

@router.post("/ml_api", response_model=EntitiesOut)
def classify_input(user_request: UserRequestIn):
    text = user_request.text

    return {"user_text": {"Testanfrage" : text}}