from datetime import datetime

from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    apartment_number: int = Field(gt=0)
    nickname: str = Field(min_length=6, max_length=30)
    breed: str = Field(min_length=6, max_length=30)
    time: int = Field(gt=0, le=30)
    walk_date: datetime
