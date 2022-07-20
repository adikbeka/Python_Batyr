from pydantic import BaseModel


class GoodsRequestSchema(BaseModel):
    name: str
    price: int
    description: str

class GoodResponseSchema(GoodsRequestSchema):
    id: int

    class Config:
        orm_mode = True
