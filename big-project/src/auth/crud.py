from src.user.models import User
from sqlalchemy.orm import Session


def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()
