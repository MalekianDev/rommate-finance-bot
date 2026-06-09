from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str

    model_config = dict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
