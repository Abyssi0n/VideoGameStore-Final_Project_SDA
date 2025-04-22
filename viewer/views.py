from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from viewer.models import Genre, Game


class GenresListView(ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genres'


class GamesListView(ListView):
    template_name = 'games.html'
    model = Game
    context_object_name = 'games'
