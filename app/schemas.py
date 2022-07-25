from pydantic import BaseModel, validator, Field
from typing import Optional
from datetime import datetime


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


class PaymentResponseSchema(PaymentRequestSchema):
    id: int

    class Config:
        orm_mode = True


class PaymentOptionalRequestSchema(BaseModel):
    good_id: Optional[int]
    created: Optional[datetime]
    status: Optional[str]



