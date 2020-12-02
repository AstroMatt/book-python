import json
import logging
from socketserver import BaseRequestHandler, UDPServer
from django.conf import settings
from django.core.management import base
from host.models import HeartBeat

log = logging.getLogger(__name__)


class RequestHandler(BaseRequestHandler):
    def handle(self):
        host, port = self.client_address
        data = self.request[0].decode()
        data = json.loads(data)
        log.warning(f'Received ping from {host}:{port}/UDP', data)
        HeartBeat.objects.create(ip=host, port=port)


class Command(base.BaseCommand):
    help = 'Start Heart Beat receiver'

    def handle(self, *args, **options):
        host = settings.HEART_BEAT_SERVER
        port = settings.HEART_BEAT_PORT

        self.stdout.write('Starting Heart Beat receiver')
        self.stdout.write(f'Listening for pings on {host}:{port}/UDP...')

        listener = UDPServer((host, port), RequestHandler)
        listener.serve_forever()
