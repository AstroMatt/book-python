from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Heartbeat(models.Model):
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
        return f'[{self.datetime:%Y-%m-%d %H:%M:%S}] {self.host}:{self.port}'

    class Meta:
        verbose_name = _('Heartbeat')
        verbose_name_plural = _('Heartbeats')
