from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

from django.shortcuts import render_to_response as response
from django.http import HttpResponseRedirect
from PIL import Image
from .forms import AddItemForm
from .models import Item
from bluebox.settings import IMAGE_UPLOAD_DIR, IMAGE_URL
import uuid

def index(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            size = form.cleaned_data['size']
            price = form.cleaned_data['price']
            mprice = form.cleaned_data['mprice']
            origin = form.cleaned_data['origin']
            invent = form.cleaned_data['invent']

            photo = form.cleaned_data['photo']
            img = Image.open(photo)
            file_name = "{}.png".format(uuid.uuid4().hex)
            path = "{}{}".format(IMAGE_UPLOAD_DIR, file_name)
            img.save(path, 'PNG')
            url = IMAGE_URL + file_name
            print(url)
            form.cleaned_data.update({'photo': url})

            item = Item(name=name,
                        photo=url,
                        desc=desc,
                        size=size,
                        price=price,
                        mprice=mprice,
                        origin=origin,
                        invent=invent)
            item.save()
        else:
            print('表单验证失败')
        return HttpResponseRedirect('/warehouse/')

    return response('warehouse.html', context_instance=RequestContext(request))