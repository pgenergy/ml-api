""" This module provides the applications settings
"""

from enum import Enum
from functools import lru_cache
from typing import Annotated

from pydantic import StringConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environments(str, Enum):
    Development = "Development"
    Production = "Production"


class Settings(BaseSettings):
    """This class provides the applications settings
    Values are automatically loaded from env and from the `.env`-file
    """
    model_config = SettingsConfigDict(env_file='.env', extra="ignore")

    api_key: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8)]
    api_version: str = "v4"
    environment: Environments = Environments.Production
    models_path: str = "./models/"
    origins: frozenset[str] = ["http://localhost:*", "https://energyleaf.de"]

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


@lru_cache
def get_settings():
    return Settings()

