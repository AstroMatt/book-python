***********************
HTTP using ``requests``
***********************


Basic API
=========
.. code-block:: python

    import requests

    requests.get('https://httpbin.org/get')                          # <Response [200]>
    requests.post('https://httpbin.org/post', data={'key':'value'})  # <Response [200]>
    requests.put('https://httpbin.org/put', data={'key':'value'})    # <Response [200]>
    requests.delete('https://httpbin.org/delete')                    # <Response [200]>
    requests.head('https://httpbin.org/get')                         # <Response [200]>
    requests.options('https://httpbin.org/get')                      # <Response [200]>


Response
========
.. code-block:: python

    from http import HTTPStatus
    import requests


    response = requests.get('https://httpbin.org/get')
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = reponse.raw      # Raw Response Content
        data = reponse.content  # Binary Response Content
        data = response.text    # Response Content
        data = response.json()  # JSON Response Content

        print(data)


GET Requests
============
* params

.. code-block:: python

    from http import HTTPStatus
    import requests


    response = requests.get('https://httpbin.org/get')
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    from http import HTTPStatus
    import requests


    params = {'key1': 'value1', 'key2': 'value2'}

    response = requests.get('https://httpbin.org/get', params=params)
    # <Response [200]>

    print(response.url)
    # https://httpbin.org/get?key2=value2&key1=value1

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    from http import HTTPStatus
    import requests


    data = {'key1': 'value1', 'key2': ['value2', 'value3']}

    response = requests.get('https://httpbin.org/get', params=data)
    # <Response [200]>

    print(response.url)
    # https://httpbin.org/get?key1=value1&key2=value2&key2=value3

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)


POST Requests
=============

POST Request with data
----------------------
.. code-block:: python

    from http import HTTPStatus
    import requests


    data = {'first_name': 'José', 'last_name': 'Jiménez'}

    response = requests.post('https://httpbin.org/post', data=data)
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Created')

.. code-block:: python

    from http import HTTPStatus
    import requests


    data = {'key1': ['value1', 'value2']}

    response = requests.post('https://httpbin.org/post', data=data)
    # <Response [200]>

    print(response.text)
    # {
    #   ...
    #   "form": {
    #     "key1": [
    #       "value1",
    #       "value2"
    #     ]
    #   },
    #   ...
    # }

    if response.status_code == HTTPStatus.OK:
        print('Created')

POST Request with JSON
----------------------
.. code-block:: python

    import json
    from http import HTTPStatus
    import requests


    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
    }

    response = requests.post('https://httpbin.org/post', data=json.dumps(data))
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Created')

.. code-block:: python

    import json
    from http import HTTPStatus
    import requests


    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
    }

    response = requests.post('https://httpbin.org/post', json=data)
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Created')


DELETE Requests
===============
.. code-block:: python

    import requests
    from http import HTTPStatus


    response = requests.delete('https://httpbin.org/delete')
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Deleted')


Custom Headers
==============
.. code-block:: python

    import requests
    from http import HTTPStatus


    headers = {
        'User-Agent': 'Python requests'
    }

    response = requests.get('https://httpbin.org/post', headers=headers)
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    response.headers
    # {
    #     'content-encoding': 'gzip',
    #     'transfer-encoding': 'chunked',
    #     'connection': 'close',
    #     'server': 'nginx/1.0.4',
    #     'x-runtime': '148ms',
    #     'etag': '"e1ca502697e5c9317743dc078f67693f"',
    #     'content-type': 'application/json'
    # }

.. code-block:: python

    response.headers['Content-Type']
    # 'application/json'

    response.headers.get('content-type')
    # 'application/json'


Timeout
=======
.. code-block:: python

    import requests


    requests.get('https://httpbin.org/get', timeout=0.001)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # requests.exceptions.Timeout: HTTPConnectionPool(host='httpbin.org', port=80): Request timed out. (timeout=0.001)


Basic Auth
==========
.. code-block:: python

    import requests
    from http import HTTPStatus


    response = requests.get('https://api.github.com/users', auth=('login', 'password'))
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)


Requests OAuth
==============
* http://requests-oauthlib.readthedocs.io/en/latest/index.html

.. code-block:: console

    $ pip install requests_oauthlib

.. literalinclude:: src/requests-oauthlib.py
    :name: listing-requests-oauthlib
    :language: python
    :caption: Requests OAuth


Assignments
===========

REST API
--------
* Complexity level: medium
* Lines of code to write: 35 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/requests_github.py`

#. Załóż darmowe konto na Github i potwierdź email
#. Wejdź na stronę internetową https://github.com/settings/tokens
#. Wygeneruj w swoim profilu token (scope ``public_repo`` - Access public repositories)
#. Używając biblioteki ``requests``
#. Zaciągnij informacje o repozytoriach użytkownika Django na https://github.com
#. Każdy request uwierzytelnij za pomocą Basic Auth i swojego Access Tokena
#. Następnie przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``
#. Przeglądnij to repozytorium i jego listę commitów
#. Podaj datę i opis ostatniego commita
#. Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu

:The whys and wherefores:
    * Komunikacja HTTP (request, response)
    * Parsowanie odpowiedzi HTTP
    * Sprawdzanie stanu połączenia
    * Serializacja i parsowanie *JSON*
    * Korzystanie z API i dokumentacji
    * Regexpy
    * Używanie biblioteki standardowej i bibliotek zewnętrznych

:Hints:
    .. code-block:: console

        $ curl -X GET https://api.github.com/orgs/django/repos
        $ curl -X GET https://api.github.com/repos/django/django/commits

    .. code-block:: python

        ...
        "name": "django",
        "full_name": "django/django",
        ...
        # wyszukaj "commits_url"
