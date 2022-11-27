from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MovieSerializer
from .models import Movie, User


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
