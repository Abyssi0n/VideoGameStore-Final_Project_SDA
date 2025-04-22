from django.db import models
from django.db.models import Model, CharField, ManyToManyField, FloatField, DateTimeField, TextField


# Create your models here.
class Genre(Model):
    name = CharField(max_length=100, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return self.name
class Game(Model):
    name = CharField(max_length=100, null=False, blank=False, unique=True)
    genres = ManyToManyField(Genre, blank=True, related_name='games')
    price = FloatField(null=False, blank=False)
    # developers = ManyToManyField(DeveloperGroup, null=True, blank=True, related_name='games')
    # publishers = ManyToManyField(PublisherGroup, null=True, blank=True, related_name='games')
    release_date = DateTimeField(auto_now_add=True)
    description = TextField(null=True, blank=True)
    system_reqs = TextField(null=False, blank=False)
    updated = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Game(name={self.name})"

    def __str__(self):
        return self.name


