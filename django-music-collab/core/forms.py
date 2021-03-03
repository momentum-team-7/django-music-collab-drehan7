from django import forms
from .models import Album, Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'album_year', 'album_photo']


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'picture', 'birthday', 'genre']
