*****************************
ReST and Sphinx documentation
*****************************


reStructuredText vs. Markdown
=============================


Format reStructuredText
=======================
* https://devguide.python.org/documenting/#rst-primer

Po co?
------

Paragrafy
---------
* newline

Nagłówki
--------
* Tytuł
* Nagłówek pierwszego poziomu
* Nagłówek drugiego poziomu
* Nagłówek trzeciego poziomu
* Nagłówek czwartego poziomu (czy stosować?)

Odnośniki
---------
* Wewnątrz dokumentu
* numref
* na zewnątrz dokumentu

Obrazki i media
---------------
* figure (scale, name, align, podpisy pod obrazkami)

Specjalne wstawki
-----------------
* ``.. todo::``

Listingi kodu
-------------
* Osadzone
* Z plików zewnętrznych

TODO
----

Listy
-----
* listy nieuporządkowane
* listy numerowane
* jednopoziomowe i zagnieżdżone
* listy mieszane

Tabele
------
* Table
* List Table
* CSV Table

Cytowanie
---------
* ``cite``
* bibtex


Sphinx
======

Zależności
----------
* ``requirements.txt``

    .. code-block:: text

        # Minimalne wymaganie
        sphinx==2.2.*

        # Theme Read the Docs
        sphinx_rtd_theme

        # System cytowania i parsowanie bibtex
        sphinxcontrib-bibtex

        # Jeżeli chcemy generować slajdy RevealJS
        sphinxjp.themes.revealjs

Config
------
* Wersja na podstawie hasha git

Dobre praktyki
--------------
* podział na rozdziały
* rozkład katalogów
* listingi kodu
* zdjęcia
* dane w tabelkach CSV
* konwencja nazewnicza plików
* konwencja nazewnicza figure, csv-table, literalinclude

Generowanie dokumentacji
------------------------
* Table of Contents

toctree
-------

Automatyczne odpalanie doctestów do listingów kodu
--------------------------------------------------

Osadzanie LaTeX
---------------

Budowanie
---------
* make html
* make singlehtml
* make pdf

* generowanie Word (docx) -> pandoc

Read the docs
=============
* http://readthedocs.org


Assignments
===========

Dokumentacja
------------
* Assignment name: Dokumentacja
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 30 lines
* Estimated time of completion: 13 min
* Solution: TODO

:English:
    .. todo:: English Translation

:Polish:
    #. Za pomocą ``sphinx-quickstart`` stwórz dokumentację.
    #. Zmień theme na ``sphinx_rtd_theme``
    #. Dokument zatytułuj "Szkolenie z Pythona"
    #. Stwórz nagłówek pierwszego poziomu "Obrazki i teksty" i w nim osadź obrazek jako figure, wraz tekstem opisującym, obrazek ma być połowy wielkości i wycentrowany, nazwany
    #. Stwórz nagłówek pierwszego poziomu "Lorem Ipsum" i wklej tekst lorem ipsum do dokumentacji.
    #. W tekście lorem ipsum wstaw numref do obrazka
    #. Stwórz nagłówek pierwszego poziomu i zamieść tabelę Irysów na podstawie danych Iris Dataset
    #. Stwórz nagłówek pierwszego poziomu "Listingi kodu" i osadź dwa swoje skrypty z poprzednich zadań:

        * książka adresowa jako ``literalinclude`` w nagłówku drugiego poziomu "Książka Adresowa"
        * prosty skrypt jako ``code-block`` w nagłówku drugiego poziomu "Pozostałe przykłady"
        * które podejście jest lepsze?

    #. Tekst lorem ipsum oznacz jako cytowanie cycerona wykorzystując bibtext

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'

