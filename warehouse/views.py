from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

from django.shortcuts import render_to_response as response


def index(request):
    if request.method == "GET":
        return response('warehouse.html', context_instance=RequestContext(request))
    if request.method == "POST":
        print(request)

def create(request):
    print(request)
    pass