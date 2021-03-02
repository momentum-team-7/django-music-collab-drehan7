from django.shortcuts import render, get_object_or_404
from .models import Album, Artist

# Create your views here.


def index(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def artist_info(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist_info.html', {'artist': artist})
