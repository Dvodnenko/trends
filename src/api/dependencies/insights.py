from typing import Annotated, List

from fastapi import Depends

from ...scrappers import get_reddit_article
from ...services.analyzer import AnalyzerService
from ...core.llm_client import LLMClient
from ...schemas.insight import Insight


def analyze_dep(
    id: str
):
    service = AnalyzerService(LLMClient("mistral"))
    r_article = get_reddit_article(post_id=id)
    insights = service.analyze_popularity([r_article], save=True)
    return insights


Analyze = Annotated[List[Insight], Depends(analyze_dep)]
