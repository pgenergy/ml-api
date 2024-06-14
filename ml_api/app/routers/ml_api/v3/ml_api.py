from fastapi import APIRouter, Security
from fastapi.security import APIKeyHeader


from app.models.models import UserRequestIn, EntitiesOut, check_api_key
from app.models.models import DeviceClassificationRequest, DeviceClassificationResponse
from src.classification.classify_devices import predict

router = APIRouter()


@router.post("/ml_api", response_model=EntitiesOut)
def classify_input(user_request: UserRequestIn, api_key: str = Security(check_api_key)):
    text = user_request.text

    return {"user_text": {"Testanfrage": text}}


@router.post("/classify_devices", response_model=DeviceClassificationResponse)
def classify_input(user_request: DeviceClassificationRequest, api_key: str = Security(check_api_key)):
    predicted_devices = predict(user_request)

    return predicted_devices
