from django.forms import ModelForm

from viewer.models import Game


class GameModelForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
