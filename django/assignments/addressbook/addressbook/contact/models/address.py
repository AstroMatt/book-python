from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    contact = models.ForeignKey(verbose_name=_('Contact'), to='contact.Contact', on_delete=models.CASCADE)
    street = models.CharField(verbose_name=_('Street'), max_length=30, null=True, blank=True, default=None)
    house_number = models.IntegerField(verbose_name=_('House Number'), null=True, blank=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=30, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.street} {self.house_number}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
