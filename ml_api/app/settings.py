""" This module provides the applications settings
"""

from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    """This class provides the applications settings
    Values are automatically loaded from env and from the `.env`-file
    """

    origin: Optional[str] = None
    api_version: str


    class Config:
        """This class provides the config for the applications settings"""

        env_file = ".env"