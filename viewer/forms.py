from django.forms import ModelForm

from viewer.models import Game, Genre


class GameModelForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class GenreModelForm(ModelForm):

    class Meta:
        model = Genre
        fields = '__all__'
