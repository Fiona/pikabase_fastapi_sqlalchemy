from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.elementtypes import ElementType
from app.db.utils import get_db

router = APIRouter()


@router.get("/")
def get_elementtypes(
    db: Session = Depends(get_db)
) -> Any:
    """
    Get Element types
    """
    return db.query(ElementType).all()
