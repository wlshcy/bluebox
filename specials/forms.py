
from django import forms


class CreateOnSaleForm(forms.Form):
    name = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    desc = forms.CharField(required=True)
    size = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    sprice = forms.FloatField(required=True)
    origin = forms.CharField(required=True)


class UpdateOnSaleForm(forms.Form):
    name = forms.CharField(required=True)
    image = forms.ImageField(required=False)
    desc = forms.CharField(required=True)
    size = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    mprice = forms.FloatField(required=True)
    origin = forms.CharField(required=True)
