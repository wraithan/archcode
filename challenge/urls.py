from django.conf.urls.defaults import *

urlpatterns = patterns('archcode.challenge.views',
    url(r'^$', 'challenge_list', name='challenge-list'),
    url(r'^(?P<challenge_id>\d+)/$', 'challenge_details',
        name='challenge-details'),

    url(r'solution/list/$', 'solution_list', name='challenge-solution-list'),
    url(r'solution/(?P<solution_id>\d+)/$', 'solution_details',
        name='challenge-solution-details'),
    url(r'solution/submit/$', 'solution_submit',
        name='challenge-solution-submit'),
)
