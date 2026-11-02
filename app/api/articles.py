from fastapi import APIRouter
from app.core.data import articles

router = APIRouter(prefix="/api/data", tags=["article"])

@router.get("/articles")
def article():
    return articles