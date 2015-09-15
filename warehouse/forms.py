__author__ = 'nmg'

from django import forms


class ItemForm(forms.Form):
    name = forms.CharField()
    img = forms.ImageField()
    desc = forms.CharField()
    size = forms.IntegerField()
    price = forms.IntegerField()
    mprice = forms.IntegerField()
    origin = forms.CharField()
    invent = forms.IntegerField()
