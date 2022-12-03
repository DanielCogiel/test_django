from .models import Movie, Task, User, Tag, Preference, Day, Event
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year']

class MovieMiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Movie
        fields = ['id', 'title', 'tasks']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'timestamp']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class PreferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Preference
        fields = ['id', 'title']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    preferences = PreferenceSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'tags', 'preferences']

class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'name']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    day = DaySerializer()
    tag = TagSerializer()
    class Meta:
        model = Event
        fields = ['id', 'day', 'time', 'timestamp', 'tag']

