from django.shortcuts import render, get_object_or_404
from .models import Album, Artist

# Create your views here.


def index(request):
    albums = Album.objects.all().order_by('artist', 'pk')
    return render(request, 'index.html', {'albums': albums})


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})


def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})


def artist_info(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist_info.html', {'artist': artist})


def album_info(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_info.html', {'album': album})
