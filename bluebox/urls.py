from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

import sales.urls
import profit.urls
import settle.urls
import warehouse.urls
import notify.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bluebox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',RedirectView.as_view(url='/sales/')),
    url(r'^sales/',include(sales.urls)),
    url(r'^profit/',include(profit.urls)),
    url(r'^settle/',include(settle.urls)),
    url(r'^warehouse/',include(warehouse.urls)),
    url(r'^notify/',include(notify.urls)),
  
)
