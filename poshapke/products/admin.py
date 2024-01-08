from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import Category, Products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Модель отображения категории.
    """
    list_display = (
        'id',
        'name',
        'slug',
        'description',
        'get_count'
    )
    list_display_links = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name', )

    @admin.display(description='Количество Символов')
    def get_count(self, category: Category):
        """
        Получаем количество символов
        :param category:
        :return: Длинна символов
        """
        return len(category.description)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'slug',
        'description',
        'price',
        'quantity',
        'product_image',
        'time_create',
        'time_update',
        'is_published',
        'category'
    )
    readonly_fields = ('product_image', )
    list_display_links = ('name', 'slug')
    list_filter = ('name', 'is_published')
    search_fields = ('name',)
    list_editable = ('is_published', 'category')
    list_per_page = 6
    actions = ('set_published', )
    prepopulated_fields = {'slug': ('name', )}

    @admin.action(description='Опубликовать выбранные товары')
    def set_published(self, request, queryset):
        """
        Позволяет выбрать несколько товаров и
        опубликовать их.
        """
        count = queryset.update(is_published=True)
        return self.message_user(request, message=f'Изменено {count}')

    @admin.display(description='Фотография Продукта')
    def product_image(self, product: Products):
        """
        Выводит картинку на экран в
        админ панели.
        """
        if product.image:
            return mark_safe(f'<img src="{product.image.url}" width=50>')
        return 'Нет Изображения'
