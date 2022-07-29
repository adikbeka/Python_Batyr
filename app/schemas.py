from pydantic import BaseModel, validator, Field
from typing import Optional
from datetime import datetime
from models import Good

MAX_PRICE = 100


class GoodRequestSchema(BaseModel):
    name: str
    price: int
    description: str


class GoodResponseSchema(GoodRequestSchema):
    id: int

    class Config:
        orm_mode = True


class GoodOptionalRequestSchema(BaseModel):
    name: Optional[str]
    price: Optional[int]
    Description: Optional[str]

###########################


class PaymentRequestSchema(BaseModel):
    good_id: int
    created: datetime
    status: str
    is_issued: bool

    @validator("good_id")
    def price_check(cls, v:int):
        good_price = Good.get_by_id(v)
        if good_price.price > MAX_PRICE:
            raise ValueError("The price of the good is more than 100")
        return v


class PaymentResponseSchema(PaymentRequestSchema):
    id: int

    class Config:
        orm_mode = True


class PaymentOptionalRequestSchema(BaseModel):
    good_id: Optional[int]
    created: Optional[datetime]
    status: Optional[str]
    is_issued: Optional[bool]



