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

    connect('admin', 'admin')

    connect('admin', 'admin', 'localhost', 22, False, 1, True)

    connect(host='localhost', username='admin', password='admin')

    connect(
        host='localhost',
        username='admin',
        password='admin',
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
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_args_sequence.py`
* Last update: 2020-10-01

:English:
    #. Define function which takes sequence of integers as an argument
    #. Sum only even numbers
    #. Print returned value

:Polish:
    #. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    #. Zsumuj tylko parzyste liczby
    #. Wypisz zwróconą wartość

Function Arguments Divide
-------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_args_divide.py`
* Last update: 2020-10-01

:English:
    #. Define function ``divide``
    #. Function takes two arguments
    #. Function divides its arguments and returns the result
    #. Call function with ``divide(4, 2)``
    #. Call function with ``divide(4, 0)``
    #. Print returned values
    #. What to do in case of error?

:Polish:
    #. Zdefiniuj funkcję ``divide``
    #. Funkcja przyjmuje dwa argumenty
    #. Funkcja dzieli oba argumenty przez siebie i zwraca wynik dzielenia
    #. Wywołaj funkcję z ``divide(4, 2)``
    #. Wywołaj funkcję z ``divide(4, 0)``
    #. Wypisz zwracane wartości
    #. Co zrobić w przypadku błędu?

:Output:
    .. code-block:: python

        >>> divide(4, 2)
        2

        >>> divide(4, 0)
        None

Function Arguments Power
------------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_args_power.py`
* Last update: 2020-10-01

:English:
    #. Define function ``power``
    #. Function takes two arguments
    #. Second argument is optional
    #. Function returns power of the first argument to the second
    #. If only one argument was passed, consider second equal to the first one
    #. Print returned values
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj funkcję ``power``
    #. Funkcja przyjmuje dwa argumenty
    #. Drugi argument jest opcjonalny
    #. Funkcja zwraca wynik pierwszego argumentu do potęgi drugiego
    #. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    #. Wypisz zwracane wartości
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> power(4, 3)
        64

        >>> power(3)
        27

Function Arguments Translate
----------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_args_translate.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Define function ``translate`` with parameter ``text``
    #. Use ``str.join()`` with generator expression to iterate over ``text``
    #. If letter is in ``PL`` then use conversion value as letter, otherwise take letter
    #. Return from function translated ``text``
    #. Call ``translate('zażółć')``
    #. Call ``translate('gęślą')``
    #. Call ``translate('jaźń')``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj funkcję ``translate`` przyjmującą parametr ``text``
    #. Użyj ``str.join()`` z wyrażeniem generatorowym do iteracji po ``text``
    #. Jeżeli litera jest w ``PL`` to użyj przekonwertowanej wartości jako litera, w przeciwnym przypadku to weź literę
    #. Zwróć z funkcji przetłumaczony ``text``
    #. Uruchom ``translate('zażółć')``
    #. Uruchom ``translate('gęślą')``
    #. Uruchom ``translate('jaźń')``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
              'ł': 'l', 'ń': 'n', 'ó': 'o',
              'ś': 's', 'ż': 'z', 'ź': 'z'}

:Output:
    .. code-block:: python

        >>> translate('zażółć')
        'zazolc'

        >>> translate('gęślą')
        'gesla'

        >>> translate('jaźń')
        'jazn'


.. _Function Arguments Clean:

Function Arguments Clean
------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/function_args_clean.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write function cleaning up data
    #. Function takes one argument of type ``str``
    #. Function returns cleaned text
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Napisz funkcję czyszczącą dane
    #. Funkcja przyjmuje jeden argument typu ``str``
    #. Funkcja zwraca oczyszczony tekst
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

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

:Output:
    .. code-block:: python

        'Mieszka II'
        'Zygmunta III Wazy'
        'Bolesława Chrobrego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input

.. todo:: Translate input data to English

Function Arguments Numbers to Str
---------------------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/function_args_numstr_simple.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Given is pilot's alphabet for numbers
    #. Convert ``DATA: dict[int, str]`` to ``data: dict[str, str]`` (keys as ``str``)
    #. For input data (see input section below)
    #. Define function converting ``int`` or ``float`` to text form in Pilot's Speak
    #. You cannot change ``DATA``, but you can modify ``data``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Dany jest alfabet pilotów dla numerów
    #. Przekonwertuj ``DATA: dict[int, str]`` na ``data: dict[str, str]`` (klucze jako ``str``)
    #. Dla danych wejściowych (patrz sekcja input poniżej)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów
    #. Nie możesz zmieniać ``DATA``, ale możesz modyfikować ``data``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
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

    .. code-block:: python

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

:Output:
    .. code-block:: python

        'one niner six niner'
        'tree one tree tree seven'
        'one tree and tree seven'
        'tree one and tree tree seven'
        'minus one niner six niner'
        'minus tree one and tree tree seven'
        'minus fower niner and tree fife'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups

Function Arguments Numbers to Human
-----------------------------------
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/function_args_numstr_human.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Define function converting ``int`` or ``float`` to text form
    #. Text form must be in proper grammar form
    #. Max 6 digits before decimal separator (point ``.``)
    #. Max 5 digits after decimal separator (point ``.``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową
    #. Forma tekstowa musi być poprawna gramatycznie
    #. Max 6 cyfr przed separatorem dziesiętnym (point ``.``)
    #. Max 5 cyfr po separatorze dziesiętnym (point ``.``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        1969
        31337
        13.37
        31.337
        -1969
        -31.337
        -49.35

:Output:
    .. code-block:: python

        'one thousand nine hundred sixty nine'
        'thirty one thousand three hundred thirty seven'
        'thirteen and thirty seven hundredths'
        'thirty one three hundreds thirty seven thousands'
        'minus one thousand nine hundred sixty nine'
        'minus thirty one and three hundreds thirty seven thousands'
        'minus forty nine and thirty five hundreds'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups
