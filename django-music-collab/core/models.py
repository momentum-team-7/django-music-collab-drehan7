from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    song_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.artist} {str(self.song_year)}"
