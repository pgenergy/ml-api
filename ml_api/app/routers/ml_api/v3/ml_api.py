from fastapi import APIRouter, Security
from starlette import status
from starlette.exceptions import HTTPException

from app.models.models import check_api_key, general_responses
from app.models.models import DeviceClassificationRequest, DeviceClassificationResponse
from src.classification.classify_devices import predict

router = APIRouter()


@router.post("/classify_devices",
             response_model=DeviceClassificationResponse,
             responses={**general_responses})
def classify_input(user_request: DeviceClassificationRequest, api_key: str = Security(check_api_key)):
    try:
        predicted_devices = predict(user_request)
        return predicted_devices
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
