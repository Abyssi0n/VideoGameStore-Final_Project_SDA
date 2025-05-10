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

from django.contrib import admin
from django.urls import path, include

from accounts.views import ProfileDetailView, SubmittableLoginView, user_logout, SignUpView, profile_redirect, \
  ProfileBiographyUpdateView
from viewer.views import *

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', home, name='home'),


  path('genres/', GenresListView.as_view(), name="genres"),
  path('genre/<int:pk>/', GenreDetailView.as_view(), name="genre"),

  path('games/', GamesListView.as_view(), name="games"),
  path('game/create/', GameCreateView.as_view(), name='game_create'),
  path('game/<int:pk>/', GameDetailView.as_view(), name="game"),

  path('profile/', profile_redirect),
  path('profile/<int:pk>/update_bio', ProfileBiographyUpdateView.as_view(), name='profilebio_update'),
  path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),

  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
  path('accounts/logout/', user_logout, name='logout'),
  path('accounts/signup/', SignUpView.as_view(), name='signup'),


]
