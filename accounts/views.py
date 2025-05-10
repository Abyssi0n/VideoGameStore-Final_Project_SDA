from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from accounts.forms import SignUpForm, CommentModelForm
from accounts.models import Profile, Comment
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


class CommentDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Comment
    success_url = reverse_lazy('profile')

# def comment(request, pk):
#     if Profile.objects.filter(id=pk).exists():
#         profilepage_ = Profile.objects.get(id=pk)
#         profile_ = None
#         if request.user.is_authenticated:
#             profile_ = Profile.objects.get(user=request.user)
#         if request.method == 'POST':
#             comment = request.POST.get('comment')
#
#             # pokud již uživatel tento film hodnotil, tak upravíme původní review
#             if Comment.objects.filter(profile=profilepage_, commenter=Profile.objects.get(user=request.user)).exists():
#                 user_comment = Comment.objects.get(profile=profilepage_, reviewer=profile_)
#                 user_comment.rating = rating
#                 user_comment.comment = comment
#                 user_comment.save()
#             else:
#                 Comment.objects.create(
#                     profile=profilepage_,
#                     reviewer=profile_,
#                     comment=comment
#                 )
#
#         context = {'profile': profilepage_,
#                    'comment_form': CommentModelForm,
#                    'commenter': profile_}
#         return render(request, 'movie.html', context)
#     return redirect('movies')
