from django.conf.urls import url
from django.contrib import admin
from botnet.heartbeat.views import HeartbeatView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pings/', HeartbeatView.as_view())
]
