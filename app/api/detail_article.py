from fastapi import APIRouter
from app.core.data import articles

router = APIRouter(prefix="/api/detail", tags=["detail_article"])

@router.get("/article/{article_id}")
def detail_article(article_id: int):
    detail_article = next((article for article in articles if article["id"] == article_id), None)
    return detail_article