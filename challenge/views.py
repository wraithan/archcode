# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from archcode.challenge.models import Status, Challenge

def index(request):
    try:
        currentChallenges = Challenge.objects.filter(status=Status.objects.get(name="In Progress"))
    except Challenge.DoesNotExist:
        currentChallenges = None
    return render_to_response('index.html', {'challenges': currentChallenges})

def details(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render_to_response('details.html', {'challenge': challenge})
