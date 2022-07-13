from peewee import *
from environs import Env

environment = Env()
environment.read_env()

DB_NAME = environment("DB_NAME")
DB_URI = environment("DB_URI")

db = PostgresqlDatabase(
    database= DB_NAME,
    dsn = DB_URI,

)

db.connect()


class Good(Model):
    good_name = CharField(verbose_name="Name of the good")
    goods_price = IntegerField(verbose_name="Price of the good")
    # goods_description = CharField(verbose_name="Description of the good")

    class Meta:
        database = db


if __name__ == "__main__":
    db.create_tables([Good])

    # good1 = Good.create(good_name = "Snickers", goods_price = 2, goods_description = "There are 242 calories in 1 bar (50 g) of Snickers Snickers bar (50g). Calorie Breakdown: 43% fat, 50% carbs, 7% prot.")
    # good2 = Good.create(good_name="Twix", goods_price=2, goods_description = "There are 143 calories in 1 stick (29 g) of Twix Twix. Calorie Breakdown: 44% fat, 52% carbs, 4% prot.")
    # good3 = Good.create(good_name="Bounty", goods_price=2, goods_description = "There are 134 calories in 1 bar (28.5 g) of Bounty Coconut Covered Milk Chocolate Bar. Calorie Breakdown: 47% fat, 49% carbs, 4% prot.")
    # good4 = Good.create(good_name="Coca-Cola", goods_price=3, goods_description = " There are 137 calories in 1 can of Cola Soft Drink. Calorie Breakdown: 0% fat, 99% carbs, 1% prot.")
    # good5 = Good.create(good_name="Sprite", goods_price=2.5, goods_description = " There are 139 calories in 1 can (330 ml) of Sprite Sprite (Can). Calorie Breakdown: 0% fat, 100% carbs, 0% prot.")
    # good6 = Good.create(good_name="Fanta", goods_price=2.5, goods_description = "There are 150 calories in 1 bottle (500 ml) of Fanta Orange (500 ml). Calorie Breakdown: 0% fat, 100% carbs, 0% prot.")
    # good7 = Good.create(good_name="Lays", goods_price=4, goods_description = "There are 192 calories in 1 serving (36 g) of Lay's Lightly Salted. Calorie Breakdown: 59% fat, 37% carbs, 5% prot.")
    # good8 = Good.create(good_name="Pringles", goods_price=6, goods_description = "There are 210 calories in 1 serving (40 g) of Pringles Original. Calorie Breakdown: 58% fat, 40% carbs, 3% prot.")
    # good9 = Good.create(good_name="Sandwich", goods_price=6, goods_description = "There are 252 calories in 1 Sandwich. Calorie Breakdown: 43% fat, 44% carbs, 13% prot.")
    # good10 = Good.create(good_name="Haribo", goods_price=3.5, goods_description = "There are 336 calories in 100 g of Haribo Goldbears. Calorie Breakdown: 0% fat, 91% carbs, 8% prot.")

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
    for item in Good.select():
        print(good_name,goods_price)