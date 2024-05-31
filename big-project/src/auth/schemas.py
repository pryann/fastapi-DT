from pydantic import BaseModel, EmailStr, constr


class AuthUser(BaseModel):
    email: EmailStr
    password: str
