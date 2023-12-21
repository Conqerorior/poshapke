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
        help_text='Слаг Категории',
        verbose_name='Слаг Категории'
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
        verbose_name='Слаг Продукта'
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
        verbose_name='Категория Товара'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('time_update',)

    def __str__(self):
        return self.name
