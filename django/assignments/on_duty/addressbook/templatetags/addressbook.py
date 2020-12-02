from django import template
from django.utils.translation import gettext_lazy as _


register = template.Library()


@register.simple_tag
def is_adult(contact):
    if contact.is_adult() is None:
        return ''

    if contact.is_adult():
        return _('Adult')
    else:
        return _('Kid')
