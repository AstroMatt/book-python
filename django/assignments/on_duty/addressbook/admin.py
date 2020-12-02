import csv
from datetime import date
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from .models import Person, Address


class ExportCsvMixin:

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['export_as_csv'] = (self.export_as_csv, 'export_as_csv', self.export_as_csv.short_description)
        return actions

    def export_as_csv(self, modeladmin, request, queryset):
        model = self.model._meta
        field_names = [field.name for field in model.fields]
        filename = f'{date.today():%Y-%m-%d}_{model}.csv'

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        writer = csv.writer(
            response,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

        writer.writerow(field_names)

        for obj in queryset.order_by('id'):
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = _('Export selected as CSV')
    export_as_csv.allowed_permissions = ['view']


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0
    max_num = 4
    min_num = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['firstname', 'lastname', 'phone', 'date_of_birth']
    search_fields = ['^lastname']
    ordering = ['lastname']
    autocomplete_fields = ['friends']
    inlines = [AddressInline]
    readonly_fields = ['id']
    exclude = ['is_deleted']
    list_per_page = 100

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields

        if not request.user.is_superuser:
            return readonly_fields + ['firstname', 'lastname', 'phone', 'date_of_birth']
        else:
            return readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if not request.user.is_superuser:
            qs = qs.filter(is_deleted=False)

        return qs

    class Media:
        js = [
            'addressbook/js/admin-person.js',
        ]

        css = {'all': [
            'addressbook/css/admin-person.css',
        ]}


#@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['person', 'street', 'house_number', 'apartment_number', 'city', 'region', 'country']
    search_fields = ['^street', '^city']
    autocomplete_fields = ['person']
    ordering = ['person', 'street']
