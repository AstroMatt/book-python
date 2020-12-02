import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    STATUS_BEST_FRIEND = 'best-friend'
    STATUS_FRIEND = 'friend'
    STATUS_ACQUAINTANCE = 'acquaintance'
    STATUS_OTHER = 'other'
    STATUS_CHOICES = [
        (STATUS_BEST_FRIEND, _('Best Friend')),
        (STATUS_FRIEND, _('Friend')),
        (STATUS_ACQUAINTANCE, _('Acquaintance')),
        (STATUS_OTHER, _('Other'))]

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = None
    GENDER_CHOICES = [
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_OTHER, _('Undisclosed'))]

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(verbose_name=_('Reporter'), to='auth.User', on_delete=models.CASCADE, null=True, default=None)
    is_deleted = models.BooleanField(verbose_name=_('Is deleted?'), default=False)

    firstname = models.CharField(verbose_name=_('First Name'), max_length=30)
    lastname = models.CharField(verbose_name=_('Last Name'), max_length=30, db_index=True)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'), null=True, blank=True, default=None)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True, default=None)
    bio = models.TextField(verbose_name=_('Bio'), null=True, blank=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), null=True, blank=True, default=None)
    status = models.CharField(verbose_name=_('Status'), max_length=30, choices=STATUS_CHOICES, null=True, blank=True, default=None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=30, choices=GENDER_CHOICES, null=True, blank=True, default=None)
    friends = models.ManyToManyField(verbose_name=_('Friends'), to='contact.Contact', blank=True, default=None)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def get_age(self):
        if not self.date_of_birth:
            return None

        today = datetime.date.today()
        return today.year - self.date_of_birth.year


    def save(self, *args, **kwargs):
        # is called at Model.save()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        unique_together = ['firstname', 'lastname']
