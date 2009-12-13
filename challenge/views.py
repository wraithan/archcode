# Create your views here.
from archcode.challenge.models import Challenge
from archcode.challenge.forms import SolutionForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

title = "Challenges"

def index(request):
    current_challenges = Challenge.objects.exclude(ends__lte=datetime.now).filter(starts__lte=datetime.now)
    past_challenges = Challenge.objects.filter(ends__lte=datetime.now)
    return render_to_response('challenge/index.html', {
        'title':                title,
        'current_challenges':   current_challenges,
        'past_challenges':      past_challenges
        })

def details(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render_to_response('challenge/details.html', {
        'title': title,
        'challenge': challenge })

@login_required
def submit_solution(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user# User.objects.filter(id=request.user.id).objects
            object.save()
            return HttpResponseRedirect('/challenge/submit/solution/')
    else:
        form = SolutionForm()
    return render_to_response('challenge/submit_solution.html', {'form':form})
