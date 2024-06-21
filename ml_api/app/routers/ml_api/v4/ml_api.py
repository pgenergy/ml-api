from google.protobuf.message import DecodeError
from google.protobuf import json_format
from typing import Annotated

from fastapi import APIRouter, Security, Response, Body, Depends
from starlette import status
from starlette.exceptions import HTTPException

from app.models.models import check_api_key, general_responses
from app.models.Energyleaf_ML_pb2 import DeviceClassificationRequest, DeviceClassificationResponse
from src.classification.classify_devices import predict

router = APIRouter()


class ProtobufResponse(Response):
    media_type = "application/x-protobuf"

    def render(self, content) -> bytes:
        message = DeviceClassificationResponse()
        json_format.ParseDict(content, message)
        return message.SerializeToString()


def parse_protobuf_body(
    body: Annotated[bytes, Body(media_type="application/x-protobuf")]
) -> DeviceClassificationRequest:
    try:
        message = DeviceClassificationRequest()
        message.ParseFromString(body)
        return message
    except DecodeError as e:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))


@router.post("/classify_devices",
             response_class=ProtobufResponse,
             responses={**general_responses})
async def classify_input(
    api_key: Annotated[str, Security(check_api_key)],
    body: Annotated[DeviceClassificationRequest, Depends(parse_protobuf_body)]
):
    try:
        predicted_devices = predict(body)
        return predicted_devices
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
