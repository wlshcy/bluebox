
from django import forms


class CreateComboForm(forms.Form):
    slide = forms.CharField(required=True)
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    num = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    long = forms.FloatField(required=True)
    freq = forms.FloatField(required=True)


class UpdateComboForm(forms.Form):
    slide = forms.CharField(required=True)
    name = forms.CharField(required=True)
    photo = forms.ImageField(required=False)
    num = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)
    price = forms.FloatField(required=True)
    long = forms.FloatField(required=True)
    freq = forms.FloatField(required=True)
