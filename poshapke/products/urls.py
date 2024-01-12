from django.urls import path, include

from basket.views import basket_add
from products.views import products

app_name = 'products'

urlpatterns = [
    path('products/', products, name='products'),
    path('products/add/<str:slug>/', basket_add, name='basket_add'),
]
