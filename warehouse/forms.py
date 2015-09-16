__author__ = 'nmg'

from django import forms


class AddItemForm(forms.Form):
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    desc = forms.CharField(required=False)
    size = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)
    mprice = forms.IntegerField(required=True)
    origin = forms.CharField(required=True)
    invent = forms.IntegerField(required=False)
