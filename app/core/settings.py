from typing import Literal

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    TITLE: str = "Roots"
    ENVIRONMENT: Literal["development", "production"] = "development"

    DATABASE_NAME: str = "roots"
    DATABASE_USER: str = "test"
    DATABASE_PASSWORD: str = "test"
    DATABASE_HOST: str = "test"
    DATABASE_PORT: int = 5432

    @computed_field
    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.DATABASE_USER,
            password=self.DATABASE_PASSWORD,
            host=self.DATABASE_HOST,
            port=self.DATABASE_PORT,
            path=self.DATABASE_NAME,
        )


settings = Settings()
