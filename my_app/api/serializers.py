from .models import Movie, Task
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year']

class MovieMiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Movie
        fields = ['id', 'title']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'timestamp']

