**************
HTML Scrapping
**************


* Requests HTML https://github.com/psf/requests-html
* BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
* Scrapy https://scrapy.org/

``BeautifulSoup``
=================

Example usage
-------------
* https://github.com/AstroMatt/thesis-masters-aerospace/blob/master/src/worldspaceflight-astronaut-bios.py

Install
-------
.. code-block:: console

    $ pip install beautifulsoup4

Parser
------
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| Parser               | Typical usage                              | Advantages                     | Disadvantages            |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| Python's html.parser | ``BeautifulSoup(markup, "html.parser")``   | * Batteries included           | * Not very tolerant      |
|                      |                                            | * Decent speed                 |   (before Python 2.7.3   |
|                      |                                            | * tolerant (as of Python 2.7.3 |   or 3.2.2)              |
|                      |                                            |   and 3.2.)                    |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| lxml's HTML parser   | ``BeautifulSoup(markup, "lxml")``          | * Very fast                    | * External C dependency  |
|                      |                                            | * Tolerant                     |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| lxml's XML parser    | ``BeautifulSoup(markup, "lxml-xml")``      | * Very fast                    | * External C dependency  |
|                      | ``BeautifulSoup(markup, "xml")``           | * The only currently supported |                          |
|                      |                                            |   XML parser                   |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| html5lib             | ``BeautifulSoup(markup, "html5lib")``      | * Extremely tolerant           | * Very slow              |
|                      |                                            | * Parses pages the same way a  | * External Python        |
|                      |                                            |   web browser does             |   dependency             |
|                      |                                            | * Creates valid HTML5          |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+

Open
----
.. code-block:: python

    from bs4 import BeautifulSoup

    with open("index.html") as file:
        html = BeautifulSoup(file, 'html.parser')

    html.find(id='menubox').decompose()

Basic Usage
-----------
.. code-block:: python

    from bs4 import BeautifulSoup


    html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
    """

    html = BeautifulSoup(html_doc, 'html.parser')

    print(html.prettify())
    # <html>
    #  <head>
    #   <title>
    #    The Dormouse's story
    #   </title>
    #  </head>
    #  <body>
    #   <p class="title">
    #    <b>
    #     The Dormouse's story
    #    </b>
    #   </p>
    #   <p class="story">
    #    Once upon a time there were three little sisters; and their names were
    #    <a class="sister" href="http://example.com/elsie" id="link1">
    #     Elsie
    #    </a>
    #    ,
    #    <a class="sister" href="http://example.com/lacie" id="link2">
    #     Lacie
    #    </a>
    #    and
    #    <a class="sister" href="http://example.com/tillie" id="link2">
    #     Tillie
    #    </a>
    #    ; and they lived at the bottom of a well.
    #   </p>
    #   <p class="story">
    #    ...
    #   </p>
    #  </body>
    # </html>

.. code-block:: python

    html.title              # <title>The Dormouse's story</title>
    html.title.name         # 'title'
    html.title.string       # 'The Dormouse's story'
    html.title.parent.name  # 'head'
    html.p                  # <p class="title"><b>The Dormouse's story</b></p>
    html.p['class']         # 'title'
    html.a                  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    html.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    html.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

Iterating over items
--------------------
.. code-block:: python

    for link in html.find_all('a'):
        print(link.get('href'))

    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

Getting Page Text
-----------------
.. code-block:: python

    html.get_text()
    # The Dormouse's story
    #
    # The Dormouse's story
    #
    # Once upon a time there were three little sisters; and their names were
    # Elsie,
    # Lacie and
    # Tillie;
    # and they lived at the bottom of a well.
    #
    # ...


Assignments
===========

Iris
----
* Assignment name: Iris
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/scrapping_iris.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Za pomocą beautifulsoup4 ze strony https://github.com/AstroMatt/book-python/blob/master/numerical-analysis/data/iris-dirty.csv pobierz dane zbióru Irysów.
    #. Parsując kod HTML oczyść dane.
    #. Skasuj pierwszy wiersz nagłówkowy.
    #. Kolumny nazwij: ``Sepal length``, ``Sepal width``, ``Petal length``, ``Petal width``, ``Species``
    #. Wyświetl dane w formacie listy dictów, kluczami mają być nazwy kolumn.

EVA
---
* Assignment name: EVA
* Complexity level: medium
* Lines of code to write: 100 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/scrapping_eva.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Na podstawie podanych URL:

        * https://www.worldspaceflight.com/bios/eva/eva.php
        * https://www.worldspaceflight.com/bios/eva/eva2.php
        * https://www.worldspaceflight.com/bios/eva/eva3.php
        * https://www.worldspaceflight.com/bios/eva/eva4.php

    #. Scrappuj stronę wykorzystując ``beautifulsoup4``
    #. Przygotuj plik CSV z danymi dotyczącymi spacerów kosmicznych
    #. Spróbuj to samo zrobić za pomocą ``pandas.read_html()``:

        * Podając jako parametr czwarty URL
        * Dla częściowo sparsowanej strony, np. wyciągniętej tabelki

:The whys and wherefores:
    * Komunikacja HTTP (request, response)
    * Parsowanie odpowiedzi HTTP
    * Sprawdzanie stanu połączenia
    * Serializacja i parsowanie *HTML*
    * Korzystanie z Web Inspectora w przeglądarce
    * Używanie bibliotek zewnętrznych
