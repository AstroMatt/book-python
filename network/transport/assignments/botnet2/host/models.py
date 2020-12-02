from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    date_created = models.DateTimeField(verbose_name=_('Date Created'), auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name=_('Date Modified'), auto_now=True)

    class Meta:
        abstract = True


class Port(BaseModel):
    STATE_OPEN = 'open'
    STATE_CLOSED = 'closed'
    STATE_FILTERED = 'filtered'
    STATE_UNKNOWN = 'unknown'
    STATE_CHOICES = [
        (STATE_OPEN, _('Open')),
        (STATE_CLOSED, _('Closed')),
        (STATE_FILTERED, _('Filtered')),
        (STATE_UNKNOWN, _('Unknown'))]

    host = models.ForeignKey(verbose_name=_('Host'), to='host.Host', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name=_('Number'), validators=[MinValueValidator(1025), MaxValueValidator(65535)])
    state = models.CharField(verbose_name=_('State'), max_length=20, choices=STATE_CHOICES, default=STATE_UNKNOWN, db_index=True)

    def __str__(self):
        return f'{self.number}'


class Host(BaseModel):
    ACTIVE_CHOICES = [
        (False, _('Inactive')),
        (True, _('Active')),
        (None, _('Unknown'))]

    uid = models.PositiveIntegerField(verbose_name=_('Unique ID'))
    ip = models.GenericIPAddressField(verbose_name=_('IP Address'))
    is_active = models.BooleanField(verbose_name=_('Is active?'), choices=ACTIVE_CHOICES, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.ip}'


class HeartBeat(BaseModel):
    ip = models.GenericIPAddressField(verbose_name=_('IP Address'))
    port = models.PositiveIntegerField(verbose_name=_('Number'), validators=[MinValueValidator(1025), MaxValueValidator(65535)])

    def __str__(self):
        return f'{self.ip}:{self.port}'
