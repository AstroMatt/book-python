from django.contrib import admin
from .models import Iris


@admin.register(Iris)
class IrisAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'species']
    list_display_links = ['species']
    search_fields = ['^species']
    list_filter = ['species', 'date_added']
    radio_fields = {
        'species': admin.VERTICAL,
    }
