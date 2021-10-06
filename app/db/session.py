from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.POSTGRESQL_DATABASE_URI, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
