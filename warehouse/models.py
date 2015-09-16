# Create your models here.


from mongoengine import *

from bluebox.settings import DATABASE

connect(host=DATABASE)


class Item(Document):
    name = StringField(required=True, max_length=30)
    photo = StringField(required=True)
    desc = StringField(required=True, max_length=15)
    size = IntField()
    price = IntField()
    mprice = IntField()
    origin = StringField()
    invent = IntField()
    sales = IntField(required=False, default=0)