from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

import items.urls
import specials.urls
import users.urls
import orders.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bluebox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/items/')),
    url(r'^items/', include(items.urls)),
    url(r'^specials/', include(specials.urls)),
    url(r'^users/', include(users.urls)),
    url(r'^orders/', include(orders.urls)),
)
