import praw

from ..core.config import config
from ..models.article import Article


def get_reddit_top(subreddit: str = "news", limit: int = 5) -> list[Article]:
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_SECRET,
        user_agent="scraper-bot"
    )
    articles = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        articles.append(Article(
            source="reddit",
            title=submission.title,
            url=f"https://reddit.com{submission.permalink}",
            score=submission.score,
            created_at=submission.created_utc
        ))
    return articles
