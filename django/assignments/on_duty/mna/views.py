import json
from http import HTTPStatus
from django.http import JsonResponse
from django.views.generic import View
from .models import Redirection


class RedirectAPIv1(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        if not request.body:
            return JsonResponse(status=HTTPStatus.BAD_REQUEST, data={'reason': 'Bad Request'})

        data = json.loads(request.body.decode())
        # {'duty_number': int, 'new_msisdn': int}

        duty_number = Redirection.objects.get(duty_number=data['duty_number'])
        duty_number.msisdn = data['new_msisdn']
        duty_number.save()

        return JsonResponse(status=HTTPStatus.OK, data=data)


class RedirectAPIv2(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        if not request.body:
            return JsonResponse(status=HTTPStatus.BAD_REQUEST, data={'reason': 'Bad Request'})

        data = json.loads(request.body.decode())
        # {'dutyNumber': int, 'newMsisdn': int}

        duty_number = Redirection.objects.get(duty_number=data['dutyNumber'])
        duty_number.msisdn = data['newMsisdn']
        duty_number.save()

        return JsonResponse(status=HTTPStatus.OK, data=data)


