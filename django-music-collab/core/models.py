from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Artist(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    genre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} Born on:{self.birthday} Genre:{self.genre}"


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, max_length=100, on_delete=models.CASCADE)
    song_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.song_year}{self.artist}"
