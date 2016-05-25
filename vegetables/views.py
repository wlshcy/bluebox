#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateVegForm, UpdateVegForm
from .models import Veg, Photo


def index(request):
    
    return response('vegetables.html', {'vegs': Veg.objects.order_by('-created')}, context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    veg = Veg.objects(id=id)[0]

    return response('veg-detail.html',
                    {'id': veg.id, 'slide': veg.slide, 'name': veg.name, 'desc': veg.desc,
                     'size': veg.size, 'price': veg.price,
                     'mprice': veg.mprice, 'origin': veg.origin, 'photo': veg.photo},
                    context_instance=RequestContext(request))


def create(request):
    form = CreateVegForm(request.POST, request.FILES)
    if form.is_valid():
        slide = form.cleaned_data['slide']
        name = form.cleaned_data['name']
        desc = form.cleaned_data['desc']
        size = form.cleaned_data['size']
        price = form.cleaned_data['price']
        mprice = form.cleaned_data['mprice']
        origin = form.cleaned_data['origin']

        photo = form.cleaned_data['photo']
        photo = Photo(photo)
        photo.save()

        veg = Veg(slide=slide,
		  name=name,
                  photo=photo.url,
                  desc=desc,
                  size=size,
                  price=price,
                  mprice=mprice,
                  origin=origin)
        veg.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/vegetables/')


def update(request):
    print(request.POST)
    form = UpdateVegForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        veg = Veg.objects(id=id)[0]
        veg.slide = form.cleaned_data['slide']
        veg.name = form.cleaned_data['name']
        veg.desc = form.cleaned_data['desc']
        veg.size = form.cleaned_data['size']
        veg.price = form.cleaned_data['price']
        veg.mprice = form.cleaned_data['mprice']
        veg.origin = form.cleaned_data['origin']

        if len(request.FILES):
            photo = form.cleaned_data['photo']
            photo = Photo(photo)
            photo.save()
            veg.photo = photo.url
        veg.save()
        
    return HttpResponseRedirect('/vegetables/')

def delete(request):
    id = request.POST.get('id')
    veg = Veg.objects(id=id)[0]
    veg.delete()

    return HttpResponseRedirect('/vegetables/')


