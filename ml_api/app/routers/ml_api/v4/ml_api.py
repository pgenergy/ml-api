from google.protobuf.message import DecodeError
from google.protobuf import json_format
from typing import Annotated

from fastapi import APIRouter, Security, Response, Body, Depends
from starlette import status
from starlette.exceptions import HTTPException

from app.models.models import check_api_key, unauthorized_response
from app.models.Energyleaf_ML_pb2 import DeviceClassificationRequest, DeviceClassificationResponse
from src.classification.classify_devices import predict

router = APIRouter()


class ProtobufResponse(Response):
    media_type = "application/x-protobuf"

    def render(self, content) -> bytes:
        message = DeviceClassificationResponse()
        json_format.ParseDict(content, message)
        return message.SerializeToString()


def parse_protobuf_body(body: Annotated[bytes, Body(media_type="application/x-protobuf")]) -> DeviceClassificationRequest:
    message = DeviceClassificationRequest()
    try:
        message.ParseFromString(body)
    except DecodeError as e:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    return message


@router.post("/classify_devices",
             response_class=ProtobufResponse,
             responses={**unauthorized_response})
async def classify_input(
    api_key: Annotated[str, Security(check_api_key)],
    body: Annotated[DeviceClassificationRequest, Depends(parse_protobuf_body)]
):
    '''
    See <a href="https://github.com/pgenergy/Protocol/blob/main/proto/Energyleaf-ML.proto">Energyleaf ML Protobuf
    definitions</a> for Request and Response
    '''
    predicted_devices = predict(body)

    return predicted_devices

