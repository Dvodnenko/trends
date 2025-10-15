from typing import List
from ..schemas.article import Article
from ..schemas.insight import Insight
from ..core.llm_client import ask_gemini
from ..models import Request
from ..db import Session


class AnalyzerService:

    def __init__(self):
        self.ask = ask_gemini

    def __generate_prompt(self, article: Article):
        prompt = (
                f"Article: \"{article.title}\".\n"
                f"Describe in one or two sentence, why can this "
                f"Article be popular on the platform {article.source}."
            )
        return prompt

    def analyze_popularity(
            self, 
            article: Article, 
            save: bool = False
    ) -> Insight:
        insight: Insight = None

        with Session() as session:
            prompt = self.__generate_prompt(article)
            reason = self.ask(prompt)
            insight = Insight(
                source=article.source,
                title=article.title,
                url=article.url,
                id=article.id,
                score=article.score,
                created_at=article.created_at,
                reason=reason,
            )

            if save:
                req = Request(prompt=prompt, response=reason)
                session.add(req)

        if save: session.commit()

        return insight
