from django.shortcuts import render
from django.shortcuts import render_to_response as response

# Create your views here.

def index(request):
    return response('orders/orders.html')

def unpay(request):
    return response('orders/unpay.html')

def delivering(request):
    return response('orders/delivering.html')

def finished(request):
    return response('orders/finished.html')
