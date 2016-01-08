from django.conf.urls import patterns,url

from vegetables import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^show$', views.show, name='show'),
    #url(r'^[a-z0-9]{24}$', views.show, name='show'),
    url(r'^create$', views.create, name='create'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^update$', views.update, name='update'),
)
