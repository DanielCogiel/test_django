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

class Day(models.Model):
    name = models.CharField(max_length=9)

    def __str__(self):
        return self.name

class Event(models.Model):
    eventName = models.CharField(max_length=128)
    day = models.ForeignKey(Day, related_name="events", null=True, on_delete=models.CASCADE)
    time = models.TimeField()
    timestamp = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, related_name="events", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.eventName} on {self.day}, {self.time} with tag: {self.tag.title}"
    # day time name tag

class Room(models.Model):
    preferences = models.ManyToManyField(Preference, related_name="rooms")

class User(AbstractUser):
    tags = models.ManyToManyField(Tag, related_name="users")
    preferences = models.ManyToManyField(Preference, related_name="preferences")