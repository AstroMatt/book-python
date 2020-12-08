*****************
HTTP using stdlib
*****************


``http.HTTPStatus``
===================

Using statuses
--------------
.. code-block:: python

    from http import HTTPStatus

    HTTPStatus.OK
    HTTPStatus.OK == 200

    HTTPStatus.OK.value
    HTTPStatus.OK.phrase
    HTTPStatus.OK.description

    list(HTTPStatus)

Most common statuses
--------------------
.. code-block:: python

    from http import HTTPStatus


    HTTPStatus.OK                       # 200
    HTTPStatus.CREATED                  # 201
    HTTPStatus.MOVED_PERMANENTLY        # 301
    HTTPStatus.FOUND                    # 302
    HTTPStatus.BAD_REQUEST              # 400
    HTTPStatus.UNAUTHORIZED             # 401
    HTTPStatus.FORBIDDEN                # 403
    HTTPStatus.METHOD_NOT_ALLOWED       # 405
    HTTPStatus.NOT_FOUND                # 404
    HTTPStatus.INTERNAL_SERVER_ERROR    # 500

All statuses
------------
.. csv-table:: ``http.HTTPStatus``
    :header-rows: 1
    :widths: 15, 85

    "Code", "Description"
    "100", "``CONTINUE``"
    "101", "``SWITCHING_PROTOCOLS``"
    "102", "``PROCESSING``"
    "200", "``OK``"
    "201", "``CREATED``"
    "202", "``ACCEPTED``"
    "203", "``NON_AUTHORITATIVE_INFORMATION``"
    "204", "``NO_CONTENT``"
    "205", "``RESET_CONTENT``"
    "206", "``PARTIAL_CONTENT``"
    "207", "``MULTI_STATUS``"
    "208", "``ALREADY_REPORTED``"
    "226", "``IM_USED``"
    "300", "``MULTIPLE_CHOICES``"
    "301", "``MOVED_PERMANENTLY``"
    "302", "``FOUND``"
    "303", "``SEE_OTHER``"
    "304", "``NOT_MODIFIED``"
    "305", "``USE_PROXY``"
    "307", "``TEMPORARY_REDIRECT``"
    "308", "``PERMANENT_REDIRECT``"
    "400", "``BAD_REQUEST``"
    "401", "``UNAUTHORIZED``"
    "402", "``PAYMENT_REQUIRED``"
    "403", "``FORBIDDEN``"
    "404", "``NOT_FOUND``"
    "405", "``METHOD_NOT_ALLOWED``"
    "406", "``NOT_ACCEPTABLE``"
    "407", "``PROXY_AUTHENTICATION_REQUIRED``"
    "408", "``REQUEST_TIMEOUT``"
    "409", "``CONFLICT``"
    "410", "``GONE``"
    "411", "``LENGTH_REQUIRED``"
    "412", "``PRECONDITION_FAILED``"
    "413", "``REQUEST_ENTITY_TOO_LARGE``"
    "414", "``REQUEST_URI_TOO_LONG``"
    "415", "``UNSUPPORTED_MEDIA_TYPE``"
    "416", "``REQUEST_RANGE_NOT_SATISFIABLE``"
    "417", "``EXPECTATION_FAILED``"
    "421", "``MISDIRECTED_REQUEST``"
    "422", "``UNPROCESSABLE_ENTITY``"
    "423", "``LOCKED``"
    "424", "``FAILED_DEPENDENCY``"
    "426", "``UPGRADE_REQUIRED``"
    "428", "``PRECONDITION_REQUIRED``"
    "429", "``TOO_MANY_REQUESTS``"
    "431", "``REQUEST_HEADER_FIELDS_TOO_LARGE``"
    "500", "``INTERNAL_SERVER_ERROR``"
    "501", "``NOT_IMPLEMENTED``"
    "502", "``BAD_GATEWAY``"
    "503", "``SERVICE_UNAVAILABLE``"
    "504", "``GATEWAY_TIMEOUT``"
    "505", "``HTTP_VERSION_NOT_SUPPORTED``"
    "506", "``VARIANT_ALSO_NEGOTIATES``"
    "507", "``INSUFFICIENT_STORAGE``"
    "508", "``LOOP_DETECTED``"
    "510", "``NOT_EXTENDED``"
    "511", "``NETWORK_AUTHENTICATION_REQUIRED``"


``urllib``
==========
.. literalinclude:: src/http-urllib.py
    :language: python
    :caption: ściąganie danych z internetu, które trzeba rozpakować, Dane są w formacie TSV (tab separator values), można je rozpakować modułem CSV i podać jako ``delimiter='\t'``


``http.server``
===============
.. warning:: ``http.server`` is not recommended for production. It only implements basic security checks.

* https://docs.python.org/3.7/library/http.server.html#module-http.server


Simple HTTP Server
------------------
.. code-block:: console

    $ python -m http.server 8000 --bind 127.0.0.1

Own HTTP Sever
--------------
.. code-block:: python

    import re
    from http import HTTPStatus
    from http.server import BaseHTTPRequestHandler
    from http.server import HTTPServer

    SERVER = ('localhost', 8080)


    class RequestHandler(BaseHTTPRequestHandler):
        def do_HEAD(self):
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write('<html>')
            self.wfile.write('<body>Hello World!</body>')
            self.wfile.write('</html>')

        def do_POST(self):
            if re.search('/api/v1/*', self.path):
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)

                self.send_response(HTTPStatus.OK)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write('<html>')
                self.wfile.write('<body>Hello World!</body>')
                self.wfile.write('</html>')


    try:
        print('Starting server {SERVER}, use <Ctrl-C> to stop')
        httpd = HTTPServer(SERVER, RequestHandler)
        httpd.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server...')
        httpd.socket.close()

Threaded server with JSON response
----------------------------------
* ``http.server.ThreadingHTTPServer`` since Python 3.7

.. code-block:: python

    import json
    from http import HTTPStatus
    from http.server import ThreadingHTTPServer
    from http.server import BaseHTTPRequestHandler


    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            data = {
                'firstname': 'José',
                'lastname': 'Jiménez'
            }
            response = bytes(json.dumps(data), 'UTF-8')

            self.send_response(HTTPStatus.OK)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(response)
            self.server.path = self.path


    def run(host='127.0.0.1', port=8080):
        print(f'Starting server on {host}:{port}, use <Ctrl-C> to stop')
        httpd = ThreadingHTTPServer((host, port), RequestHandler)
        httpd.serve_forever()


    if __name__ == '__main__':
        run()


``http.client``
===============

Connecting
----------
.. code-block:: python

    h1 = http.client.HTTPConnection('www.python.org')
    h2 = http.client.HTTPConnection('www.python.org:80')
    h3 = http.client.HTTPConnection('www.python.org', 80)
    h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)

GET Request
-----------
.. code-block:: python

    import http.client


    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("GET", "/")
    response = conn.getresponse()

    response.status         # 200
    response.reason         # OK

    data = response.read()  # This will return entire content.
    conn.close()

GET Request in chunks
---------------------
.. code-block:: python

    import http.client


    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("GET", "/")
    response = conn.getresponse()

    # The following example demonstrates reading data in chunks.
    while not response.closed:
        print(response.read(200))   # 200 bytes

GET Request to Not Existing Resource
------------------------------------
.. code-block:: python

    import http.client


    conn = http.client.HTTPSConnection("www.python.org")

    conn.request("GET", "/parrot.spam")
    response = conn.getresponse()

    response.status  # 404
    response.reason  # Not Found

    data = response.read()
    print(data)
    # b'<!doctype html> ... </body>\n</html>\n'

    conn.close()

HEAD Request
------------
.. code-block:: python

    import http.client

    conn = http.client.HTTPSConnection("www.python.org")

    conn.request("HEAD", "/")
    response = conn.getresponse()

    response.status         # 200
    response.reason         # OK

    print(response.headers)
    # Server: nginx
    # Content-Type: text/html; charset=utf-8
    # X-Frame-Options: SAMEORIGIN
    # x-xss-protection: 1; mode=block
    # X-Clacks-Overhead: GNU Terry Pratchett
    # Via: 1.1 varnish
    # Content-Length: 48925
    # Accept-Ranges: bytes
    # Date: Tue, 06 Nov 2018 11:06:52 GMT
    # Via: 1.1 varnish
    # Age: 599
    # Connection: keep-alive
    # X-Served-By: cache-iad2142-IAD, cache-fra19148-FRA
    # X-Cache: HIT, HIT
    # X-Cache-Hits: 1, 2
    # X-Timer: S1541502413.680933,VS0,VE0
    # Vary: Cookie
    # Strict-Transport-Security: max-age=63072000; includeSubDomains

    conn.close()

POST Request
------------
.. code-block:: python

    import http.client
    import urllib.parse


    params = urllib.parse.urlencode({
        '@number': 12524,
        '@type': 'issue',
        '@action': 'show'
    })

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }

    conn = http.client.HTTPSConnection("bugs.python.org")
    conn.request("POST", "/", params, headers)

    response = conn.getresponse()

    response.status  # 302
    response.reason  # 'Found'

    data = response.read()
    print(data)
    # b'Redirecting to <a href="https://bugs.python.org/issue12524">https://bugs.python.org/issue12524</a>'

    conn.close()


Basic Auth
----------
* https://github.com/settings/tokens

.. code-block:: python

    import http.client
    import json
    from http import HTTPStatus
    from base64 import b64encode


    USERNAME = 'my_username'
    TOKEN = 'my_token'


    auth = bytes(f'{USERNAME}:{TOKEN}', 'utf-8')
    auth = b64encode(auth).decode('ascii')

    headers = {
        'Authorization': f'Basic {auth}',
        'User-Agent': 'Python http.client',
        'Accept': 'application/json'
    }

    conn = http.client.HTTPSConnection(host="api.github.com", port=443)
    conn.request("GET", "/users", headers=headers)

    response = conn.getresponse()

    if response.status == HTTPStatus.OK:
        body = response.read().decode()
        data = json.loads(body)
        print(data)

    conn.close()


Assignments
===========

.. todo:: Convert assignments to literalinclude

REST API
--------
* Assignment: REST API
* Complexity: medium
* Lines of code: 60 lines
* Time: 21 min
* Filename: :download:`assignments/http_github.py`

English:
    .. todo:: English Translation

Polish:
    #. Załóż darmowe konto na Github i potwierdź email
    #. Wejdź na stronę internetową https://github.com/settings/tokens
    #. Wygeneruj w swoim profilu token (scope ``public_repo`` - Access public repositories)
    #. Używając biblioteki standardowej w Pythonie
    #. Zaciągnij informacje o repozytoriach użytkownika Django na https://github.com
    #. Każdy request uwierzytelnij za pomocą Basic Auth i swojego Access Tokena
    #. Następnie przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``
    #. Przeglądnij to repozytorium i jego listę komitów
    #. Podaj datę i opis ostatniego komita
    #. Znajdź numery ID zadań (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu

Hints:
    .. code-block:: console

        $ curl -X GET https://api.github.com/orgs/django/repos
        $ curl -X GET https://api.github.com/repos/django/django/commits

    .. code-block:: python

        ...
        "name": "django",
        "fullname": "django/django",
        ...
        # wyszukaj "commits_url"
