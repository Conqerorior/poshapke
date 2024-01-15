from django.urls import path

from basket.views import basket_add, basket_remove

app_name = 'basket'

urlpatterns = [
    path('add/<str:slug>/', basket_add, name='basket_add'),
    path('remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
