from __future__ import unicode_literals

from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    model = Movie

    fieldsets = [('Movie Information', {'fields': ['name','post','year','movieId',]})]


admin.site.register(Movie, MovieAdmin)