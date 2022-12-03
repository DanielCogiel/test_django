from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import MovieSerializer, MovieMiniSerializer, TaskSerializer, UserSerializer, PreferenceSerializer, TagSerializer
from .models import Movie, Task, User, Event, Day, Tag, Room

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
            return Response({"message":"Invalid time."})
        
        new_event = Event()
        new_event.eventName = request.data["eventName"]
        new_event.day = day
        new_event.tag = tag
        new_event.time = time
        new_event.save()
        return Response({"message": "Succesfully added user."})
        
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = EventSerializer(queryset, many=True)
    #     return Response({"eventName" : serializer.data.name})

class TagRelatedEvents(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tags = request.user.tags.all()
        events = []
        for event in Event.objects.all():
            if event.tag in tags:
                events.append({"id": event.id, "day": event.day.name, 
                "time": event.time, "eventName": event.eventName, "tag": event.tag.title})
        return Response(events)

class UserRelatedTags(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tags = request.user.tags.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class UserRelatedPreferences(APIView):
    permission_classes = [permissions.IsAuthenticated]
        
    def get(self, request):
        preferences = request.user.preferences.all()
        serializer = PreferenceSerializer(preferences, many=True)
        return Response(serializer.data)

class MatchRoom(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_preferences = request.user.preferences.all()
        chosenRoomID = 1
        counter = 0
        maxCounter = 0
        for room in Room.objects.all():
            counter = 0
            for preference in room.preferences.all():
                if preference in user_preferences:
                    counter += 1
            if counter > maxCounter:
                chosenRoomID = room.id
                maxCounter = counter
        return Response({"id": Room.objects.filter(id=chosenRoomID).first().id})
        # return Response({"message": chosenRoomID})

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
       