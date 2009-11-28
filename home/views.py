# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    title = "Welcome"
    message = "This is a message."
    return render_to_response('home/index.html', {
        'title':                title,
        'message':              message,
        })
