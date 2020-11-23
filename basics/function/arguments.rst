.. _Function Arguments:

******************
Function Arguments
******************


Rationale
=========
.. glossary::

    argument
        Value/variable/reference being passed to the function

    positional argument
        Value passed to function - order is important

    keyword argument
        Value passed to function resolved by name - order is not important


Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    my_function(<arguments>)

.. code-block:: python

    add(1, 2)
    add(a=1, b=2)
    add(1, b=2)

Positional Arguments
====================
.. highlights::
    * Order of positional arguments has significance

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(2, 1)          # 1
    subtract(1, 2)          # -1


Keyword Arguments
=================
.. highlights::
    * Order of keyword arguments has no significance

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(a=2, b=1)      # 1
    subtract(b=1, a=2)      # 1


Positional and Keyword Arguments
================================
.. highlights::
    * Positional arguments must be at the left side
    * Keyword arguments must be at the right side

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(2, b=1)        # 1
    subtract(a=2, 1)        # SyntaxError: positional argument follows keyword argument
    subtract(2, a=1)        # TypeError: subtract() got multiple values for argument 'a'


Examples
========
.. code-block:: python
    :caption: Example 1

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Mark Watney')          # My name... Mark Watney
    hello(name='Mark Watney')     # My name... Mark Watney
    hello()                       # My name... José Jiménez

.. code-block:: python
    :caption: Example 2

    connect('myusername', 'mypassword')

    connect('myusername', 'mypassword', 'example.com', 443, False, 1, True)

    connect(host='example.com', username='myusername', password='mypassword')

    connect(
        host='example.com',
        username='myusername',
        password='mypassword',
        port=443,
        ssl=True,
        persistent=True,
    )

.. code-block:: python
    :caption: Example 3

    read_csv('iris.csv')

    read_csv('iris.csv', encoding='utf-8')

    read_csv('iris.csv', encoding='utf-8', parse_dates=['date_of_birth'])

    read_csv('iris.csv', skiprows=3, delimiter=';')

    read_csv('iris.csv',
        encoding='utf-8',
        skiprows=3,
        delimiter=';',
        usecols=['Sepal Length', 'Species'],
        parse_dates=['date_of_birth']
    )


Assignments
===========

Function Arguments Sequence
---------------------------
* Assignment name: Function Arguments Sequence
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Suggested filename: function_args_sequence.py

English:
    #. Define function which takes sequence of integers as an argument
    #. Sum only even numbers
    #. Print returned value

Polish:
    #. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    #. Zsumuj tylko parzyste liczby
    #. Wypisz zwróconą wartość

Function Arguments Divide
-------------------------
* Assignment name: Function Arguments Divide
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Suggested filename: function_args_divide.py

English:
    #. Define function ``divide``
    #. Function takes two arguments
    #. Function divides its arguments and returns the result
    #. Call function with ``divide(4, 2)``
    #. Call function with ``divide(4, 0)``
    #. Print returned values
    #. What to do in case of error?

Polish:
    #. Zdefiniuj funkcję ``divide``
    #. Funkcja przyjmuje dwa argumenty
    #. Funkcja dzieli oba argumenty przez siebie i zwraca wynik dzielenia
    #. Wywołaj funkcję z ``divide(4, 2)``
    #. Wywołaj funkcję z ``divide(4, 0)``
    #. Wypisz zwracane wartości
    #. Co zrobić w przypadku błędu?

Tests:
    .. code-block:: text

        >>> divide(4, 0)
        >>> divide(4, 2)
        2.0

Function Arguments Power
------------------------
* Assignment name: Function Arguments Power
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Suggested filename: function_args_power.py

English:
    #. Define function ``power``
    #. Function takes two arguments
    #. Second argument is optional
    #. Function returns power of the first argument to the second
    #. If only one argument was passed, consider second equal to the first one
    #. Print returned values
    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj funkcję ``power``
    #. Funkcja przyjmuje dwa argumenty
    #. Drugi argument jest opcjonalny
    #. Funkcja zwraca wynik pierwszego argumentu do potęgi drugiego
    #. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    #. Wypisz zwracane wartości
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: text

        >>> power(4, 3)
        64
        >>> power(3)
        27

Function Arguments Translate
----------------------------
* Assignment name: Function Arguments Translate
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Suggested filename: function_args_translate.py

English:
    #. Define function ``translate`` with parameter ``text``
    #. Use ``str.join()`` with generator expression to iterate over ``text``
    #. If letter is in ``PL`` then use conversion value as letter, otherwise take letter
    #. Return from function translated ``text``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj funkcję ``translate`` przyjmującą parametr ``text``
    #. Użyj ``str.join()`` z wyrażeniem generatorowym do iteracji po ``text``
    #. Jeżeli litera jest w ``PL`` to użyj skonwertowanej wartości jako litera, w przeciwnym przypadku to weź literę
    #. Zwróć z funkcji przetłumaczony ``text``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
              'ł': 'l', 'ń': 'n', 'ó': 'o',
              'ś': 's', 'ż': 'z', 'ź': 'z'}

Tests:
    .. code-block:: text

        >>> translate('zażółć')
        'zazolc'
        >>> translate('gęślą')
        'gesla'
        >>> translate('jaźń')
        'jazn'
        >>> translate('zażółć gęślą jaźń')
        'zazolc gesla jazn'


.. _Function Arguments Clean:

Function Arguments Clean
------------------------
* Assignment name: Function Arguments Clean
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Suggested filename: function_args_clean.py

English:
    #. Write function cleaning up data
    #. Function takes one argument of type ``str``
    #. Function returns cleaned text
    #. Compare result with "Tests" section (see below)

Polish:
    #. Napisz funkcję czyszczącą dane
    #. Funkcja przyjmuje jeden argument typu ``str``
    #. Funkcja zwraca oczyszczony tekst
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: text

        >>> clean('ul.Mieszka II')
        'Mieszka II'
        >>> clean('UL. Zygmunta III WaZY')
        'Zygmunta III Wazy'
        >>> clean('  bolesława chrobrego ')
        'Bolesława Chrobrego'
        >>> clean('ul Jana III SobIESkiego')
        'Jana III Sobieskiego'
        >>> clean('\tul. Jana trzeciego Sobieskiego')
        'Jana III Sobieskiego'
        >>> clean('ulicaJana III Sobieskiego')
        'Jana III Sobieskiego'
        >>> clean('UL. JA    NA 3 SOBIES  KIEGO')
        'Jana III Sobieskiego'
        >>> clean('ULICA JANA III SOBIESKIEGO  ')
        'Jana III Sobieskiego'
        >>> clean('ULICA. JANA III SOBIeskieGO')
        'Jana III Sobieskiego'
        >>> clean(' Jana 3 Sobieskiego  ')
        'Jana III Sobieskiego'
        >>> clean('Jana III Sobi  eskiego ')
        'Jana III Sobieskiego'

TODO: Translate input data to English

Function Arguments Numbers to Str
---------------------------------
* Assignment name: Function Arguments Numbers to Str
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Suggested filename: function_args_numstr.py

English:
    #. Use data from "Given" section (see below)
    #. Given is pilot's alphabet for numbers
    #. Convert ``DATA: dict[int, str]`` to ``data: dict[str, str]`` (keys as ``str``)
    #. Define function ``pilot_say`` converting ``int`` or ``float`` to text form in Pilot's Speak
    #. You cannot change ``DATA``, but you can modify ``data``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Dany jest alfabet pilotów dla numerów
    #. Przekonwertuj ``DATA: dict[int, str]`` na ``data: dict[str, str]`` (klucze jako ``str``)
    #. Zdefiniuj funkcję ``pilot_say`` konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów
    #. Nie możesz zmieniać ``DATA``, ale możesz modyfikować ``data``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'tree',
            4: 'fower',
            5: 'fife',
            6: 'six',
            7: 'seven',
            8: 'ait',
            9: 'niner',
        }

Tests:
    .. code-block:: text

        >>> pilot_say(1969)
        'one niner six niner'
        >>> pilot_say(31337)
        'tree one tree tree seven'
        >>> pilot_say(13.37)
        'one tree and tree seven'
        >>> pilot_say(31.337)
        'tree one and tree tree seven'
        >>> pilot_say(-1969)
        'minus one niner six niner'
        >>> pilot_say(-31.337)
        'minus tree one and tree tree seven'
        >>> pilot_say(-49.35)
        'minus fower niner and tree fife'

Function Arguments Numbers to Human
-----------------------------------
* Assignment name: Function Arguments Numbers to Human
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Suggested filename: function_args_numhuman.py

English:
    #. Define function converting ``int`` or ``float`` to text form
    #. Text form must be in proper grammar form
    #. Max 6 digits before decimal separator (point ``.``)
    #. Max 5 digits after decimal separator (point ``.``)
    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową
    #. Forma tekstowa musi być poprawna gramatycznie
    #. Max 6 cyfr przed separatorem dziesiętnym (point ``.``)
    #. Max 5 cyfr po separatorze dziesiętnym (point ``.``)
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: text

        >>> number_to_str(1969)
        'one thousand nine hundred sixty nine'
        >>> number_to_str(31337)
        'thirty one thousand three hundred thirty seven'
        >>> number_to_str(13.37)
        'thirteen and thirty seven hundredths'
        >>> number_to_str(31.337)
        'thirty one and three hundreds thirty seven thousands'
        >>> number_to_str(-1969)
        'minus one thousand nine hundred sixty nine'
        >>> number_to_str(-31.337)
        'minus thirty one and three hundreds thirty seven thousands'
        >>> number_to_str(-49.35)
        'minus forty nine and thirty five hundreds'

