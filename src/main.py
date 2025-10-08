from fastapi import FastAPI

from .api import articles_router, insights_router


application = FastAPI(
    title="Trends",
)

application.include_router(articles_router)
application.include_router(insights_router)
