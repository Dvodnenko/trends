from pydantic import BaseModel


class Insight(BaseModel):
    article_title: str
    reason: str
