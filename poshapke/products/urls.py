from django.urls import include, path

from products.views import ProductsListView

app_name = 'products'

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='index'),
    path('products/<str:slug>', ProductsListView.as_view(), name='category'),
    path('products/', include('basket.urls', namespace='basket'))
]
