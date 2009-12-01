from django.conf.urls.defaults import *
from django.contrib import admin
import os
admin.autodiscover()
relpath = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

urlpatterns = patterns('',
    (r'^$', 'archcode.home.views.index'),
    (r'^challenge/', include('archcode.challenge.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': relpath('media/') }),
    (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

