from django.conf.urls.defaults import *

urlpatterns = patterns('archcode.challenge.views',
    url(r'^$', 'index', {}, 'challenge-index'),
    url(r'(?P<challenge_id>\d+)/$', 'details', {}, 'challenge-details'),
    url(r'submit/solution/$', 'submit_solution', name='challenge-submit-solution'),
)
