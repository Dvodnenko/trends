from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class Settings(BaseSettings):

    REDDIT_CLIENT_ID: str
    REDDIT_SECRET: str
    TWITTER_BEARER: str

settings = Settings()
