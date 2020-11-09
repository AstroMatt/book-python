****
HTTP
****

Narzędzia
=========

Web Inspector
-------------

curl
----

wget
----

DNS
===
* /etc/hosts
* DNS

HTTP Protocol
=============

HTTP and HTTPS
--------------

HTTP/1.1 vs. HTTP/2.0
---------------------

URI vs URL
----------
* SEO friendly URL

text protocol
-------------

Status Code
-----------
* https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

.. csv-table:: Http Response Codes
    :header-rows: 1
    :widths: 10, 20, 70
    :file: data/http-status-codes.csv

Header
------
* Host
* ETag
* Last-Modified
* Accept
* Accept-Encoding
* Accept-Language
* Referer
* Cache-Control
* Cookie
* DNT
* User-Agent
* X-*

``q=...`` parameters
--------------------
.. code-block:: text

    Accept-Language: en-US,en;q=0.9,pl;q=0.8

Request
-------
.. code-block:: text

    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pl;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: _ga=GA1.2.1711323714.1523218102; csrftoken=CwTmac4VUT7FcyFAEKkIXWCxQurIZVbU
    DNT: 1
    Host: python.astrotech.io
    If-Modified-Since: Wed, 13 Jun 2018 00:15:11 GMT
    If-None-Match: W/"5b20620f-60e2"
    Referer: http://python.astrotech.io/django/django-apps.html
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36

Response
--------
.. code-block:: text

    Connection: keep-alive
    Date: Wed, 13 Jun 2018 07:21:58 GMT
    ETag: "5b20620f-60e2"
    Last-Modified: Wed, 13 Jun 2018 00:15:11 GMT
    Server: nginx/1.10.3 (Ubuntu)
    X-Cname-TryFiles: True
    X-Deity: web01
    X-Served: Nginx

stateless
---------

sessions
--------
* bazy danych
* cache
* pliki
* memory

Cookies
-------
* ustawa o cookies

HTTP Methods
============
.. csv-table:: Http Response Codes
    :header-rows: 1
    :widths: 20, 80
    :file: data/http-methods.csv

GET vs POST
-----------
* ``?argument1=value&argument2=value``
* single argument
* multiple arguments
* arrays
* files
* multipart
* security

POST vs. PUT
------------

POST and CSRF
-------------
* csrf_token

PATCH?!
-------

OPTIONS and CORS
----------------
.. code-block:: python

    http_method_names = ['get', 'post', 'options']

    def options(self, request, *args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = ', '.join(http_method_names).upper()
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response


HTML + JS + CSS
===============
