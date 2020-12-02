from django.urls import path
from contact.views import ListView, DetailView, ContactAPI


urlpatterns = [
    path('<int:id>/', DetailView.as_view(), name='details'),
    path('', ListView.as_view(), name='list'),
    path('api/', ContactAPI.as_view())
]
