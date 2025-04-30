from django.shortcuts import render
from django.views.generic import DetailView

from accounts.models import Profile


# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

