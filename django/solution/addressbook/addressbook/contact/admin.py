from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _
from contact.models import Contact, Address


class AddressInline(admin.TabularInline):
    model = Address
    max_num = 10
    min_num = 2
    extra = 1


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    autocomplete_fields = ['contact']


class AgeFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Age')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return [
            ('None', _('Not Specified')),
            ('0-10', _('0-10')),
            ('11-20', _('11-20')),
            ('21-30', _('21-30')),
            ('31-40', _('31-40')),
            ('41-50', _('41-50')),
            ('51-60', _('51-60')),
            ('Older', _('Older')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'None':
            return queryset.filter(date_of_birth=None)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'date_of_birth', 'column_age']
    list_display_links = ['lastname']
    search_fields = ['^lastname']
    list_filter = ['created', 'modified', AgeFilter]
    inlines = [AddressInline]
    exclude = ['reporter', 'created', 'updated']
    ordering = ['lastname', 'firstname']
    autocomplete_fields = ['friends']
    # formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}
    radio_fields = {
        'gender': admin.HORIZONTAL,
        'status': admin.VERTICAL
    }
    fieldsets = [
        (_('Personal Data'), {'fields': ['lastname', 'firstname', 'date_of_birth', 'gender']}),
        (_('Additional Data'), {'fields': ['email', 'bio', 'image']}),
        (_('Relations'), {'fields': ['status', 'friends']}),
    ]

    def get_list_display(self, request):
        list_display = super().get_list_display(request)

        if request.user.is_superuser and 'is_deleted' not in list_display:
            list_display += ['is_deleted']

        return list_display

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(is_deleted=False)

    def column_age(self, obj):
        age = obj.get_age()
        return str(age) if age else ''

    # https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    column_age.short_description = _('Age')
    column_age.empty_value_display = ''
    column_age.admin_order_field = 'date_of_birth'

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)

    class Media:
        js = [
            'contact/js/alert.js',
        ]

        css = {'all': [
            'contact/css/style.css',
        ]}
