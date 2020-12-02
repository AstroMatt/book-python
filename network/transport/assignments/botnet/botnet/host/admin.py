from django.contrib import admin
from botnet.host.models import Host
from botnet.host.models import Group


class HostInline(admin.TabularInline):
    model = Host
    extra = 1


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'host', 'port']
    search_fields = ['^host']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['^name']
    inlines = [HostInline]
