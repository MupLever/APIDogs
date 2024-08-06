import enum
from datetime import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
)


class Walker(enum.Enum):
    Petr = "petr"
    Anton = "anton"


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Order(Base):
    __tablename__ = "orders"

    apartment_number: Mapped[int] = mapped_column(nullable=False)
    petname: Mapped[str] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=False)
    time: Mapped[int] = mapped_column(nullable=False)
    walk_datetime: Mapped[datetime] = mapped_column(nullable=False)
    walker: Mapped[Walker] = mapped_column(nullable=False)
