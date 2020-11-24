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

About IDE Usage
---------------
* Assignment: About IDE Usage
* Complexity: easy
* Lines of code to write: 0 lines
* Estimated time: 8 min
* Solution: TODO

English:
    .. todo:: English Translation

Polish:
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

About IDE Spellchecker
----------------------
* Assignment: About IDE Spellchecker
* Complexity: easy
* Lines of code to write: 0 lines
* Estimated time: 5 min
* Solution: TODO

English:
    .. todo:: English Translation

Polish:
    #. Zainstaluj w PyCharm plugin 'Hunspell' (File -> Settings -> Plugins -> Marketplace -> 'Hunspell')
    #. Pobierz z https://github.com/LibreOffice/dictionaries/tree/master/pl_PL słownik ``.dic`` oraz ``.aff`` dla języka polskiego

        * https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pl_PL/pl_PL.aff
        * https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pl_PL/pl_PL.dic

    #. Skonfiguruj IDE do korzystania z tego słownika (File -> Settings -> Editor -> Spelling -> Add custom dictionary)

