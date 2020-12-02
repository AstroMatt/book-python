from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from botnet.commands.models import Command


@admin.register(Command)
class CommandAdmin(ImportExportModelAdmin):
    list_display = ['date_modified', 'is_active', 'command', 'comment']
    search_fields = ['command']
    list_filter = ['is_active']
