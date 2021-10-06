from fastapi import APIRouter

from app.api.api_v1.endpoints import test
from app.api.api_v1.endpoints import elementypes

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(elementypes.router, prefix="/elementtypes", tags=["elementtypes"])
