from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Auto generate the tablename from the class name."""
        return "".join(["_"+c.lower() if c.isupper() else c for c in cls.__name__]).lstrip("_")
