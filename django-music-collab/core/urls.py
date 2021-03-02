from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/<int:pk>/', views.artist_info, name='artist_info'),
]
