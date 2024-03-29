from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    REAL_DATABASE_URL: str
    model_config = SettingsConfigDict(env_file="src/.env", env_file_encoding="utf-8")


settings = Settings()
