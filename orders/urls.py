from django.conf.urls import patterns,url

from orders import views

urlpatterns = patterns('',
    url(r'^search$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^unpay$', views.unpay, name='unpay'),
    url(r'^delivering$', views.delivering, name='delivering'),
    url(r'^finished$', views.finished, name='finished'),
)
