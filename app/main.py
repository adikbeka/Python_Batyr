from fastapi import FastAPI, Depends
from dependencies import get_db
from schemas import GoodResponseSchema, GoodsRequestSchema
from models import Good, db
from fastapi.encoders import jsonable_encoder
from typing import List

app = FastAPI(dependencies=[Depends(get_db)])

# Creating items
@app.post("/goods")
def create_good(good_schema: GoodsRequestSchema) -> dict:
    good = Good.create(
        name = good_schema.name,
        price = good_schema.price,
        description = good_schema.description
    )

    response = GoodResponseSchema.from_orm(good)

    return response.dict()


# Getting index of item
@app.get("/goods/{good_id}")
def get_good(good_id: int) -> dict:
    good = Good.get_by_id(good_id)

    response = GoodResponseSchema.from_orm(good)

    return response.dict()


# Test
@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# Get all items
@app.get("/goods")
def get_all_goods(goods: int) -> dict:
    good = Good.get(goods)

    response = GoodResponseSchema.from_orm(good)

    return response.dict()


# Updating items
@app.put("/goods/{good_id}", response_model=GoodsRequestSchema)
def update_good(good_id: str, good: GoodsRequestSchema):
    update_good_encoded = jsonable_encoder(good)
    Good[good_id] = update_good_encoded
    return update_good_encoded


# Deleting the item
@app.delete("/goods/{good_id}")
def delete_good(good_id: int):
    return {"good": [f"delete good {good_id}"]}


