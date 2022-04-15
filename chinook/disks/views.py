from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Track

# Create your views here.

def albums(request):
    album_list = Album.objects.all
    output = ", " .join([album.title, album.artist])
    return HttpResponse(output)
