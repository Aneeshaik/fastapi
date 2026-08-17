from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://neondb_owner:npg_mMeSAb2np3tg@ep-proud-hat-ayhs82g6.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require"

    class ConfigDict:
        env_file = ".env"


settings = Settings()