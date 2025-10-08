import praw

from .config import settings


def get_reddit_client():
    return praw.Reddit(
        client_id=settings.REDDIT_CLIENT_ID,
        client_secret=settings.REDDIT_SECRET,
        user_agent="scraper-bot"
    )
