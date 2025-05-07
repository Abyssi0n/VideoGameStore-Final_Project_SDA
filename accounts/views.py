from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from accounts.forms import SignUpForm
from accounts.models import Profile
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class ProfileBiographyUpdateView(UpdateView):
    model = Profile
    fields = ["biography"]
    template_name = 'form.html'


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


def user_logout(request):
    logout(request)
    return redirect('home')


def profile_redirect(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return redirect('profile', user_id)
    else:
        return redirect('home')





