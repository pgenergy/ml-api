from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Security
from starlette import status
from app.settings import Settings

settings = Settings()
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def check_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key")
    return api_key


general_responses = {
    status.HTTP_401_UNAUTHORIZED: {
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"
                }
            }
        }
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"
                }
            }
        }
    }
}
