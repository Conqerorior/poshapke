from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from users.tasks import send_verification_email

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите имя пользователя',
            }
        ),
        label='Имя пользователя',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите пароль',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')
        verbose_name_plural = 'Логин'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}
        ),
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите фамилию',
            }
        ),
    )
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите имя пользователя',
            }
        ),
    )
    email = forms.CharField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите адрес эл. почты',
            }
        ),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите пароль',
            }
        ),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Подтвердите пароль',
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
        verbose_name_plural = 'Регистрация'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже существует')
        return email

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        send_verification_email.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'custom-file-input'}),
        required=False,
    )
    username = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control py-4', 'readonly': True}
        ),
    )
    email = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control py-4', 'readonly': True}
        ),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
        verbose_name_plural = 'Профиль'
