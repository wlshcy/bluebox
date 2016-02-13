#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import CreateFrtForm, UpdateFrtForm
from .models import Frt, Photo


def index(request):
    
    return response('fruits.html', {'frts': Frt.objects.order_by('-created')}, context_instance=RequestContext(request))


def show(request):
    id = request.GET.get('id')
    frt = Frt.objects(id=id)[0]

    return response('frt-detail.html',
                    {'id': frt.id, 'slide': frt.slide, 'name': frt.name, 'desc': frt.desc,
                     'size': frt.size, 'price': frt.price,
                     'mprice': frt.mprice, 'origin': frt.origin, 'photo': frt.photo},
                    context_instance=RequestContext(request))


def create(request):
    form = CreateFrtForm(request.POST, request.FILES)
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

        frt = Frt(slide=slide,
		  name=name,
                  photo=photo.url,
                  desc=desc,
                  size=size,
                  price=price,
                  mprice=mprice,
                  origin=origin)
        frt.save()
    else:
        print('表单验证失败')

    return HttpResponseRedirect('/fruits/')


def update(request):
    print(request.POST)
    form = UpdateFrtForm(request.POST, request.FILES)
    if form.is_valid():
        id = request.POST['id']
        frt = Frt.objects(id=id)[0]
        frt.slide = form.cleaned_data['slide']
        frt.name = form.cleaned_data['name']
        frt.desc = form.cleaned_data['desc']
        frt.size = form.cleaned_data['size']
        frt.price = form.cleaned_data['price']
        frt.mprice = form.cleaned_data['mprice']
        frt.origin = form.cleaned_data['origin']

	if len(request.FILES):
            photo = form.cleaned_data['photo']
            photo = Photo(photo)
            photo.save()
	    frt.photo = photo
        frt.save()
        
    return HttpResponseRedirect('/fruits/')

def delete(request):
    id = request.POST.get('id')
    frt = Frt.objects(id=id)[0]
    frt.delete()

    return HttpResponseRedirect('/fruits/')


