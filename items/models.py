# from django.db import models

# Create your models here.
import time
from mongoengine import *

from bluebox.settings import DATABASE

connect(host=DATABASE)


class Item(Document):
    name = StringField(required=True, max_length=30)
    photo = StringField(required=True)
    desc = StringField(required=True, max_length=15)
    size = FloatField(required=True)
    price = FloatField(required=True)
    mprice = FloatField(required=True)
    origin = StringField(required=True)
    invent = IntField(required=True)
    sales = FloatField(required=False)
    created = DateTimeField()

    # def human_price(self):
    #     return self.price / 100
    #
    # def human_mprice(self):
    #     return self.mprice / 100
    #
    # def human_invent(self):
    #     return self.invent / 500
    #
    # def human_sales(self):
    #     return self.sales / 500
    #
    # def human_size(self):
    #     return self.size / 500

    def human_created(self):
        return "%s-%s-%s" % (self.created.year, self.created.month, self.created.day)
