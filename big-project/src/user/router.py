from fastapi import APIRouter, HTTPException, Depends
from src.database import get_db
import src.user.service as user_service
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    user = user_service.fetch_users(db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
