from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Preference(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class User(AbstractUser):
    tags = models.ManyToManyField(Tag, related_name="users")
    preferences = models.ManyToManyField(Preference, related_name="preferences")

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    year = models.IntegerField()

class Task(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)
    film = models.ForeignKey(Movie, related_name="tasks", on_delete=models.CASCADE, null=True)

