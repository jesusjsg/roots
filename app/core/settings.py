from typing import Literal

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    TITLE: str = "Roots"
    ENVIRONMENT: Literal["development", "production"] = "development"

    POSTGRES_DB: str = "roots"
    POSTGRES_USER: str = "test"
    POSTGRES_PASSWORD: str = "test"
    POSTGRES_HOST: str = "test"
    POSTGRES_PORT: int = 5432

    @computed_field
    @property
    def POSTGRES_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()
