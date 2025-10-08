from ..schemas.article import Article
from ..core.reddit_client import get_reddit_client


def get_reddit_top(subreddit: str = "news", limit: int = 5) -> list[Article]:
    reddit = get_reddit_client()
    articles = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        articles.append(Article(
            source="reddit",
            title=submission.title,
            url=f"https://reddit.com{submission.permalink}",
            score=submission.score,
            created_at=submission.created_utc,
            id=submission.id
        ))
    return articles


def get_reddit_article(post_id: str) -> Article:
    reddit = get_reddit_client()
    submission = reddit.submission(id=post_id)

    return Article(
        source="reddit",
        title=submission.title,
        url=f"https://reddit.com{submission.permalink}",
        score=submission.score,
        created_at=submission.created_utc,
        id=submission.id
    )
