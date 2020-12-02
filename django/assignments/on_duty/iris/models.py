from django.db import models
from django.utils.translation import gettext_lazy as _


class Iris(models.Model):
    SPECIES_SETOSA = 'setosa'
    SPECIES_CHOICES = [
        (SPECIES_SETOSA, _('Iris Setosa')),
        ('virginica', _('Iris Virginica')),
        ('versicolor', _('Iris Versicolor')),
    ]

    date_added = models.DateTimeField(verbose_name=_('Date Added'), auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name=_('Date Modified'), auto_now=True)

    sepal_length = models.DecimalField(verbose_name=_('Sepal Length'), help_text=_('cm'), max_digits=3, decimal_places=1)
    sepal_width = models.DecimalField(verbose_name=_('Sepal Width'), help_text=_('cm'), max_digits=3, decimal_places=1)
    petal_length = models.DecimalField(verbose_name=_('Petal Length'), help_text=_('cm'), max_digits=3, decimal_places=1)
    petal_width = models.DecimalField(verbose_name=_('Petal Width'), help_text=_('cm'), max_digits=3, decimal_places=1)
    species = models.CharField(verbose_name=_('Species'), max_length=30, choices=SPECIES_CHOICES, help_text=_('Select one'))

