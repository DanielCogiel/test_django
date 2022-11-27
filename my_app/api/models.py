from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    year = models.IntegerField()