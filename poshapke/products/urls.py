from django.urls import path, include

from products.views import products

app_name = 'products'

urlpatterns = [
    path('products/', products, name='index'),
    path('products/<str:slug>', products, name='category'),
    path('products/', include('basket.urls', namespace='basket'))
]
