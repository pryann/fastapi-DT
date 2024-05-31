import bcrypt
import src.user.crud as user_crud
import src.user.schemas as user_schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from bcrypt import hashpw, gensalt
from src.exceptions import NotFoundError, AlreadyExistsError

# you can add salt too, in this case you need to write your own pass_hash function
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)


# use bcrypt directly and add salt
# def hash_password(password: str):
#     salt = gensalt()
#     pwd_bytes = password.encode("utf-8")
#     hashed_password = hashpw(pwd_bytes, salt)
#     return hashed_password


def fetch_users(db: Session):
    return user_crud.fetch_users(db)


def get_user(user_id: int, db: Session):
    user = user_crud.get_user_by_id(user_id, db)
    if user is None:
        raise NotFoundError("User not found")
    return user


def create_user(user: user_schemas.UserCreate, db: Session):
    is_exists = user_crud.if_user_exists_with_username_or_email(
        user.username, user.email, db)
    if is_exists:
        raise AlreadyExistsError("User already exists")
    user.password = hash_password(user.password)
    return user_crud.create_user(user, db)


# def update_user(user_id: int, user: user_schemas.UserUpdate, db: Session):
#     db_user = user_crud.get_user_by_id(user_id, db)
#     if db_user is None:
#         raise NotFoundError("User not found")

#     is_exists = user_crud.if_user_exists_with_username_or_email(
#         user.username, user.email, db)
#     if is_exists:
#         raise AlreadyExistsError(
#             f"Username ({user.username}) or email address ({user.email}) alredy exists")

#     return user_crud.update_user(user_id, user, db)


def update_user(user_id: int, user: user_schemas.UserUpdate, db: Session):
    db_user = user_crud.get_user_by_id(user_id, db)
    if db_user is None:
        raise NotFoundError("User not found")

    is_exists = user_crud.if_user_exists_with_username_or_email(
        user.username, user.email, db)
    if is_exists:
        raise AlreadyExistsError(
            f"Username ({user.username}) or email address ({user.email}) alredy exists")

    return user_crud.update_user(db_user, user, db)


def delete_user(user_id: int, db: Session):
    db_user = user_crud.get_user_by_id(user_id, db)
    if db_user is None:
        raise NotFoundError("User not found")
    user_crud.delete_user(user_id, db)
    return
