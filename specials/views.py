#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateSpecialForm, UpdateSpecialForm
from .models import Special, Photo


def index(request):
    
    return response('specials.html', {'specials': Special.objects.order_by('-created')}, context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    special = Special.objects(id=id)[0]

    return response('special.html',
                    {'id': special.id,'name': special.name, 'desc': special.desc,
                     'size': special.size, 'price': special.price,
                     'mprice': special.mprice, 'origin': special.origin, 'photo': special.photo},
                    context_instance=RequestContext(request))


def create(request):
    form = CreateSpecialForm(request.POST, request.FILES)
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

        special = Special(
		  name=name,
                  photo=photo.url,
                  desc=desc,
                  size=size,
                  price=price,
                  mprice=mprice,
                  origin=origin)
        special.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/specials/')


def update(request):
    form = UpdateSpecialForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        special = Special.objects(id=id)[0]
        special.name = form.cleaned_data['name']
        special.desc = form.cleaned_data['desc']
        special.size = form.cleaned_data['size']
        special.price = form.cleaned_data['price']
        special.mprice = form.cleaned_data['mprice']
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
    special = Special.objects(id=id)[0]
    special.delete()

    return HttpResponseRedirect('/specials/')


def new(request):
    
    return response('special-new.html', context_instance=RequestContext(request))

