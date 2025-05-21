from django.db import models
from django.db.models import Model, CharField, ManyToManyField, FloatField, DateTimeField, TextField, DateField, \
    URLField, SET_NULL, ForeignKey, ImageField


# Create your models here.
class Genre(Model):
    name = CharField(max_length=100, null=False, blank=False, unique=True)
    description = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return self.name

class Developer(Model):
    name = CharField(max_length=100, null=False, blank=False, unique=True)
    website = URLField(null=False, blank=True)
    about = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Developer(name={self.name})"

    def __str__(self):
        return self.name


class Publisher(Model):
    name = CharField(max_length=100, null=False, blank=False, unique=True)
    website = URLField(null=False, blank=True)
    about = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Publisher(name={self.name})"

    def __str__(self):
        return self.name



class Game(Model):
    name = CharField(max_length=100, null=False, blank=False, unique=True)
    genres = ManyToManyField(Genre, blank=True, related_name='games')
    price = FloatField(null=False, blank=False)
    developers = ManyToManyField(Developer, blank=True, related_name='games')
    publishers = ManyToManyField(Publisher, blank=True, related_name='games')
    release_date = DateField()
    description = TextField(null=True, blank=True)
    system_reqs = TextField(null=False, blank=False)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Game(name={self.name})"

    def __str__(self):
        return self.name




class Image(Model):
    image = ImageField(upload_to='images/', default=None, null=False, blank=False)
    game = ForeignKey(Game, on_delete=SET_NULL, null=True, blank=True, related_name='image')
    description = TextField(null=True, blank=True)

    def __repr__(self):
        return f"Description(description={self.description})"

    def __str__(self):
        return self.description[:25]
