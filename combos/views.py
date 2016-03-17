#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateComboForm, UpdateComboForm
from .models import Combo, Photo


def index(request):
    
    return response('combos.html', {'combos': Combo.objects.order_by('-created')}, context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    combo = Combo.objects(id=id)[0]

    return response('combo-detail.html',
                    {'id': combo.id, 'slide': combo.slide, 'name': combo.name, 'num': combo.num,
                     'price': combo.price, 'weight': combo.weight,
                     'long': combo.long, 'freq': combo.freq, 'photo': combo.photo},
                    context_instance=RequestContext(request))


def create(request):
    form = CreateComboForm(request.POST, request.FILES)
    if form.is_valid():
        slide = form.cleaned_data['slide']
        name = form.cleaned_data['name']
        num = form.cleaned_data['num']
        price = form.cleaned_data['price']
        weight = form.cleaned_data['weight']
        long = form.cleaned_data['long']
        freq = form.cleaned_data['freq']

        photo = form.cleaned_data['photo']
        photo = Photo(photo)
        photo.save()

        combo = Combo(slide=slide,
		  name=name,
                  photo=photo.url,
                  num=num,
                  weight=weight,
                  price=price,
                  long=long,
                  freq=freq)
        combo.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/combos/')


def update(request):
    form = UpdateComboForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        combo = Combo.objects(id=id)[0]
        combo.slide = form.cleaned_data['slide']
        combo.name = form.cleaned_data['name']
        combo.num = form.cleaned_data['num']
        combo.price = form.cleaned_data['price']
        combo.weight  = form.cleaned_data['weight']
        combo.long = form.cleaned_data['long']
        combo.freq = form.cleaned_data['freq']

	if len(request.FILES):
            photo = form.cleaned_data['photo']
            photo = Photo(photo)
            photo.save()
	    combo.photo = photo
        combo.save()
    else:
        print('表单验证失败')
        
    return HttpResponseRedirect('/combos/')

def delete(request):
    id = request.POST.get('id')
    combo = Combo.objects(id=id)[0]
    combo.delete()

    return HttpResponseRedirect('/combos/')


