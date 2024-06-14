from fastapi import APIRouter, Security


from app.models.models import check_api_key, unauthorized_response
from app.models.models import DeviceClassificationRequest, DeviceClassificationResponse
from src.classification.classify_devices import predict

router = APIRouter()


@router.post("/classify_devices",
             response_model=DeviceClassificationResponse,
             responses={**unauthorized_response})
def classify_input(user_request: DeviceClassificationRequest, api_key: str = Security(check_api_key)):
    predicted_devices = predict(user_request)

    return predicted_devices
