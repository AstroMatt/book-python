from django.contrib import admin
from .models import Redirection


@admin.register(Redirection)
class RedirectionAdmin(admin.ModelAdmin):
    list_display = ['duty_number', 'msisdn']
