# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from archcode.challenge.models import Challenge
from datetime import datetime

def index(request):
    title = "Challenges"
    current_challenges = Challenge.objects.exclude(ends__lte=datetime.now).filter(starts__lte=datetime.now)
    past_challenges = Challenge.objects.filter(ends__lte=datetime.now)
    return render_to_response('challenge/index.html', {
        'title':                title,
        'current_challenges':   current_challenges,
        'past_challenges':      past_challenges
        })

def details(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render_to_response('challenge/details.html', {'challenge': challenge})
