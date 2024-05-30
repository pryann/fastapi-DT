import src.user.models as user_models
from sqlalchemy.orm import Session

def fetch_users(db: Session):
    return db.query(user_models.User).all()
