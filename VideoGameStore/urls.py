"""
URL configuration for VideoGameStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from VideoGameStore import settings
from accounts.views import ProfileDetailView, SubmittableLoginView, user_logout, SignUpView, profile_redirect, \
  ProfileBiographyUpdateView
from viewer.views import *

urlpatterns = [
  path('admin/', admin.site.urls, name='admin'),
  path('', home, name='home'),


  path('genres/', GenresListView.as_view(), name="genres"),
  path('genre/create/', GenreCreateView.as_view(), name="genre_create"),
  path('genre/<int:pk>/', GenreDetailView.as_view(), name="genre"),
  path('genre/<int:pk>/update/', GenreUpdateView.as_view(), name="genre_edit"),

  path('games/', GamesListView.as_view(), name="games"),
  path('game/create/', GameCreateView.as_view(), name='game_create'),
  path('game/<int:pk>/', game, name="game"),
  path('game/<int:pk>/update', GameUpdateView.as_view(), name="game_edit"),

  path('profile/', profile_redirect),
  path('profile/<int:pk>/update_bio', ProfileBiographyUpdateView.as_view(), name='profilebio_update'),
  path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),

  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
  path('accounts/logout/', user_logout, name='logout'),
  path('accounts/signup/', SignUpView.as_view(), name='signup'),

  path('buy/<int:pk>', buy, name="buy_game"),
  path('buy_confirm/<int:pk>', buy_confirm, name="buy_confirm"),

  path('publisher/<int:pk>/', PublisherDetailView.as_view(), name="publisher"),
  path('publisher/<int:pk>/update', PublisherUpdateView.as_view(), name="pub_edit"),
  path('publisher/create/', PublisherCreateView.as_view(), name="pub_create"),
  path('developer/<int:pk>/', DeveloperDetailView.as_view(), name="developer"),
  path('developer/<int:pk>/update', DeveloperUpdateView.as_view(), name="dev_edit"),
  path('developer/create/', DeveloperCreateView.as_view(), name="dev_create"),

  path('images/', ImageListView.as_view(), name='images'),
  path('image/<int:pk>/', ImageDetailView.as_view(), name='image'),
  path('image/create/', ImageCreateView.as_view(), name='img_add'),
  path('image/update/<int:pk>/', ImageUpdateView.as_view(), name='img_edit'),
  path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='img_del'),

  path('search/', search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
