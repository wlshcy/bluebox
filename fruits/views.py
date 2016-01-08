#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

from .forms import AddFrtForm
from .models import Frt, Photo


def index(request):
    if request.method == "POST":
        form = AddFrtForm(request.POST, request.FILES)
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

            frt = Frt(name=name,
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
    
    return response('fruits.html', {'frts': Frt.objects.order_by('-created')}, context_instance=RequestContext(request))
