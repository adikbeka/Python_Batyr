from models import Payment
from datetime import datetime, timedelta

TIME_LIMIT = 60


def check_payment():
    payment_list = Payment.select().where(Payment.status == "new")

    for payment in payment_list:
        deadline = payment.date + timedelta(seconds=TIME_LIMIT)
        print(deadline, payment.status)
        if deadline < datetime.now():
            payment.status = "not paid"
            payment.save()



def issued_item(payment_id):
    payment = Payment.get_by_id(payment_id)
    payment.is_issued = True
    payment.save()

