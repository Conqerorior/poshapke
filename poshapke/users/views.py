from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginForm


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
    return render(request, 'users/register.html')
