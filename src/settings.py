from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """App settings."""

    host: str
    port: int
    log_level: str = "info"


app_settings = AppSettings()
