from dependencies import get_db
from peewee import *


db = get_db()


class Good(Model):
    name = CharField(verbose_name="Name of the good")
    price = IntegerField(verbose_name="Price of the good")
    description = CharField(verbose_name="Description of the good")

    class Meta:
        database = db

class Payment(Model):
    good_id = ForeignKeyField
    created = DateTimeField(verbose_name="Date of the payment")
    status = CharField(verbose_name="Status of payment")

    class Meta:
        database = db


if __name__ == "__main__":
    db.create_tables([Good, Payment])

    # good1 = Good.create(name = "Snickers", price = 2, description = "There are 242 calories in 1 bar (50 g) of Snickers Snickers bar (50g). Calorie Breakdown: 43% fat, 50% carbs, 7% prot.")
    # good2 = Good.create(name="Twix", price=2, description = "There are 143 calories in 1 stick (29 g) of Twix Twix. Calorie Breakdown: 44% fat, 52% carbs, 4% prot.")
    # good3 = Good.create(name="Bounty", price=2, description = "There are 134 calories in 1 bar (28.5 g) of Bounty Coconut Covered Milk Chocolate Bar. Calorie Breakdown: 47% fat, 49% carbs, 4% prot.")
    # good4 = Good.create(name="Coca-Cola", price=3, description =" There are 137 calories in 1 can of Cola Soft Drink. Calorie Breakdown: 0% fat, 99% carbs, 1% prot.")
    # good5 = Good.create(name="Sprite", price=2.5, description = " There are 139 calories in 1 can (330 ml) of Sprite Sprite (Can). Calorie Breakdown: 0% fat, 100% carbs, 0% prot.")
    # good6 = Good.create(name="Fanta", price=2.5, description = "There are 150 calories in 1 bottle (500 ml) of Fanta Orange (500 ml). Calorie Breakdown: 0% fat, 100% carbs, 0% prot.")
    # good7 = Good.create(name="Lays", price=4, description = "There are 192 calories in 1 serving (36 g) of Lay's Lightly Salted. Calorie Breakdown: 59% fat, 37% carbs, 5% prot.")
    # good8 = Good.create(name="Pringles", price=6, description = "There are 210 calories in 1 serving (40 g) of Pringles Original. Calorie Breakdown: 58% fat, 40% carbs, 3% prot.")
    # good9 = Good.create(name="Sandwich", price=6, description = "There are 252 calories in 1 Sandwich. Calorie Breakdown: 43% fat, 44% carbs, 13% prot.")
    # good10 = Good.create(name="Haribo", price=3.5, description = "There are 336 calories in 100 g of Haribo Goldbears. Calorie Breakdown: 0% fat, 91% carbs, 8% prot.")

    # good1 = Good.create(good_name="Snickers", goods_price=2)
    # good2 = Good.create(good_name="Twix", goods_price=2)
    # good3 = Good.create(good_name="Bounty", goods_price=2)
    # good4 = Good.create(good_name="Coca-Cola", goods_price=
    # good5 = Good.create(good_name="Sprite", goods_price=2.5)
    # good6 = Good.create(good_name="Fanta", goods_price=2.5)
    # good7 = Good.create(good_name="Lays", goods_price=4)
    # good8 = Good.create(good_name="Pringles", goods_price=6)
    # good9 = Good.create(good_name="Sandwich", goods_price=6)
    # good10 = Good.create(good_name="Haribo", goods_price=3.5)

    # user1 = User(fist_name = "Bob", last_name = "David", age = 23, is_ill=True)
    # user1.save()
    #
    # user2 = User.create(fist_name = "Andrew", last_name = "Choo", age = 35, is_ill=False)
    # for item in Good.select():
    #     print(good_name,goods_price)