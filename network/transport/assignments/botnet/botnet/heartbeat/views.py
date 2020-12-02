import datetime
from django.views.generic import TemplateView
from botnet.heartbeat.models import Heartbeat


class HeartbeatsView(TemplateView):
    template_name = 'heartbeat/list.html'

    def get_context_data(self, **kwargs):
        month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
        return {'heartbeats': Heartbeat.objects.filter(datetime__gt=month_ago)}
