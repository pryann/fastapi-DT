import src.user.crud as user_crud
from sqlalchemy.orm import Session


def fetch_users(db: Session):
    return user_crud.fetch_users(db)
