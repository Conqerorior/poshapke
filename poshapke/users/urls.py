from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import login_user, UserRegistrationView, UserProfileView, user_logout

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<str:username>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', user_logout, name='logout'),
]
