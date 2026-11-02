from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.core.templating import templates
from app.core.data import articles

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    print(articles)
    return templates.TemplateResponse(request=request, name="home.html")