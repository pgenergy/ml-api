from fastapi import APIRouter, Security, Depends
from starlette import status
from starlette.exceptions import HTTPException

import logging
from typing import Annotated

from app.models.models import check_api_key, general_responses
from app.models.models import DeviceClassificationRequest, DeviceClassificationResponse
from app.settings import Settings, get_settings, Environments
from src.classification.classify_devices import predict

router = APIRouter()


@router.post("/classify_devices",
             response_model=DeviceClassificationResponse,
             responses={**general_responses})
def classify_input(
    user_request: DeviceClassificationRequest,
    api_key:  Annotated[str, Security(check_api_key)],
    settings: Annotated[Settings, Depends(get_settings)]
):
    try:
        predicted_devices = predict(user_request)
        return predicted_devices
    except Exception as e:
        logging.error(e)
        detail = None if settings.environment == Environments.Production else str(e)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
