#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateItemForm, UpdateItemForm
from .models import Item, Photo


def index(request):
    return response('items/items.html', {'items': Item.objects.order_by('-created')},
                    context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    item = Item.objects(id=id)[0]

    return response('items/item.html',
                    {'id': item.id,
                     'name': item.name,
                     'desc': item.desc,
                     'size': item.size,
                     'price': item.price,
                     'mprice': item.mprice,
                     'origin': item.origin,
                     'photo': item.photo},
                    context_instance=RequestContext(request))


def create(request):
    form = CreateItemForm(request.POST, request.FILES)
    if form.is_valid():
        name = form.cleaned_data['name']
        desc = form.cleaned_data['desc']
        size = form.cleaned_data['size']
        price = form.cleaned_data['price']
        mprice = form.cleaned_data['mprice']
        origin = form.cleaned_data['origin']

        photo = form.cleaned_data['photo']
        photo = Photo(photo)
        photo.save()

        item = Item(
                name=name,
                photo=photo.url,
                desc=desc,
                size=size,
                price=price,
                mprice=mprice,
                origin=origin)
        item.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/items/')


def new(request):
    return response('items/item-new.html', context_instance=RequestContext(request))


def update(request):
    form = UpdateItemForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        item = Item.objects(id=id)[0]
        item.name = form.cleaned_data['name']
        item.desc = form.cleaned_data['desc']
        item.size = form.cleaned_data['size']
        item.price = form.cleaned_data['price']
        item.mprice = form.cleaned_data['mprice']
        item.origin = form.cleaned_data['origin']

    if len(request.FILES):
        photo = form.cleaned_data['photo']
        photo = Photo(photo)
        photo.save()
        item.photo = photo.url
        item.save()
    return HttpResponseRedirect('/items/')


def delete(request):
    _id = request.POST.get('id')
    item = Item.objects(id=_id)[0]
    item.delete()

    return HttpResponseRedirect('/items/')
