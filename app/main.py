from fastapi import FastAPI, Depends, status
from dependencies import get_db, get_queue
from schemas import GoodResponseSchema, GoodRequestSchema, GoodOptionalRequestSchema, PaymentRequestSchema, PaymentResponseSchema, PaymentOptionalRequestSchema
from models import Good, Payment
from typing import List
from tasks import issued_item, check_payment
from datetime import datetime, timedelta
from scheduler import create_scheduler

queue = get_queue()

app = FastAPI(dependencies=[Depends(get_db)],
              on_startup=[create_scheduler])


@app.post("/goods", response_model= GoodResponseSchema)
def create_good(good_schema: GoodRequestSchema) -> dict:

    """
    Creating items

    """

    good = Good.create(
        name = good_schema.name,
        price = good_schema.price,
        description = good_schema.description
    )

    response = GoodResponseSchema.from_orm(good)

    return response.dict()


@app.get("/goods/{good_id}")
def get_good(good_id: int) -> dict:
    """
    Getting index of item

    """

    good = Good.get_by_id(good_id)

    response = GoodResponseSchema.from_orm(good)

    return response.dict()


@app.get("/health")
def health() -> dict:
    """
    Health check

    """
    return {"status": "ok"}


@app.get("/goods", response_model=List[GoodResponseSchema])
def get_all_goods():
    """
    Get all items

    """

    good_list = Good.select()

    response = [GoodResponseSchema.from_orm(item) for item in good_list]

    return response


@app.patch("/goods/{good_id}", response_model=GoodResponseSchema)
def update_good(good_id: int, good_body: GoodOptionalRequestSchema):
    """
    Updating items

    """

    good = Good.get_by_id(good_id)

    for key, value in good_body.dict(exclude_unset=True).items():
        setattr(good, key, value)

    good.save()

    response = GoodResponseSchema.from_orm(good)

    return response


# Deleting the item
@app.delete("/goods/{good_id}", status_code=status.HTTP_200_OK)
def delete_good(good_id: int):
    """
    Deleting the item

    """

    good = Good.get_by_id(good_id)

    good.delete_instance()

    return  {}


##################################################################
#Payment

@app.get("/payments/{days}", response_model=List[PaymentResponseSchema])
def get_all_payments(days:int):
    """
    Get all payments

    """

    range = datetime.now() - timedelta(7)
    payment_list = Payment.select().where(Payment.status >= range)


    response = [PaymentResponseSchema.from_orm(item) for item in payment_list]

    return response


@app.post("/create-payment", response_model= PaymentResponseSchema)
def create_payment(payment_schema: PaymentRequestSchema) -> dict:
    """
    Creating payment

    """

    payment = Payment.create(
        good_id = payment_schema.good_id,
        created = datetime.now(),
        status = payment_schema.status,
        is_issued = payment_schema.is_issued
    )

    response = PaymentResponseSchema.from_orm(payment)

    return response.dict()


@app.post("/approve-payment/{payment_id}")
def approve_payment(payment_id:int):
    """
    Approve payment

    """

    paid_payment = Payment.get_by_id("payment_id")
    paid_payment.status = "paid"
    paid_payment.save()

    job = queue.enqueue(issued_item, payment_id)


@app.patch("/payments/{payment_id}", response_model=PaymentResponseSchema)
def update_payment(payment_id: int, payment_body: PaymentOptionalRequestSchema):
    """
    Updating items

    """

    payment = Payment.get_by_id(payment_id)

    for key, value in payment_body.dict(exclude_unset=True).items():
        setattr(payment, key, value)

    payment.save()

    response = PaymentResponseSchema.from_orm(payment)

    return response


@app.post("/check-payment-list")
def check_payment_list():
    """
    Running task
    """
    queue = get_queue()
    queue.enqueue(check_payment)

    return {}
