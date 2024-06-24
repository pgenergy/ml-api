""" This module provides the applications settings
"""

from typing import Optional, Annotated

from pydantic import StringConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """This class provides the applications settings
    Values are automatically loaded from env and from the `.env`-file
    """
    model_config = SettingsConfigDict(env_file='.env')

    origin: Optional[str] = None
    api_version: str = "v2"
    api_key: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8)]
    models_path: str = "./models/"


settings = Settings()
