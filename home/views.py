# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    title = "Welcome"

    return render_to_response('home/index.html', {
        'title':                title,
        })
