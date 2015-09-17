from django.conf.urls import patterns, url

from items import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'delete/$', views.delete, name='delete'),
)

