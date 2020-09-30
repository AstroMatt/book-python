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


How to Choose?
==============
* Nie ma znaczenia z jakiego IDE skorzystasz!
* Do edycji skryptów Pythona wystarczy sam Notatnik lub Jupyter
* W miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę
* Dobre IDE pomoże Ci w refaktoringu, podpowiedziach typów, debuggingu oraz pracy z systemem kontroli wersji
* PyCharm ma dwie wersję płatną oraz darmową, wersja darmowa w zupełności nam wystarczy
* Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse


Which One is the Best?
======================
#. `PyCharm Professional <https://www.jetbrains.com/pycharm/download/>`_ (Not-free)
#. `PyCharm Community <https://www.jetbrains.com/pycharm/download/>`_
#. Jupyter Notebook
#. Visual Studio Code
#. `PyDev <http://www.pydev.org/download.html>`_
#. Spyder
#. Atom
#. Vim

.. note:: This are my preferences. Choosing best IDE is very opinionated.


Keyboard Shortcuts
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

About IDE Create from VCS
-------------------------
* Assignment name: About IDE Create from VCS
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min
* Solution: TODO
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Stwórz projekt w Twoim IDE wykorzystując opcję 'Create from VCS'
    #. Trener poda Ci link do repozytorium
    #. Sugestia: możesz zapisać katalog z projektem na pulpicie, aby łatwiej było znaleźć pliki
    #. Kliknij "clone" i zaczekaj na pobranie repozytorium
    #. Upewnij się, że w repozytorium jest plik ``.gitignore`` i ma zawartość
    #. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imię ``nazwisko_imie``
    #. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań
    #. Dzięki oddzielnym katalogom dla każdego uczestnika unikniemy konfliktów w Git

About IDE Create Project
------------------------
* Assignment name: About IDE Create Project
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min
* Solution: TODO
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Stwórz projekt w Twoim IDE
    #. Wybierz "Pure Python" (opcja dostępna tylko w Pycharm Professional)
    #. Rozwiń listę Project Interpreter i ustaw aby korzystać z "Virtualenv"
    #. WAŻNE: Upewnij się, że masz Python 3.7 lub nowszy
    #. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imię ``nazwisko_imie``
    #. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań

About IDE Usage
---------------
* Assignment name: About IDE Usage
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 8 min
* Solution: TODO
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

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

About IDE Spellchecker
----------------------
* Assignment name: About IDE Spellchecker
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min
* Solution: TODO
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Zainstaluj w PyCharm plugin 'Hunspell' (File -> Settings -> Plugins -> Marketplace -> 'Hunspell')
    #. Pobierz z https://github.com/LibreOffice/dictionaries/tree/master/pl_PL słownik ``.dic`` oraz ``.aff`` dla języka polskiego

        * https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pl_PL/pl_PL.aff
        * https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pl_PL/pl_PL.dic

    #. Skonfiguruj IDE do korzystania z tego słownika (File -> Settings -> Editor -> Spelling -> Add custom dictionary)

:The whys and wherefores:
    * Korzystanie z IDE
    * Konfiguracja IDE
