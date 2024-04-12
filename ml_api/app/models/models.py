from pydantic import BaseModel, Field
from typing import Dict

class UserRequestIn(BaseModel):
    """ Example model for a user request with text parameter."""

    text: str = Field(...,
                        max_length=500,
                        description="Placeholder"
                     )


class EntityOut(BaseModel):
    """ Example model for a user response with text parameter."""

    text: str = Field(...,
                        max_length=500,
                        description="Placeholder"
                     )


class EntitiesOut(BaseModel):
    """ Example model for a user response with dict parameter."""

    user_text: Dict[str, str] = Field(...,
                                         max_length=500,
                                         description="Placeholder"
                                    )