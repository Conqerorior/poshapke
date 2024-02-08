from django.db import models
from users.models import Users


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(
        max_length=128, help_text='Введите Имя', verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=128, help_text='Введите Фамилию', verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=128, help_text='Введите email', verbose_name='email'
    )
    address = models.CharField(
        max_length=256, help_text='Введите Адрес', verbose_name='Адрес'
    )
    basket_history = models.JSONField(
        default=dict, verbose_name='История Заказов'
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Время Создания Заказа'
    )
    status = models.PositiveSmallIntegerField(
        default=CREATED, choices=STATUSES, verbose_name='Статус Заказа'
    )
    owner = models.ForeignKey(
        to=Users, on_delete=models.CASCADE, verbose_name='Заказчик'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('created',)

    def __str__(self):
        return f'Заказ #{self.id}. {self.first_name} {self.last_name}'
