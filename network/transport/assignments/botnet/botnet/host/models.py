from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        db_index=True,
        max_length=50)

    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')


class Host(models.Model):
    group = models.ForeignKey(
        verbose_name=_('Group'),
        to='host.Group')

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        auto_now_add=True,
        db_index=True)

    host = models.GenericIPAddressField(
        verbose_name=_('Host'),
        db_index=True)

    port = models.PositiveIntegerField(
        verbose_name=_('Port'),
        help_text=_('1025-65535'),
        validators=[
            MinValueValidator(1025),
            MaxValueValidator(65535)])

    def __str__(self):
        return f'{self.host}:{self.port}'

    class Meta:
        verbose_name = _('Host')
        verbose_name_plural = _('Hosts')
