from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from src.database import get_db
import src.user.service as user_service
from sqlalchemy.orm import Session
import src.user.schemas as user_schemas
from src.exceptions import AlreadyExistsError, NotFoundError

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[user_schemas.UserRead])
def get_users(db: Session = Depends(get_db)):
    return user_service.fetch_users(db)


@router.get("/{user_id}", response_model=user_schemas.UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return user_service.get_user(user_id, db)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=e.args[0])


@router.post(
    "/", response_model=user_schemas.UserRead, status_code=status.HTTP_201_CREATED
)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(user, db)
    except AlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=e.args[0])

# offical: put replace the whole object, patch update part of the object


@router.put("/{user_id}", response_model=user_schemas.UserRead)
def update_user(user_id: int, user: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    try:
        return user_service.update_user(user_id, user, db)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except AlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=e.args[0])

