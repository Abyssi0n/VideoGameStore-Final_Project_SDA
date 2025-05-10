from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField, ManyToManyField, DateField, ForeignKey, \
    DateTimeField
from django.urls import reverse

from viewer.models import Game


# Create your models here.


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    nickname = TextField(max_length=32, default=user.name, blank=True)
    # TODO: image
    biography = TextField(max_length=250, blank=True)
    date_of_birth = DateField()
    owned_games = ManyToManyField(Game, blank=True, related_name='own_game')

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile(user={self.user})"

    def __str__(self):
        return self.user.username

    def age(self):
        if self.date_of_birth:
            end_date = date.today()
            return (end_date.year - self.date_of_birth.year -
                    ((end_date.month, end_date.day) < (self.date_of_birth.month, self.date_of_birth.day)))
        return None

    def get_absolute_url(self):
        return reverse('profile', args=(self.pk,))


class Comment(Model):
    profile = ForeignKey(Profile, on_delete=CASCADE, null=False, blank=False, related_name='profile')
    commenter = ForeignKey(Profile, on_delete=CASCADE, null=False, blank=False, related_name='commenter')
    comment = TextField(null=False, blank=False)
    created = DateTimeField(auto_now_add=True)
    edited = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __repr__(self):
        return (f"Comment(profile={self.profile}, "
                f"from={self.commenter}, "
                f"text={self.comment[:20]})")

    def __str__(self):
        return f"{self.commenter}: {self.profile} ({self.comment})"
