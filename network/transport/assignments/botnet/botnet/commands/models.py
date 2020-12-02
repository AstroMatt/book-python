from django.db import models
from django.utils.translation import gettext_lazy as _


class Command(models.Model):
    date_add = models.DateTimeField(
        verbose_name=_('Datetime Add'),
        auto_now=True)

    date_modified = models.DateTimeField(
        verbose_name=_('Datetime Modified'),
        auto_now_add=True)

    is_active = models.BooleanField(
        verbose_name=_('Is Active?'),
        default=False)

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50,
        db_index=True)

    command = models.TextField(
        verbose_name=_('Command'))

    comment = models.TextField(
        verbose_name=_('Comment'),
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.command}'

    class Meta:
        verbose_name = _('Command')
        verbose_name_plural = _('Commands')
