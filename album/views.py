from django.shortcuts import render_to_response, get_object_or_404
from album.models import Page

def index(request):
    return render_to_response('index.html', {
        'pages': Page.objects.all()
    })
