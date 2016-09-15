#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateOnSaleForm, UpdateOnSaleForm
from .models import OnSale, Photo


def index(request):
    
    return response('items/specials.html', {'specials': OnSale.objects.order_by('-created')}, context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    special = OnSale.objects(id=id)[0]

    return response('items/special.html',
                    {'id': special.id,'name': special.name, 'desc': special.desc,
                     'size': special.size, 'price': special.price,
                     'sprice': special.sprice, 'origin': special.origin, 'photo': special.photo},
                    context_instance=RequestContext(request))

def new(request):
    
    return response('items/special-new.html', context_instance=RequestContext(request))

def create(request):
    form = CreateOnSaleForm(request.POST, request.FILES)
    if form.is_valid():
        name = form.cleaned_data['name']
        desc = form.cleaned_data['desc']
        size = form.cleaned_data['size']
        price = form.cleaned_data['price']
        sprice = form.cleaned_data['sprice']
        origin = form.cleaned_data['origin']

        photo = form.cleaned_data['photo']
        photo = Photo(photo)
        photo.save()

        special = OnSale(
		          name=name,
                  photo=photo.url,
                  desc=desc,
                  size=size,
                  price=price,
                  sprice=sprice,
                  origin=origin)
        special.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/specials/')


def update(request):
    form = UpdateOnSaleForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        special = OnSale.objects(id=id)[0]
        special.name = form.cleaned_data['name']
        special.desc = form.cleaned_data['desc']
        special.size = form.cleaned_data['size']
        special.price = form.cleaned_data['price']
        special.sprice = form.cleaned_data['sprice']
        special.origin = form.cleaned_data['origin']

	if len(request.FILES):
            photo = form.cleaned_data['photo']
            photo = Photo(photo)
            photo.save()
	    special.photo = photo.url
        special.save()
        
    return HttpResponseRedirect('/specials/')

def delete(request):
    id = request.POST.get('id')
    special = OnSale.objects(id=id)[0]
    special.delete()

    return HttpResponseRedirect('/specials/')


def new(request):
    
    return response('items/special-new.html', context_instance=RequestContext(request))

