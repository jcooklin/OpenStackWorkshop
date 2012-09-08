from django.conf.urls import patterns, include, url
from registerapp.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ittlcsite.views.home', name='home'),
    # url(r'^ittlcsite/', include('ittlcsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('registerapp',
    (r'^register/(?P<server>[-.\w]+)/(?P<login>[-\w]+)/$', register),
    (r'^$', get_login),
    (r'^login/list/$', list_logins),
)



