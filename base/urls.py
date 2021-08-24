from django.contrib import admin
from django.urls import path, include
from account.views import home, guest
from django.conf.urls.static import static

from base import settings

urlpatterns = [
    path('', home, name='home'),
    path('guest/', guest, name='guest'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
