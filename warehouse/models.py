# Create your models here.


from mongoengine import *


class Item(Document):
    name = StringField(required=True, max_length=30)
    img = StringField(required=True)
    desc = StringField(required=True, max_length=15)
    size = IntField()
    price = IntField()
    mprice = IntField()
    origin = IntField()
    invent = IntField()