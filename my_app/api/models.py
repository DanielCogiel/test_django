from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    year = models.IntegerField()


class Task(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)
    film = models.ForeignKey(Movie, related_name="tasks", on_delete=models.CASCADE, null=True)