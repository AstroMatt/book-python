from django.db import models
from django.utils.translation import gettext_lazy as _


class Redirection(models.Model):
    duty_number = models.PositiveIntegerField(verbose_name=_('Duty Number'))
    msisdn = models.PositiveIntegerField(verbose_name=_('MSISDN'))

    def __str__(self):
        return f'Duty: {self.duty_number} -> {self.msisdn}'

