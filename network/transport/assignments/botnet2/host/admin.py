from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Host, Port, HeartBeat


class PortInline(admin.TabularInline):
    model = Port
    extra = 1
    min_num = 1


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    inlines = [PortInline]
    search_fields = ['^ip']
    list_filter = ['is_active']
    list_display = ['ip', 'is_active', 'uid']
    radio_fields = {
        'is_active': admin.VERTICAL,
    }


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    autocomplete_fields = ['host']


@admin.register(HeartBeat)
class HeartBeatAdmin(admin.ModelAdmin):
    list_display = ['field_date', 'ip', 'port']
    list_per_page = 10

    def field_date(self, model):
        return f'{model.date_created:%Y-%m-%d %H:%M:%S}'

    field_date.short_description = _('Date')

    def field_address(self, model):
        return f'{model.ip}:{model.port}'
