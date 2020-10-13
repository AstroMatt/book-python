from django.contrib import admin
from django.utils.translation import gettext_lazy as _


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'date_of_birth', 'column_age']
    list_display_links = ['lastname']
    search_fields = ['^lastname']
    list_filter = ['created', 'modified', AgeFilter]
    inlines = [AddressInline]
    exclude = ['reporter', 'created', 'updated']
    readonly_fields = []
    ordering = ['lastname', 'firstname']
    autocomplete_fields = ['friends']
    fieldsets = [
        (_('Personal Data'), {'fields': ['lastname', 'firstname', 'date_of_birth', 'gender']}),
        (_('Additional Data'), {'fields': ['email', 'bio', 'image']}),
        (_('Relations'), {'fields': ['status', 'friends']})]
    radio_fields = {
        'gender': admin.HORIZONTAL,
        'status': admin.VERTICAL}
    # formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}

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

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
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
