from http import HTTPStatus
from django.http import JsonResponse
from django.views.generic import View
from .models import Host


class HostAPI(View):
    def get(self, *args, **kwargs):
        hosts = Host.objects.all().values()
        return JsonResponse(status=HTTPStatus.OK, data=list(hosts), safe=False)
