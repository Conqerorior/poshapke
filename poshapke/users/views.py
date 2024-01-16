from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from basket.models import Basket
from common.mixins import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import EmailVerification

User = get_user_model()


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы !'
    title = 'Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Личный Кабинет'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = ' Подтверждение электронной почты'

    def get(self, request, *args, **kwargs):
        url_uuid = self.kwargs['url_uuid']
        user = User.objects.get(email=self.kwargs['email'])
        email_verification = EmailVerification.objects.filter(
            user=user,
            url_uuid=url_uuid
        )
        if (email_verification.exists() and
                user == request.user and
                email_verification.first().is_expired()):
            user.is_verified_email = True
            user.save()

            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
