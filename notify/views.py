from django.shortcuts import render
from django.shortcuts import render_to_response as response

# Create your views here.

def index(request):
    return response('notify.html')     
