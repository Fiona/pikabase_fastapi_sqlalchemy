from typing import Optional
from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_root():
    return {"Heloaoaeea,lo": "Woeoaeaoerld"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
