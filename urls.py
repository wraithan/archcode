from django.conf.urls.defaults import *
from django.contrib import admin
import os
admin.autodiscover()
relpath = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

urlpatterns = patterns('',
    (r'^$', 'archcode.home.views.index'),
    (r'^challenge/$', 'archcode.challenge.views.index'),
    (r'^challenge/(?P<challenge_id>\d+)/$', 'archcode.challenge.views.details'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': relpath('media/')}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

