from sqlalchemy import String, ForeignKey
from src.models import CustomBase
from sqlalchemy.orm import Mapped, mapped_column


class BillingAddress(CustomBase):
    __tablename__ = "billing_address"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    zip_code: Mapped[str] = mapped_column(String(10))
    city: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
