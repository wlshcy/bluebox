# from django.db import models

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

    def human_price(self):
        return self.price / 100

    def human_mprice(self):
        return self.mprice / 100

    def human_invent(self):
        return self.invent / 500

    def human_sales(self):
        return self.sales / 500

    def human_size(self):
        return self.size / 500
