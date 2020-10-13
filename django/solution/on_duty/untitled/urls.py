from django.conf import settings
from django.contrib import admin
from django.urls import path

from mna.views import RedirectAPIv1, RedirectAPIv2
from addressbook.views import ContactHTML, ContactCSV, ContactJSON, ContactCreateView, ThankYouView, ContactUsView

from addressbook.contact_us import ContactUsView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('contact/<str:lastname>/', ContactHTML.as_view()),
    path('contact/create/', ContactCreateView.as_view()),
    path('contact.csv', ContactCSV.as_view(), name='contact-csv'),
    path('contact.json', ContactJSON.as_view(), name='contact-json'),
    path('contact.html', ContactHTML.as_view()),

    path('thank-you.html', ThankYouView.as_view()),
    path('contact-us.html', ContactUsView.as_view()),

    path('api/v1/redirect/', RedirectAPIv1.as_view()),
    path('api/v2/redirect/', RedirectAPIv2.as_view()),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
