#!/usr/bin/python
# -*- coding: utf8 -*-

# Create your views here.

from django.shortcuts import render


def index(request):

    return render(request, 'summaries/summaries.html')