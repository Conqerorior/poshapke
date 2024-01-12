from django.db import models

from products.models import Products
from users.models import Users


class Basket(models.Model):
    user = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        verbose_name='Покупатель'
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество товаров в Корзине'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время добавления в Корзину'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ('time_create',)

    def __str__(self):
        return f'{self.user} {self.product}'
