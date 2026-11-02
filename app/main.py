from fastapi import FastAPI

app = FastAPI()

# router
from app.routes.home import router as routes_home
app.include_router(routes_home)
from app.routes.detail_article import router as routes_detail_article
app.include_router(routes_detail_article)

# api
from app.api.articles import router as api_articles
app.include_router(api_articles)
from app.api.detail_article import router as api_detail_article
app.include_router(api_detail_article)