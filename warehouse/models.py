# Create your models here.


from mongoengine import *

from bluebox.settings import DATABASE, IMAGE_UPLOAD_PATH, IMAGE_URL


from PIL import Image

import uuid
import os
import datetime

connect(host=DATABASE)


class Item(Document):
    name = StringField(required=True, max_length=30)
    photo = StringField(required=True)
    desc = StringField(required=True, max_length=15)
    size = FloatField()
    price = FloatField()
    mprice = FloatField()
    origin = StringField()
    invent = IntField()
    sales = FloatField(required=False, default=0)
    created = DateTimeField(default=datetime.datetime.now)


class Photo(object):
    def __init__(self, image):
        self.image = image
        self._name = uuid.uuid4().hex

    @property
    def name(self, extension='.png'):
        return self._name + extension

    @property
    def path(self):
        return os.path.join(IMAGE_UPLOAD_PATH, self.name)

    @property
    def url(self):
        return os.path.join(IMAGE_URL, self.name)

    def save(self, default_format="PNG"):
        img = Image.open(self.image)
        img.save(self.path, default_format)
