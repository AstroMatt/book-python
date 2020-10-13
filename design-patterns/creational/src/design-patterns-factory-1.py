import os


class HttpClientInterface:
    def GET(self):
        raise NotImplementedError

    def POST(self):
        raise NotImplementedError


class GatewayLive(HttpClientInterface):
    def GET(self):
        """execute GET request over network"""

    def POST(self):
        """execute POST request over network"""


class GatewayStub(HttpClientInterface):
    def GET(self):
        return {'firstname': 'José', 'lastname': 'Jiménez'}

    def POST(self):
        return {'status': 200, 'reason': 'OK'}


class HttpClientFactory:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            if os.getenv('ENVIRONMENT') == 'production':
                cls.instance = GatewayLive()
            else:
                cls.instance = GatewayStub()

        return cls.instance


client = HttpClientFactory()
result = client.GET()
print(result)


client2 = HttpClientFactory()
result1 = client2.GET()
result2 = client2.POST()

print(result1)
print(result2)
