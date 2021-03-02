from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Artist(models.Model):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=250, blank=True, null=True)
    birthday = models.DateField()
    genre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} Born on:{self.birthday} Genre:{self.genre}"


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, max_length=100, on_delete=models.CASCADE)
    album_year = models.IntegerField(blank=True, null=True)
    album_photo = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.album_year}{self.artist}"
