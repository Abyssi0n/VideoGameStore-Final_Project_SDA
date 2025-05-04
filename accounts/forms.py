import profile

from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea, PasswordInput


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'nickname', 'biography', 'email',
                  'password1', 'password2']

        labels = {
            'biography': 'Bio',
            'email': 'E-mail',

        }

    nickname = CharField(
        label='Nickname',
        required=False
    )

    biography = CharField(
        widget=Textarea,
        label='Bio',
        required=False
    )

    password1 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password'
    )

    password2 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Password again'}),
        label='Password again'
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)



        if commit:
            profile.save()
        return user
