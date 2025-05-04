from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from accounts.forms import SignUpForm
from accounts.models import Profile


# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def profile_redirect(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return redirect(f'/profile/{user_id}')
    else:
        return redirect('home')



