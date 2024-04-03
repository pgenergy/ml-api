from pydantic import BaseModel, Field
from typing import Dict

class UserRequestIn(BaseModel):
    """..."""

    text: str = Field(...,
                        max_length=500,
                        description="Placeholder"
                     )


class EntityOut(BaseModel):

    text: str = Field(...,
                        max_length=500,
                        description="Placeholder"
                     )


class EntitiesOut(BaseModel):

    user_text: Dict[str, str] = Field(...,
                                         max_length=500,
                                         description="Placeholder"
                                    )