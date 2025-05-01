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
from django.urls import path

from accounts.views import ProfileDetailView
from viewer.views import *

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', home, name='home'),


  path('genres/', GenresListView.as_view(), name="genres"),
  path('games/', GamesListView.as_view(), name="games"),
  path('game/<int:pk>/', GameDetailView.as_view(), name="game"),


  path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),

]
