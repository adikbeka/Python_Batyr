from fastapi import FastAPI, Depends, status
from dependencies import get_db, get_queue
from schemas import GoodResponseSchema, GoodRequestSchema, GoodOptionalRequestSchema, PaymentRequestSchema, PaymentResponseSchema, PaymentOptionalRequestSchema
from models import Good, Payment
from typing import List
from tasks import hello_world
from datetime import datetime, timedelta
from scheduler import create_scheduler

app = FastAPI(dependencies=[Depends(get_db)],
              on_startup=[create_scheduler])


# Creating items
@app.post("/goods", response_model= GoodResponseSchema)
def create_good(good_schema: GoodRequestSchema) -> dict:
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
@app.get("/goods", response_model=List[GoodResponseSchema])
def get_all_goods():
    good_list = Good.select()

    response = [GoodResponseSchema.from_orm(item) for item in good_list]

    return response


# Updating items
@app.patch("/goods/{good_id}", response_model=GoodResponseSchema)
def update_good(good_id: int, good_body: GoodOptionalRequestSchema):

    good = Good.get_by_id(good_id)

    for key, value in good_body.dict(exclude_unset=True).items():
        setattr(good, key, value)

    good.save()

    response = GoodResponseSchema.from_orm(good)

    return response


# Deleting the item
@app.delete("/goods/{good_id}", status_code=status.HTTP_200_OK)
def delete_good(good_id: int):

    good = Good.get_by_id(good_id)

    good.delete_instance()

    return  {}


##################################################################
#Payment

@app.get("/payments/{days}", response_model=List[PaymentResponseSchema])
def get_all_payments(days:int):
    range = datetime.now() - timedelta(7)
    payment_list = Payment.select().where(Payment.status >= range)


    response = [PaymentResponseSchema.from_orm(item) for item in payment_list]

    return response


# Creating payment
@app.post("/payments", response_model= PaymentResponseSchema)
def create_payment(payment_schema: PaymentRequestSchema) -> dict:
    payment = Payment.create(
        good_id = payment_schema.good_id,
        created = datetime.now(),
        status = payment_schema.status,
        is_issed = payment_schema.is_issued
    )

    response = PaymentResponseSchema.from_orm(payment)

    return response.dict()


# @app.post("/approve-payment/{payment_id}")
# def approve_payment(payment_id:int, )

# Updating items
@app.patch("/payments/{payment_id}", response_model=PaymentResponseSchema)
def update_payment(payment_id: int, payment_body: PaymentOptionalRequestSchema):

    payment = Payment.get_by_id(payment_id)

    for key, value in payment_body.dict(exclude_unset=True).items():
        setattr(payment, key, value)

    payment.save()

    response = PaymentResponseSchema.from_orm(payment)

    return response


@app.post("/run-task")
def run_task():
    """
    Running task
    """
    queue = get_queue()
    queue.enqueue(hello_world)

    return {}
