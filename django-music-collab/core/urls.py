from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/<int:pk>/', views.artist_info, name='artist_info'),
    path('artists/', views.artists, name="artists"),
    path('albums', views.albums, name="albums"),
    path('album/<int:pk>/', views.album_info, name="album_info"),
    path('albums/add_album/', views.add_album, name='add_album'),
    path('artists/add_artist/', views.add_artist, name='add_artist'),
]
