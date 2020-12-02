from django.contrib import admin
from botnet.heartbeat.models import Heartbeat


@admin.register(Heartbeat)
class HeartbeatAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'host', 'port']
    search_fields = ['^host']
