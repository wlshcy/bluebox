
from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'items.html', {'items': Item.objects})


def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        item = Item.objects(id=id)[0]
        item.delete()

    return HttpResponseRedirect('/items/')
