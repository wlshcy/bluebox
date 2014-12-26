from django.conf.urls import patterns,url

from warehouse import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
)
