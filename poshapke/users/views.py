from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from basket.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Профиль',
        'form': form,
        'baskets': Basket.objects.all()
    }
    return render(request, 'users/profile.html', context=context)


def user_logout(request):
    logout(request=request)
    return HttpResponseRedirect(reverse('index'))
