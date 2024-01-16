from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from basket.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


User = get_user_model()


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Регистрация'
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object, ))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Личный Кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context
