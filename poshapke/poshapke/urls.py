from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('', include('products.urls', namespace='products')),
    path('', include('orders.urls', namespace='orders')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

admin.site.site_header = 'Панель Администратора Магазина'
admin.site.index_title = 'Создание и удаление данных'
