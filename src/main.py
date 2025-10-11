from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import articles_router, insights_router
from .db import mapping_registry, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    mapping_registry.metadata.create_all(engine)
    yield


application = FastAPI(
    title="Trends",
    lifespan=lifespan
)

application.add_middleware(
    CORSMiddleware, allow_origins="http://localhost:5173", 
    allow_methods=["8"])

application.include_router(articles_router)
application.include_router(insights_router)
