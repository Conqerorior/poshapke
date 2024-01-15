from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        help_text='Введите название Категории',
        verbose_name='Категория'
    )
    slug = models.CharField(
        max_length=128,
        unique=True,
        help_text='URL Категории',
        verbose_name='URL Категории'
    )
    description = models.TextField(
        max_length=256,
        help_text='Опишите Категорию',
        blank=False,
        verbose_name='Описание Категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=128,
        help_text='Название Товара',
        verbose_name='Имя Товара'
    )
    slug = models.CharField(
        max_length=128,
        verbose_name='URL Продукта',
        unique=True
    )
    description = models.TextField(
        max_length=256,
        help_text='Опишите Товар',
        verbose_name='Описание Товара'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text='Введите Цену Товара',
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        help_text='Введите Количество Товара',
        verbose_name='Количество Товара'
    )
    # rating = models.PositiveSmallIntegerField(
    #     verbose_name='Рейтинг Товара',
    #     help_text='Поставьте оценку',
    #     validators=[
    #         MinValueValidator(
    #             limit_value=1,
    #             message='Минимальная оценка 1'
    #         ),
    #         MaxValueValidator(
    #             limit_value=5,
    #             message='Максимальная оценка 5'
    #         )
    #     ]
    # )
    image = models.ImageField(
        upload_to='product_image',
        help_text='Загрузите Фото',
        verbose_name='Фото Товара'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время Создания'
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Видимость Товара'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        verbose_name='Категория Товара',
        related_name='category'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('time_update',)

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum_basket() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)
