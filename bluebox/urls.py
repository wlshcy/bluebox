from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

import warehouse.urls
import items.urls
import users.urls
import orders.urls

import notifications.urls
import vegetables.urls
import fruits.urls
import meats.urls
import specialties.urls
import combos.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bluebox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^warehouse/', include(warehouse.urls)),
    #url(r'^items/', include(items.urls)),
    #url(r'^users/', include(users.urls)),
    #url(r'^orders/', include(orders.urls)),

    url(r'^$', RedirectView.as_view(url='/notifications/')),
    url(r'^$', RedirectView.as_view(url='/notifications/')),
    url(r'^notifications/', include(notifications.urls)),
    url(r'^vegetables/', include(vegetables.urls)),
    url(r'^fruits/', include(fruits.urls)),
    url(r'^orders/', include(orders.urls)),
    url(r'^users/', include(users.urls)),
    #url(r'^meat/', include(meats.urls)),
    url(r'^specialties/', include(specialties.urls)),
    url(r'^combos/', include(combos.urls)),

  
)
