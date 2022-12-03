from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import MovieSerializer, MovieMiniSerializer, TaskSerializer, UserSerializer, EventSerializer
from .models import Movie, Task, User, Event, Day, Tag

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.order_by('day', 'time')
#     serializer_class = EventSerializer
#     permission_classes = [permissions.IsAuthenticated]

class ListEvents(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        events = [{"id": event.id, "day": event.day.name, "time": event.time, "eventName": event.eventName, "tag": event.tag.title} for event in Event.objects.order_by('day', 'time')]
        return Response(events)

    def post(self, request):
        day = Day.objects.filter(name=request.data["day"]).first()
        if day == None:
            return Response({"message": "Invalid day."})
        tag = Tag.objects.filter(title=request.data["tag"]).first()
        if tag == None:
            return Response({"message": "Invalid tag."})
        time = request.data["time"]
        if time == "":
            return Response({"Invalid time."})
        new_event = Event()
        new_event.eventName = request.data["eventName"]
        new_event.day = day
        new_event.tag = tag
        new_event.time = time
        new_event.save()
        return Response({"message": "Successfully added user."})
        
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = EventSerializer(queryset, many=True)
    #     return Response({"eventName" : serializer.data.name})



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })
       