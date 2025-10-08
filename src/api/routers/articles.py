from fastapi import APIRouter

from ..dependencies.articles import (
    RedditArticles, TwitterArticles, RedditArticle)


articles_router = APIRouter(
    prefix="/articles", 
    tags=["articles"]
)


@articles_router.get("/reddit/all", tags=["reddit"])
def get_reddit_articles(data: RedditArticles):
    return data

@articles_router.get("/reddit", tags=["reddit"])
def get_reddit_article(data: RedditArticle):
    return data


@articles_router.get("/twitter", tags=["twitter"])
def get_twitter_articles(data: TwitterArticles):
    return data
