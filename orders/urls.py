from django.conf.urls import patterns,url

from orders import views

urlpatterns = patterns('',
    url(r'^search$', views.index, name='index'),
    url(r'^all$', views.index, name='index'),
    url(r'^unpay$', views.index, name='index'),
    url(r'^delivering$', views.index, name='index'),
    url(r'^finished$', views.index, name='index'),
)
