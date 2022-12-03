from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
import rest_framework.authtoken.views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'events', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('events/', views.ListEvents.as_view()),
    path('events/tagRelated/', views.TagRelatedEvents().as_view()),
    path('rooms/matchRoom/', views.MatchRoom.as_view()),
    path('userRelatedTags/', views.UserRelatedTags.as_view()),
    path('userRelatedPreferences/', views.UserRelatedPreferences.as_view())
]

# rest_framework.authtoken.views.obtain_auth_token