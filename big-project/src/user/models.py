from typing import List
from src.billing_address.models import BillingAddress
from src.models import CustomBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from sqlalchemy import Enum
from src.user.consts import UserStatusEnum, UserRolesEnum


class User(CustomBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(
        Enum(UserRolesEnum), default=UserRolesEnum.USER.value
    )
    status: Mapped[str] = mapped_column(
        Enum(UserStatusEnum), default=UserStatusEnum.UNVERIFIED.value
    )
    billing_adddress: Mapped[List["BillingAddress"]] = relationship(lazy="selectin")
