""" This module provides the applications settings
"""

from typing import Optional, Annotated

from pydantic import StringConstraints
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """This class provides the applications settings
    Values are automatically loaded from env and from the `.env`-file
    """

    origin: Optional[str] = None
    api_version: str = "v2"
    api_key: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8)]

    class Config:
        """This class provides the config for the applications settings"""

        env_file = "./.env"


settings = Settings()