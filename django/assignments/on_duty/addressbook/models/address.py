from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    person = models.ForeignKey(verbose_name=_('Person'), to='addressbook.Person', on_delete=models.CASCADE)
    street = models.CharField(verbose_name=_('Street'), max_length=30, db_index=True)
    house_number = models.CharField(verbose_name=_('House Number'), max_length=5)
    apartment_number = models.CharField(verbose_name=_('Apartment Number'), max_length=5, null=True, blank=True)
    city = models.CharField(verbose_name=_('City'), max_length=30, null=True, blank=True, db_index=True)
    post_code = models.IntegerField(verbose_name=_('Post Code'), null=True, blank=True)
    region = models.CharField(verbose_name=_('Region'), max_length=30, null=True, blank=True)
    country = models.CharField(verbose_name=_('Country'), max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.street}, {self.city}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

