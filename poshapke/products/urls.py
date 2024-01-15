from django.urls import path, include

from products.views import products

app_name = 'products'

urlpatterns = [
    path('products/', products, name='products'),
    path('products/', include('basket.urls', namespace='basket'))
]
