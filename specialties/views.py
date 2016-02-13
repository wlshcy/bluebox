#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateSpeForm, UpdateSpeForm
from .models import Spe, Photo


def index(request):
    
    return response('specialties.html', {'spes': Spe.objects.order_by('-created')}, context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    spe = Spe.objects(id=id)[0]

    return response('spe-detail.html',
                    {'id': spe.id, 'slide': spe.slide, 'name': spe.name, 'desc': spe.desc,
                     'size': spe.size, 'price': spe.price,
                     'mprice': spe.mprice, 'origin': spe.origin, 'photo': spe.photo},
                    context_instance=RequestContext(request))


def create(request):
    form = CreateSpeForm(request.POST, request.FILES)
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

        spe = Spe(slide=slide,
		  name=name,
                  photo=photo.url,
                  desc=desc,
                  size=size,
                  price=price,
                  mprice=mprice,
                  origin=origin)
        spe.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/specialties/')


def update(request):
    print(request.POST)
    form = UpdateSpeForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        spe = Spe.objects(id=id)[0]
        spe.slide = form.cleaned_data['slide']
        spe.name = form.cleaned_data['name']
        spe.desc = form.cleaned_data['desc']
        spe.size = form.cleaned_data['size']
        spe.price = form.cleaned_data['price']
        spe.mprice = form.cleaned_data['mprice']
        spe.origin = form.cleaned_data['origin']

	if len(request.FILES):
            photo = form.cleaned_data['photo']
            photo = Photo(photo)
            photo.save()
	    spe.photo = photo
        spe.save()
        
    return HttpResponseRedirect('/specialties/')

def delete(request):
    id = request.POST.get('id')
    spe = Spe.objects(id=id)[0]
    spe.delete()

    return HttpResponseRedirect('/specialties/')


