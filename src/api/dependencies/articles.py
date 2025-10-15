from typing import Annotated

from fastapi import Depends

from ...scrappers import get_reddit_top, get_reddit_article
from ...schemas.article import Article


RedditArticles = Annotated[list[Article], Depends(get_reddit_top)]
RedditArticle = Annotated[Article, Depends(get_reddit_article)]
