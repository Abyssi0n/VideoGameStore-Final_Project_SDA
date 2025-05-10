import profile

from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea, PasswordInput, DateField, NumberInput, ModelForm

from accounts.models import Profile, Comment


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

    date_of_birth = DateField(
        widget=NumberInput(attrs={'type': 'date'}),
        label="Date of Birth",
        required=True
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

        date_of_birth = self.cleaned_data.get('date_of_birth')
        biography = self.cleaned_data.get('biography')
        nickname = self.cleaned_data.get('nickname')
        profile = Profile(
            user=user,
            nickname=nickname,
            biography=biography,
            date_of_birth=date_of_birth,

        )
        if commit:
            profile.save()
        return user


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        labels = {
            'comment': 'Comment'
        }