from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from archcode.challenge.models import Challenge, Solution
from archcode.challenge.forms import SolutionForm



def challenge_list(request):
    title = "Challenges"
    current_challenges = Challenge.objects.exclude(ends__lte=datetime.now).filter(starts__lte=datetime.now)
    past_challenges = Challenge.objects.filter(ends__lte=datetime.now)
    return render_to_response('challenge/challenge_list.html', {
        'title': title,
        'current_challenges': current_challenges,
        'past_challenges': past_challenges
        })

def challenge_details(request, challenge_id):
    title = "Challenge Details"
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render_to_response('challenge/challenge_details.html', {
        'title': title,
        'challenge': challenge })

def solution_list(request):
    title = 'Solutions'
    solutions = Solution.objects.all()
    return render_to_response('challenge/solution_list.html', {
        'title': title,
        'solutions': solutions,
        })

def solution_details(request, solution_id):
    title = "Solution Details"
    solution = get_object_or_404(Solution, pk=solution_id)
    return render_to_response('challenge/solution_details.html', {
        'title': title,
        'solution': solution })

@login_required
def solution_submit(request):
    title = 'Submit a Solution'
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            messages.success(request, 'Your solution has been successfully submitted.')
            return HttpResponseRedirect(reverse('challenge-solution-submit'))
    else:
        form = SolutionForm()
    return render_to_response('challenge/solution_submit.html', {
        'title': title,
        'form': form}, context_instance=RequestContext(request))

