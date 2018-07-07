from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('oauth2/', include('provider.oauth2.urls')),
    path('admin/', admin.site.urls)
]
