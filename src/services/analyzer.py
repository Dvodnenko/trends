from typing import List
from ..models.article import Article
from ..models.insight import Insight
from ..core.llm_client import LLMClient


llm = LLMClient(model="mistral")

def analyze_popularity(articles: List[Article]) -> List[Insight]:
    insights: List[Insight] = []

    for article in articles:
        prompt = (
            f"Article: \"{article.title}\".\n"
            f"Describe in short, why can this Article be popular"
            f"on the platform {article.source}."
        )

        reason = llm.ask(prompt)
        insights.append(Insight(article_title=article.title, reason=reason))

    return insights
