# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    title = "Welcome"

    return render_to_response('home/index.html', {
        'title':                title,
        })
