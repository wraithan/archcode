from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    title = "Welcome"

    return render_to_response('home/index.html', {
        'title': title,
        }, context_instance=RequestContext(request))


@login_required
def profile(request):
    title = "Profile"

    return render_to_response('home/profile.html', {
        'title': title,
        }, context_instance=RequestContext(request))
