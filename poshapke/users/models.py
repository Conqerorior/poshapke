from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Users(AbstractUser):
    image = models.ImageField(
        verbose_name='Изображение пользователя',
        upload_to='users_image',
        help_text='Загрузите Изображение'
    )
    is_verified_email = models.BooleanField(
        default=False,
        verbose_name='Подтверждение Почты'
    )


class EmailVerification(models.Model):
    url_uuid = models.UUIDField(
        unique=True,
        verbose_name='Уникальная ссылка'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время Создания'
    )
    expiration = models.DateTimeField(
        verbose_name='Истечение срока действия'
    )
    user = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        verbose_name='Новый Пользователь'
    )

    class Meta:
        verbose_name = 'Подтверждение Почты'
        verbose_name_plural = 'Подтверждение Почты'

    def __str__(self):
        return self.user.email

    def send_verification_email(self):
        link = reverse(
            viewname='users:email_verification',
            kwargs={
                'email': self.user.email,
                'url_uuid': self.url_uuid
            }
        )
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение Учетной записи для {self.user.username}'
        message = (f'Для подтверждения учетной записи,'
                   f' перейдите по ссылке {verification_link}')
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return self.expiration >= now()
