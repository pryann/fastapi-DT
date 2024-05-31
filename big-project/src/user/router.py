from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from src.database import get_db
import src.user.service as user_service
from sqlalchemy.orm import Session
import src.user.schemas as user_schemas
from src.exceptions import AlreadyExistsError, NotFoundError
from fastapi import Cookie
from jose import JWTError, jwt
from src.config import get_settings
from src.exceptions import AuthorizationError

router = APIRouter(prefix="/users", tags=["Users"])
settings = get_settings()
# uer role check Deps


def check_user_role(allowed_roles: List[str]):
    async def _check_user_role(access_token: str = Cookie(None)):
        try:
            if not access_token:
                raise AuthorizationError("Access token is missing")
            payload = jwt.decode(
                access_token, settings.JWT_ACCESS_TOKEN_SECRET_KEY)
            if payload.get("role") not in allowed_roles:
                raise AuthorizationError(
                    "You don't have permission to access this route")
        except JWTError:
            raise JWTError("Invalid token")
        return access_token
    return _check_user_role


@router.get("/", response_model=List[user_schemas.UserRead])
def get_users(db: Session = Depends(get_db),  access_token: str = Depends(check_user_role(["ADMIN"]))):
    return user_service.fetch_users(db)


@ router.get("/{user_id}", response_model=user_schemas.UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(user_id, db)


@ router.post(
    "/", response_model=user_schemas.UserRead, status_code=status.HTTP_201_CREATED
)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(user, db)

# offical: put replace the whole object, patch update part of the object


@ router.put("/{user_id}", response_model=user_schemas.UserRead)
def update_user(user_id: int, user: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(user_id, user, db)


@ router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(user_id, db)
