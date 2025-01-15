import os
from pathlib import Path

from pydantic import BaseModel, Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    host: str = Field("localhost", alias="DB_HOST")
    port: int = Field(5432, alias="DB_PORT")
    user: str = Field("postgres", alias="DB_USER")
    name: str = Field("postgres", alias="DB_NAME")
    password: str = Field("secret", alias="DB_PASSWORD")
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")
    project_name: str = Field("Application", alias="PROJECT_NAME")

    db: DatabaseConfig = DatabaseConfig()

settings = Settings()