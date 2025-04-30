from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField, ManyToManyField

from viewer.models import Game


# Create your models here.


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    nickname = TextField(max_length=32, default=user.name, blank=True)
    # TODO: image
    biography = TextField(max_length=250, blank=True)
    owned_games = ManyToManyField(Game, blank=True, related_name='own_game')
    # TODO: publisher group
    # TODO: developer group

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile(user={self.user})"

    def __str__(self):
        return self.user.username
