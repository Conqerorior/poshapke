from django.urls import path

from users.views import login_user, registration, profile, user_logout

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
]
