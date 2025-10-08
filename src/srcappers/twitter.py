from datetime import datetime, timezone

import tweepy

from ..core.config import config
from ..models.article import Article


def get_twitter_trending(query: str = "news", limit: int = 5) -> list[Article]:
    client = tweepy.Client(bearer_token=config.TWITTER_BEARER)
    
    tweets = client.search_recent_tweets(query=query, max_results=limit, tweet_fields=["created_at", "public_metrics"])
    
    articles = []
    if tweets.data:
        for tweet in tweets.data:
            metrics = tweet.public_metrics
            articles.append(Article(
                source="twitter",
                title=tweet.text,
                url=f"https://twitter.com/i/web/status/{tweet.id}",
                score=metrics.get("like_count"),
                created_at=tweet.created_at or datetime.now(timezone.utc)
            ))
    return articles
