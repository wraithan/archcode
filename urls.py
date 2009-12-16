from django.conf.urls.defaults import *
from django.contrib import admin
import os
admin.autodiscover()
relpath = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

urlpatterns = patterns('',
    (r'^$', 'archcode.home.views.index'),
    (r'^challenge/', include('archcode.challenge.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': relpath('media/')}),
    (r'^accounts/profile/$', 'archcode.home.views.profile'),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^paste/', include('dpaste.urls')),
)
