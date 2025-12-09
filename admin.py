from django.contrib import admin
from .models import Movie, Country, Genre, Language

admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Language)
