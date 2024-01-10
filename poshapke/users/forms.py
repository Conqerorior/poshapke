from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите имя пользователя'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите пароль'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')
