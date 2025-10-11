from typing import List
from ..schemas.article import Article
from ..schemas.insight import Insight
from ..core.llm_client import LLMClient
from ..models import Request
from ..db import Session


class AnalyzerService:

    def __init__(self, model: LLMClient):
        self._model = model

    def __generate_prompt(self, article: Article):
        prompt = (
                f"Article: \"{article.title}\".\n"
                f"Describe in one or two sentence, why can this "
                f"Article be popular on the platform {article.source}."
            )
        return prompt

    def analyze_popularity(
            self, 
            articles: List[Article], 
            save: bool = False
    ) -> List[Insight]:
        insights: List[Insight] = []

        with Session() as session:
            for article in articles:
                prompt = self.__generate_prompt(article)
                reason = self._model.ask(prompt)
                insights.append(Insight(article_title=article.title, 
                                        reason=reason))

                if save:
                    req = Request(prompt=prompt, response=reason)
                    session.add(req)

            if save: session.commit()

        return insights
