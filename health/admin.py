from django.contrib import admin
from .models import Album, Song, HealthData


admin.site.register(HealthData)
admin.site.register(Album)
admin.site.register(Song)
