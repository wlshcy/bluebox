from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response as response


def index(request):
    return response('items.html')

def show(request):
    pass

def create(request):
    pass

def update(request):
    pass

def delete(request):
    pass

