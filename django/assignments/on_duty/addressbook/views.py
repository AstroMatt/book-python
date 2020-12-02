import base64
from http import HTTPStatus

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, View, FormView

from addressbook.forms import ContactCreateForm, ContactUsForm
from .models import Person


class ContactHTML(TemplateView):
    template_name = 'addressbook/contact.html'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.all()
        }


class ContactCSV(TemplateView):
    template_name = 'addressbook/contact.csv'

    def get_context_data(self, **kwargs):
        contacts = Person.objects.all()
        contacts = contacts.filter(lastname__startswith='T')
        return locals()


class BasicAuth:
    def basic_auth(self):
        auth_header = self.request.environ.get('HTTP_AUTHORIZATION', None)

        if not auth_header:
            raise PermissionError

        auth_type, credentials = auth_header.split()
        credentials = base64.b64decode(credentials).decode()
        username, password = credentials.split(':')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
        else:
            raise PermissionError


class ContactJSON(BasicAuth, PermissionRequiredMixin, View):
    permission_required = 'mna.can_view'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.basic_auth()
        except PermissionError:
            return JsonResponse(status=HTTPStatus.FORBIDDEN, data={
                'status': HTTPStatus.FORBIDDEN,
                'reason': 'Forbidden',
            })

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        p = Person.objects.all().values()
        return JsonResponse(status=HTTPStatus.OK, data=list(p), safe=False)


class ContactCreateView(FormView):
    template_name = 'addressbook/contact-create.html'
    form_class = ContactCreateForm
    success_url = '/contact.html'

    def form_valid(self, form):
        Person.objects.create(
            firstname=form.cleaned_data['firstname'],
            lastname=form.cleaned_data['lastname'],
        )
        return super().form_valid(form)


class ContactUsView(FormView):
    template_name = 'addressbook/contact-form.html'
    form_class = ContactUsForm
    success_url = '/thank-you.html'


class ThankYouView(TemplateView):
    template_name = 'addressbook/thank-you.html'
