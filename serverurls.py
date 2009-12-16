from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'archcode.home.views.index'),
    (r'^challenge/', include('archcode.challenge.urls')),
    (r'^accounts/profile/$', 'archcode.home.views.profile'),
    (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
