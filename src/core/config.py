import os

from pydantic import SecretStr
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from schemas.models import AllModelEnum 

load_dotenv()


class Settings(BaseSettings):

    OPENAI_API_KEY: SecretStr | None = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: SecretStr | None = None

    DEFAULT_MODEL: AllModelEnum | None = None

    POSTGRES_USER: str = os.getenv("POSTGRES_USER") 
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")

    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}?sslmode=disable"


    class Config(SettingsConfigDict):
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()
