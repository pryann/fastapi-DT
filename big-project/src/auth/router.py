from fastapi import APIRouter, Depends, Response
from src.auth.schemas import AuthUser
from sqlalchemy.orm import Session
from src.database import get_db
import src.auth.service as auth_service
router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(response: Response, user: AuthUser, db: Session = Depends(get_db)):
    access_token = auth_service.login(user, db)
    response.set_cookie(key="access_token",
                        value=access_token, httponly=True, secure=True)
    return {}


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {}


@ router.post("/refresh-token")
def refresh_token():
    return {"message": "Refresh token successfully"}
