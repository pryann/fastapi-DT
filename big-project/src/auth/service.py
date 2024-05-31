from sqlalchemy.orm import Session
from src.auth.schemas import AuthUser
from src.auth.crud import get_user_by_email
from src.exceptions import NotFoundError
from passlib.context import CryptContext
from bcrypt import hashpw, gensalt
from src.exceptions import NotFoundError, AuthencticationError
from jose import JWTError, jwt
from src.config import get_settings
from datetime import datetime, timedelta, timezone
# you can add salt too, in this case you need to write your own pass_hash function
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

settings = get_settings()


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def generate_access_token(id: int, email: str, role: str):
    payload = {"id": id, "email": email, "role": role}
    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRATION_MINUTES)
    payload.update({"exp": expire})
    token = jwt.encode(payload,
                       settings.JWT_ACCESS_TOKEN_SECRET_KEY
                       )
    return token


def login(user: AuthUser, db: Session):
    db_user = get_user_by_email(user.email, db)
    if db_user is None:
        raise NotFoundError("User not found")
    is_match = verify_password(user.password, db_user.password)
    if not is_match:
        raise AuthencticationError("Invalid password")
    access_token = generate_access_token(
        db_user.id, db_user.email, db_user.role)
    return access_token
