from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.core.data import articles
from app.core.templating import templates

router = APIRouter()

@router.get("/detail/article/{article_id}", response_class=HTMLResponse)
def detail_article(article_id: int, request: Request):
    # detail_article = next((article for article in articles if article["id"] == article_id), None)
    return templates.TemplateResponse(request=request, name="detail_article.html")