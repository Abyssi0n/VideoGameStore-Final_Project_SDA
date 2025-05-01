from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from viewer.models import Genre, Game


def home(request):
    return render(request, 'home.html')


class GenresListView(ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genres'


class GamesListView(ListView):
    template_name = 'games.html'
    model = Game
    context_object_name = 'games'


class GenreDetailView(DetailView):
    template_name = 'genre.html'
    model = Genre
    context_object_name = 'genre'


class GameDetailView(DetailView):
    template_name = 'game.html'
    model = Game
    context_object_name = 'game'


