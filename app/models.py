from datetime import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Order(Base):
    __tablename__ = "orders"

    apartment_number: Mapped[int]
    nickname: Mapped[str]
    breed: Mapped[str]
    time: Mapped[int]
    walk_date: Mapped[datetime]
