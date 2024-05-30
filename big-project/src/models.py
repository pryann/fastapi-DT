from humps import camel
from sqlalchemy import Column, DateTime, func
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


def to_camel(text):
    return camel(text)


class CustomBase(Base):
    __abstract__ = True

    creadted_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
