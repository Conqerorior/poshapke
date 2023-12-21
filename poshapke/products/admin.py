from django.contrib import admin
from products.models import Category, Products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'description'
    )
    list_display_links = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name', )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'description',
        'price',
        'quantity',
        'image',
        'time_create',
        'time_update',
        'is_published',
        'category'
    )
    list_display_links = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('is_published', 'category')
    list_per_page = 6
