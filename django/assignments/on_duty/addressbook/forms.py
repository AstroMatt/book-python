import re

from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Person


class ContactUsForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname']

    def regex(self, pattern, text):
        if not re.match(pattern, text):
            raise ValidationError(_(f'Invalid character'))

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        firstname = firstname.title()

        self.regex(
            pattern=r'^\w\w[\s\w-]*\w$',
            text=firstname,
        )

        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        lastname = lastname.title()

        self.regex(
            pattern=r'^\w\w[\s\w-]*\w$',
            text=lastname,
        )

        return lastname
