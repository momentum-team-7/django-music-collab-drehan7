from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm

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


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})


def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()
    return render(request, 'add_artist.html', {'form': form})


def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'edit_artist.html', {'form': form, 'artist': artist})


def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/artists/')


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/albums/')

    else:
        form = AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'form': form, 'album': album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return HttpResponseRedirect('/albums/')
