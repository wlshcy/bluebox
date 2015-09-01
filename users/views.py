from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response as response

def index(request):
    return response('users.html')
