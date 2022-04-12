import django
from django.conf.urls import include
from django.contrib import admin
from django.urls import path


if django.VERSION < (1, 9):
    admin_urls = include(admin.site.urls)
else:
    admin_urls = admin.site.urls

urlpatterns = [
    path('admin/', admin_urls),
]
