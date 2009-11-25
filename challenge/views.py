# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from archcode.challenge.models import Challenge
from datetime import datetime

def index(request):
    current_challenges = Challenge.objects.exclude(ends__lte=datetime.now).filter(starts__lte=datetime.now)
    past_challenges = Challenge.objects.filter(ends__lte=datetime.now)
    return render_to_response('index.html', {'current_challenges': current_challenges,'past_challenges': past_challenges})

def details(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render_to_response('details.html', {'challenge': challenge})
