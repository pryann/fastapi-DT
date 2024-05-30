from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.config import get_settings


settings = get_settings()
charset = "utf8mb4"
SQLALCHEMY_DATABASE_URL = f"{settings.MYSQL_DATABASE_URL}?charset={charset}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
