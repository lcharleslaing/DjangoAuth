from django.contrib import admin
from django.urls import path, include
from account.views import home, guest


urlpatterns = [
    path('', home, name='home'),
    path('guest/', guest, name='guest'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls'))
]
