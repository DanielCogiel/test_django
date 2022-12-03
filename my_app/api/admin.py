from django.contrib import admin
from .models import User, Tag, Preference, Day, Event, Room

# Register your models here.

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Preference)
admin.site.register(Day)
admin.site.register(Event)
admin.site.register(Room)