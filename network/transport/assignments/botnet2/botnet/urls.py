from django.contrib import admin
from django.urls import path
from host.views import HostAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hosts/', HostAPI.as_view())
]
