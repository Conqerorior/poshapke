from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Панель Администратора Магазина'
admin.site.index_title = 'Создание и удаление данных'
