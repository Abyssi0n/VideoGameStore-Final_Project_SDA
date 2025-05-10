from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from viewer.forms import GameModelForm
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


class GameCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = GameModelForm
    success_url = reverse_lazy('games')
    permission_required = 'viewer.add_game'

    def form_invalid(self, form):
        print("Formulář 'CreatorModelForm' není validní.")
        return super().form_invalid(form)


