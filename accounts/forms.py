from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email',
                  'password1', 'password2']

        labels = {
            'username': 'Uživatelské jméno',
            'email': 'E-mail',
        }