from django.conf.urls.defaults import *

urlpatterns = patterns('archcode.challenge.views',
    (r'$', 'index', {}, 'challenge-index'),
    (r'(?P<challenge_id>\d+)/$', 'details', {}, 'challenge-details'),
)
