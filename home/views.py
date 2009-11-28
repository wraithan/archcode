# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    title = "Welcome"

    messages = [ "This is a test message.", "This is another test message." ]
    return render_to_response('home/index.html', {
        'title':                title,
        'messages':              messages,
        })
