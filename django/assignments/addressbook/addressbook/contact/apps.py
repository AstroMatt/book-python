from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactConfig(AppConfig):
    name = 'contact'
    verbose_name = _('Contact')
