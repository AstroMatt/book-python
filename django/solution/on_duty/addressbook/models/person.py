from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    AGE_ADULT = 18 * 365.2524

    is_deleted = models.BooleanField(verbose_name=_('Is Deleted?'), default=False)

    firstname = models.CharField(verbose_name=_('First Name'), max_length=30)
    lastname = models.CharField(verbose_name=_('Last Name'), max_length=30, db_index=True)
    phone = models.IntegerField(verbose_name=_('Phone'), null=True, blank=True)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'), null=True, blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='person/', null=True, blank=True)
    friends = models.ManyToManyField(verbose_name=_('Friends'), to='addressbook.Person', blank=True)

    def is_adult(self):
        if not self.date_of_birth:
            return None

        if (date.today() - self.date_of_birth).days >= self.AGE_ADULT:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        unique_together = ['firstname', 'lastname']

