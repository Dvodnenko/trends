from fastapi import APIRouter

from ..dependencies.insights import Analyze


insights_router = APIRouter()


@insights_router.post("/insights/analyze")
def analyze(data: Analyze):
    return data
