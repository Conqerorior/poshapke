from django.urls import path

from orders.views import OrderCreateView

app_name = 'orders'

urlpatterns = [
    path('orders_create/', OrderCreateView.as_view(), name='orders_create'),
]
