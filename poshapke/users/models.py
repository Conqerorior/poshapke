from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(
        verbose_name='Изображение пользователя',
        upload_to='users_image',
        help_text='Загрузите Изображение'
    )
