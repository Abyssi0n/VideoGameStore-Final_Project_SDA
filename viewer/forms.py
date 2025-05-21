from django.forms import ModelForm

from viewer.models import Game, Genre, Publisher, Developer, Image


class GameModelForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class GenreModelForm(ModelForm):

    class Meta:
        model = Genre
        fields = '__all__'

class PublisherModelForm(ModelForm):

    class Meta:
        model = Publisher
        fields = '__all__'

class PublisherModelForm(ModelForm):

    class Meta:
        model = Developer
        fields = '__all__'


class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'description']
