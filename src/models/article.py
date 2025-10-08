from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class Article(BaseModel):
    source: str
    title: str
    url: str
    id: str
    score: Optional[int] = None
    created_at: Optional[datetime] = None
