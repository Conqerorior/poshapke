from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (UserLoginView,
                         UserRegistrationView,
                         UserProfileView,
                         EmailVerificationView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<str:username>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verification/<str:email>/<uuid:url_uuid>/', EmailVerificationView.as_view(), name='email_verification'),
]
