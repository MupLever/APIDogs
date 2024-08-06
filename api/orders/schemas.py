from datetime import datetime

from pydantic import BaseModel, Field
from pydantic import validator


class OrderCreate(BaseModel):
    apartment_number: int = Field(gt=0)
    petname: str = Field(min_length=6, max_length=30)
    breed: str = Field(min_length=6, max_length=30)
    time: int = Field(gt=0, le=30)
    walk_datetime: datetime

    @validator("walk_datetime")
    def validate_walk_datetime(cls, value):
        if value.minute != 0 and value.minute != 30:
            raise ValueError("The walk can start either at the beginning of the hour or at half")

        if value.hour < 7 or value.hour > 22:
            raise ValueError("The earliest walk can start no earlier than 7 a.m., and the latest no later than 11 p.m.")

        return value
