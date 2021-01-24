***********************
Development Environment
***********************


What is IDE?
============
* Integrated Development Environment
* Refactoring
* Syntax helping and highlighting
* Type hinting and checking
* VCS support
* Virtualenv support
* Debugging
* Spell checking
* Running code and inspections
* File Scopes and views
* Database explorer
* Support for testing (doctest, unittest)
* Jump to line in exceptions


How to choose?
==============
* Nie ma znaczenia z jakiego IDE skorzystasz!
* Do edycji skryptów Pythona wystarczy sam Notatnik lub Jupyter
* W miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę
* Dobre IDE pomoże Ci w Refactoringu, podpowiedziach typów, debuggingu oraz pracy z systemem kontroli wersji
* PyCharm ma dwie wersję płatną oraz darmową, wersja darmowa w zupełności nam wystarczy
* Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse


Which one is the best?
======================
#. `PyCharm Professional <https://www.jetbrains.com/pycharm/download/>`_ (Not-free)
#. `PyCharm Community <https://www.jetbrains.com/pycharm/download/>`_
#. Jupyter Notebook
#. Visual Studio Code
#. `PyDev <http://www.pydev.org/download.html>`_
#. Spyder
#. Atom


Keyboard shortcuts
==================
.. csv-table:: PyCharm Keyboard shortcuts
    :header-rows: 1
    :widths: 25, 75

    "Key Combination", "Action"
    "``ctrl`` + ``/``", "Comment multiple lines"
    "``alt`` + ``F12``", "Open Terminal"
    "``shift`` + ``F6``", "Refactor... Rename"
    "``tab``", "Indent (also used on multiple lines)"
    "``shift`` + ``tab``", "Un-indent (also used on multiple lines)"
    "``alt`` + ``1``", "Show file drawer"
    "", "Run"
    "", "Show console"
    "", "Actions"
    "``ctrl`` + ``g``", "Jump to line"
    "``ctrl`` + ``f``", "Search in file"
    "``ctrl`` + ``r``", "Replace in file"


Assignments
===========

Create Project from Git
-----------------------
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min

:Polish:
    #. Stwórz projekt w Twoim IDE wykorzystując opcję 'Create from VCS'
    #. Trener poda Ci link do repozytorium
    #. Sugestia: możesz zapisać katalog z projektem na pulpicie, aby łatwiej było znaleźć pliki
    #. Kliknij "clone" i zaczekaj na pobranie repozytorium
    #. Upewnij się, że w repozytorium jest plik ``.gitignore`` i ma zawartość
    #. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imie ``nazwisko_imie``
    #. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań
    #. Dzięki oddzielnym katalogom dla każdego uczestnika unikinemy konfliktów w Git

Create Project in Pure Python
-----------------------------
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min

:Polish:
    #. Stwórz projekt w Twoim IDE
    #. Wybierz "Pure Python" (opcja dostępna tylko w Pycharm Professional)
    #. Rozwiń listę Project Interpreter i ustaw aby korzystać z "Virtualenv"
    #. WAŻNE: Upewnij się, że masz Python 3.7 lub nowszy
    #. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imie ``nazwisko_imie``
    #. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań

Know thou IDE
-------------
* Lines of code to write: 0 lines
* Estimated time of completion: 10 min

:Polish:
    #. Jak zrobić w Twoim IDE:

        * Run...
        * Run in console
        * Debug...
        * Python Console
        * Terminal
        * Full Screen
        * Distraction Free Mode
        * Reformat Code
        * Scope

    #. Jakie są skróty klawiszowe do poszczególnych opcji?
    #. Czym się różni ``Run...`` od ``Debug...``?
    #. Czym się różni ``Python Console`` od ``Terminal``
    #. Czym się różni ``Distraction Free Mode`` od ``Full Screen``
    #. Ustaw Scope tak, aby ukryć katalog z Virtualenv

:The whys and wherefores:
    * Korzystanie z IDE
    * Uruchamianie debuggera
    * Znajomość różnicy między uruchamianiem i debuggingiem
    * Znajomość różnicy między terminalem i konsolą

Spellchecker
------------
* Lines of code to write: 0 lines
* Estimated time of completion: 3 min

:Polish:
    #. Zainstaluj plugin 'Hunspell'
    #. Pobierz z https://github.com/LibreOffice/dictionaries słownik ``.dic`` oraz ``.aff`` dla języka polskiego
    #. Skonfiguruj IDE do korzystania z tego słownika

:The whys and wherefores:
    * Korzystanie z IDE
    * Konfiguracja IDE
