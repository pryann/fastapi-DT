import src.user.models as user_models
import src.user.schemas as user_schemas
from sqlalchemy.orm import Session


def fetch_users(db: Session):
    return db.query(user_models.User).all()


def get_user_by_id(user_id: int, db: Session):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()


def if_user_exists_with_username_or_email(username: str, email: str, db: Session):
    return (
        db.query(user_models.User)
        .filter(
            user_models.User.email == email or user_models.User.username == username
        )
        .first()
    )


def create_user(user: user_schemas.UserCreate, db: Session):
    db_user = user_models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def update_user(user_id: int, user: user_schemas.UserUpdate, db: Session):
#     db_user = get_user_by_id(user_id, db)
#     user_data = user.model_dump()
#     for key, value in user_data.items():
#         setattr(db_user, key, value)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def update_user(db_user: user_models.User, user: user_schemas.UserUpdate, db: Session):
    user_data = user.model_dump()
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = get_user_by_id(user_id, db)
    db.delete(db_user)
    db.commit()
    return
