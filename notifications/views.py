#!/usr/bin/python
# -*- coding: utf8 -*-

from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect

def index(request):
    
    return response('notifications.html')
