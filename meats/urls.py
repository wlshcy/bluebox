from django.conf.urls import patterns,url

from meats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
