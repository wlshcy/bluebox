from django.conf.urls import patterns,url

from fruits import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
