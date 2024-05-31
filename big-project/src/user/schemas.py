from pydantic import BaseModel, EmailStr, constr
from typing import Annotated

password_pattern = (
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: Annotated[str, constr(pattern=password_pattern)]


class UserRead(UserBase):
    id: int
    status: str
    role: str
    password: str


class UserUpdate(UserBase):
    pass


class UserUpdatePassword(BaseModel):
    pass


class UserUpdateStatus(BaseModel):
    pass


class UserUpdateRole(BaseModel):
    pass
