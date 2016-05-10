
from django import forms


class CreateFrtForm(forms.Form):
    slide = forms.CharField(required=True)
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    desc = forms.CharField(required=True)
    size = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    mprice = forms.FloatField(required=True)
    origin = forms.CharField(required=True)


class UpdateFrtForm(forms.Form):
    slide = forms.CharField(required=True)
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=False)
    desc = forms.CharField(required=True)
    size = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    mprice = forms.FloatField(required=True)
    origin = forms.CharField(required=True)