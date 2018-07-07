from django.urls import path, include, re_path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    re_path(r'^oauth2/', include('provider.oauth2.urls')),
]
