
from django import forms


class CreateSpecialForm(forms.Form):
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    desc = forms.CharField(required=True)
    size = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    mprice = forms.FloatField(required=True)
    origin = forms.CharField(required=True)


class UpdateSpecialForm(forms.Form):
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=False)
    desc = forms.CharField(required=True)
    size = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    mprice = forms.FloatField(required=True)
    origin = forms.CharField(required=True)
