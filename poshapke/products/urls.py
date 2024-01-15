from django.urls import path

from basket.views import basket_add, basket_remove
from products.views import products

app_name = 'products'

urlpatterns = [
    path('products/', products, name='products'),
    path('products/add/<str:slug>/', basket_add, name='basket_add'),
    path('products/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
