from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class Article(BaseModel):
    source: str
    title: str
    url: str
    score: Optional[int] = None
    created_at: Optional[datetime] = None
