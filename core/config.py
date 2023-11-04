from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class DbSettings(BaseModel):
  host: str = os.environ.get("DB_HOST")
  name: str = os.environ.get("DB_NAME")
  password: str = os.environ.get("DB_PASS")
  user: str = os.environ.get("DB_USER")
  port: int = os.environ.get("DB_PORT")
  url: str = f"postgresql+asyncpg://{user}:{password}@{host}/{name}"
  echo: bool = True


class Settings(BaseSettings):
  api_v1_prefix: str = "/api/v1"
  db: DbSettings = DbSettings()


settings = Settings()
print(settings.db.url)
