from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # project settings
    PROJECT_NAME: str = "restaurant"
    API_V1_STR: str = "/v1/restaurant"


settings = Settings()
