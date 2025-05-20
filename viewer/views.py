from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Count

from accounts.models import Profile
from viewer.forms import GameModelForm, GenreModelForm, PublisherModelForm, DeveloperModelForm, ImageModelForm
from viewer.models import Genre, Game, Publisher, Developer, Image


def home(request):
    newgames_ = Game.objects.order_by("-pk")[:5]
    context = {"newgames": newgames_,
               }
    return render(request, 'home.html', context)


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


def game(request, pk):
    game_ = Game.objects.get(id=pk)
    profile_ = None
    try:
        image_ = Image.objects.get(game=game_)
    except:
        image_ = None
    if request.user.is_authenticated:
        profile_ = Profile.objects.get(user=request.user)
    context = {'game': game_,
               'profile': profile_,
               }
    if image_:
        context.update({'image': image_})
    return render(request, 'game.html', context)



class GameCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = GameModelForm
    success_url = "games/{id}"
    permission_required = 'viewer.add_game'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    success_url = "/genre/{id}"
    # success_url = reverse_lazy('genres')
    permission_required = 'viewer.add_genre'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    model = Genre
    success_url = "/genre/{id}"
    permission_required = 'viewer.edit_genre'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)

class GameUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = GameModelForm
    model = Game
    success_url = "/game/{id}"
    permission_required = 'viewer.edit_game'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


@login_required
def buy(request, pk):
    buying_game = Game.objects.get(id=pk)
    context = {'game': buying_game}
    return render(request, 'buy.html', context)

@login_required
def buy_confirm(request, pk):
    profile_ = Profile.objects.get(user=request.user)
    game_ = Game.objects.get(id=pk)

    profile_.owned_games.add(game_)

    return redirect('game', pk)


class PublisherDetailView(DetailView):
    template_name = 'publisher.html'
    model = Publisher
    context_object_name = 'publisher'


class DeveloperDetailView(DetailView):
    template_name = 'developer.html'
    model = Developer
    context_object_name = 'developer'

# def dev(request, pk):
#     dev_ = Developer.objects.get(id=pk)
#     games_ = Game.objects.get(developers=pk)
#     context = {'developer': dev_,
#                'games': games_}
#     return render(request, "developer.html", context)


class PublisherCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = PublisherModelForm
    success_url = "publisher/{id}/"
    permission_required = 'viewer.add_pub'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class DeveloperCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = DeveloperModelForm
    success_url = "developer/{id}/"
    permission_required = 'viewer.add_dev'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class PublisherUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = PublisherModelForm
    model = Publisher
    success_url = "/publisher/{id}"
    permission_required = 'viewer.edit_pub'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class DeveloperUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = DeveloperModelForm
    model = Developer
    success_url = "/developer/{id}"
    permission_required = 'viewer.edit_dev'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)

def search(request):
    if request.method == 'POST':
        search_string = request.POST.get('search').strip()
        if search_string:
            games = (Game.objects.filter(name__contains=search_string).distinct() |
                     Game.objects.filter(genres__name__contains=search_string).distinct() |
                     Game.objects.filter(description__contains=search_string).distinct())

            publisher = (Publisher.objects.filter(name__contains=search_string).distinct() |
                         Publisher.objects.filter(about__contains=search_string).distinct())

            developer = (Developer.objects.filter(name__contains=search_string).distinct() |
                         Developer.objects.filter(about__contains=search_string).distinct())

            context = {'search': search_string,
                       'games': games,
                       'publisher': publisher,
                       'developer': developer,}
            return render(request, 'search.html', context)
    return render(request, 'home.html')


class ImageListView(ListView):
    template_name = 'images.html'
    model = Image
    context_object_name = 'images'



class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'


class ImageCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_img'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('images')
    model = Image
    permission_required = 'viewer.edit_img'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Image
    success_url = reverse_lazy('images')
    permission_required = 'viewer.del_img'
