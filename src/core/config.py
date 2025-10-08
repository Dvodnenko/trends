import os

from dotenv import load_dotenv


load_dotenv()

class Config:
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_SECRET = os.getenv("REDDIT_SECRET")
    TWITTER_BEARER = os.getenv("TWITTER_BEARER")

config = Config()
