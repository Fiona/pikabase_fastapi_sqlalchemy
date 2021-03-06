from fastapi import FastAPI

from app.config import settings
from app.api.api_v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_PATH)
