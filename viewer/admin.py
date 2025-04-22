from django.contrib import admin
from django.urls import path

# Register your models here.
from viewer.models import Genre, Game

admin.site.register(Genre)
admin.site.register(Game)

