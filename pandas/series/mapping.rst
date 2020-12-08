**************
Series Mapping
**************


Rationale
=========
* ``Series.apply`` - apply function to data, function can have args and/or kwargs
* ``Series.map`` - convert data from one to another using function or dict


Apply
=====
* Signature: ``Series.apply(func, convert_dtype=True, args=(), **kwds)``
* Parameters:

    * ``func: Callable``
    * ``convert_dtype: bool``; default: ``True``
    * ``args: tuple``
    * ``**kwds: dict``

* Returns: ``Union[Series, DataFrame]``

* Invoke function on values of Series
* Can be ufunc (a NumPy function that applies to the entire Series) or a Python function that only works on single values.

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)


    s = pd.Series(
        index = pd.date_range('2000-01-01', periods=4),
        data = np.random.randn(4))

    s
    # 2000-01-01    1.764052
    # 2000-01-02    0.400157
    # 2000-01-03    0.978738
    # 2000-01-04    2.240893
    # Freq: D, dtype: float64

    s.apply(int)
    # 2000-01-01    1
    # 2000-01-02    0
    # 2000-01-03    0
    # 2000-01-04    2
    # Freq: D, dtype: int64

    s.apply(lambda x: round(x, 2))
    # 2000-01-01    1.76
    # 2000-01-02    0.40
    # 2000-01-03    0.98
    # 2000-01-04    2.24
    # Freq: D, dtype: float64

    s.apply(round, ndigits=2)
    # 2000-01-01    1.76
    # 2000-01-02    0.40
    # 2000-01-03    0.98
    # 2000-01-04    2.24
    # Freq: D, dtype: float64

    s.apply(round, args=(2,))
    # 2000-01-01    1.76
    # 2000-01-02    0.40
    # 2000-01-03    0.98
    # 2000-01-04    2.24
    # Freq: D, dtype: float64

.. code-block:: python
    :caption: ``functools.partial(func, *args, **keywords)``

    from functools import partial
    import pandas as pd
    import numpy as np
    np.random.seed(0)


    s = pd.Series(
        index = pd.date_range('2000-01-01', periods=4),
        data = np.random.randn(4))

    s
    # 2000-01-01    1.764052
    # 2000-01-02    0.400157
    # 2000-01-03    0.978738
    # 2000-01-04    2.240893
    # Freq: D, dtype: float64

    round2 = partial(round, ndigits=2)
    square = partial(pow, exp=2)
    cube = partial(pow, exp=3)

    s.apply(round2)
    # 2000-01-01    1.76
    # 2000-01-02    0.40
    # 2000-01-03    0.98
    # 2000-01-04    2.24
    # Freq: D, dtype: float64

    s.apply(square)
    # 2000-01-01    3.111881
    # 2000-01-02    0.160126
    # 2000-01-03    0.957928
    # 2000-01-04    5.021602
    # Freq: D, dtype: float64

    s.apply(cube)
    # 2000-01-01     5.489520
    # 2000-01-02     0.064075
    # 2000-01-03     0.937561
    # 2000-01-04    11.252875
    # Freq: D, dtype: float64


Map
===
* Signature: ``Series.map(arg, na_action=None)``
* Parameters:

    * arg: ``Union[Callable, collections.abc.Mapping, Series]``
    * na_action: ``Optional[Literal['ignore']]``; default ``None``

* Returns: ``Series``

* Map values of Series according to input correspondence.
* Used for substituting each value in a Series with another value, that may be derived from a function, a dict or a Series.
* When arg is a dictionary, values in Series that are not in the dictionary (as keys) are converted to NaN.
* If the dictionary is a dict subclass that defines __missing__ (i.e. provides a method for default values), then this default is used rather than NaN.

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)


    s = pd.Series(
        index = pd.date_range('2000-01-01', periods=4),
        data = np.random.randn(4))

    s
    # 2000-01-01    1.764052
    # 2000-01-02    0.400157
    # 2000-01-03    0.978738
    # 2000-01-04    2.240893
    # Freq: D, dtype: float64

    s.map(int)
    # 2000-01-01    1
    # 2000-01-02    0
    # 2000-01-03    0
    # 2000-01-04    2
    # Freq: D, dtype: int64

    s.map(lambda x: round(x, 2))
    # 2000-01-01    1.76
    # 2000-01-02    0.40
    # 2000-01-03    0.98
    # 2000-01-04    2.24
    # Freq: D, dtype: float64

.. code-block:: python

    import pandas as pd


    s = pd.Series(['Watney', 'Twardowski', pd.NA, 'Lewis'])

    s
    # 0        Watney
    # 1    Twardowski
    # 2          <NA>
    # 3         Lewis
    # dtype: object

    s.map({'Watney': 'Mark', 'Twardowski': 'Jan'})
    # 0    Mark
    # 1     Jan
    # 2     NaN
    # 3     NaN
    # dtype: object

    s.map('I am a {}'.format)
    # 0        My name... Watney
    # 1    My name... Twardowski
    # 2          My name... <NA>
    # 3         My name... Lewis
    # dtype: object

    s.map('I am a {}'.format, na_action='ignore')
    # 0        My name... Watney
    # 1    My name... Twardowski
    # 2                     <NA>
    # 3         My name... Lewis
    # dtype: object


Cleaning User Input
===================
.. highlights::
    * 80% of machine learning and data science is cleaning data

Addresses
---------
.. highlights::
    * Is This the Same Address?
    * This is a dump of distinct records of a single address
    * Which one of the below is a true address?

.. code-block:: text

    'ul. Jana III Sobieskiego'
    'ul Jana III Sobieskiego'
    'ul.Jana III Sobieskiego'
    'ulicaJana III Sobieskiego'
    'Ul. Jana III Sobieskiego'
    'UL. Jana III Sobieskiego'
    'ulica Jana III Sobieskiego'
    'Ulica. Jana III Sobieskiego'

    'os. Jana III Sobieskiego'

    'Jana 3 Sobieskiego'
    'Jana 3ego Sobieskiego'
    'Jana III Sobieskiego'
    'Jana Iii Sobieskiego'
    'Jana IIi Sobieskiego'
    'Jana lll Sobieskiego'  # three small letters 'L'

Streets
-------
.. code-block:: text

    'ul'
    'ul.'
    'Ul.'
    'UL.'
    'ulica'
    'Ulica'

.. code-block:: text

    'os'
    'os.'
    'Os.'
    'osiedle'

    'oś'
    'oś.'
    'Oś.'
    'ośedle'

.. code-block:: text

    'pl'
    'pl.'
    'Pl.'
    'plac'

.. code-block:: text

    'al'
    'al.'
    'Al.'

    'aleja'
    'aleia'
    'alei'
    'aleii'
    'aleji'

House and Apartment Number
--------------------------
.. code-block:: text

    'Ćwiartki 3/4'
    'Ćwiartki 3 / 4'
    'Ćwiartki 3 m. 4'
    'Ćwiartki 3 m 4'
    'Brighton Beach 1st apt 2'
    'Brighton Beach 1st apt. 2'
    'Myśliwiecka 3/5/7'

.. code-block:: text

    '180f/8f'
    '180f/8'
    '180/8f'

.. code-block:: text

    'Jana Twardowskiego III 3 m. 3'
    'Jana Twardowskiego 13d bud. A piętro II sala 3'

Phone Numbers
-------------
.. code-block:: text

    +48 (12) 355 5678
    +48 123 555 678

.. code-block:: text

    123 555 678

    +48 12 355 5678
    +48 123-555-678
    +48 123 555 6789

    +1 (123) 555-6789
    +1 (123).555.6789

    +1 800-python
    +48123555678

    +48 123 555 678 wew. 1337
    +48 123555678,1
    +48 123555678,1,,2


Example
=======
.. code-block:: python
    :caption: String cleaning

    expected = 'Jana Twardowskiego III'
    text = 'UL. jana \tTWArdoWskIEGO 3'

    # Convert to common format
    text = text.upper()

    # Remove unwanted whitespaces
    text = text.replace('\t', '')

    # Remove unwanted special characters
    text = text.replace('.', '')

    # Remove unwanted text
    text = text.replace('UL', '')
    text = text.replace('3', 'III')

    # Formatting
    text = text.title()
    text = text.replace('Iii', 'III')
    text = text.strip()

    print('Matched:', text == expected)
    # Matched: True

    print(text)
    # Jana Twardowskiego III

.. code-block:: python
    :caption: Remove Polish diacritics

    def pl_to_latin(text):
        PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
              'ł': 'l', 'ń': 'n', 'ó': 'o',
              'ś': 's', 'ż': 'z', 'ź': 'z'}
        result = ''.join(PL.get(x,x) for x in text.lower())
        return result.capitalize()

    s = pd.Series(['Poznań', 'Swarzędz', 'Kraków',
                   'Łódź', 'Gdańsk', 'Koło', 'Dęblin'])

    s
    # 0      Poznań
    # 1    Swarzędz
    # 2      Kraków
    # 3        Łódź
    # 4      Gdańsk
    # 5        Koło
    # 6      Dęblin
    # dtype: object

    s.map(pl_to_latin)
    # 0      Poznan
    # 1    Swarzedz
    # 2      Krakow
    # 3        Lodz
    # 4      Gdansk
    # 5        Kolo
    # 6      Deblin
    # dtype: object

    s.apply(pl_to_latin)
    # 0      Poznan
    # 1    Swarzedz
    # 2      Krakow
    # 3        Lodz
    # 4      Gdansk
    # 5        Kolo
    # 6      Deblin
    # dtype: object


Assignments
===========

.. todo:: Convert assignments to literalinclude

Series Mapping Clean
--------------------
* Assignment: Series Mapping Clean
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min
* Filename: :download:`assignments/series_mapping_clean.py`

English:
    #. Use data from "Given" section (see below)
    #. Convert ``DATA`` (see input section) to ``pd.Series``
    #. Create ``pd.Series``
    #. Write function to clean up data
    #. Function takes one ``str`` argument
    #. Function returns cleaned text
    #. Apply function to all elements of ``pd.Series``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Przekonwertuj ``DATA`` (patrz sekcja input) do ``pd.Series``
    #. Napisz funkcję czyszczącą dane
    #. Funkcja przyjmuje jeden argument typu ``str``
    #. Funkcja zwraca oczyszczony tekst
    #. Zaaplikuj funkcję na wszystkich elementach ``pd.Series``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = ['ul.Mieszka II',
                'UL. Zygmunta III WaZY',
                '  bolesława chrobrego ',
                'ul Jana III SobIESkiego',
                '\tul. Jana trzeciego Sobieskiego',
                'ulicaJana III Sobieskiego',
                'UL. JA    NA 3 SOBIES  KIEGO',
                'ULICA JANA III SOBIESKIEGO  ',
                'ULICA. JANA III SOBIeskieGO',
                ' Jana 3 Sobieskiego  ',
                'Jana III Sobi  eskiego ']

Tests:
    .. code-block:: python

        s: pd.Series
        # 0               Mieszka II
        # 1        Zygmunta III Wazy
        # 2      Bolesława Chrobrego
        # 3     Jana III Sobieskiego
        # 4     Jana III Sobieskiego
        # 5     Jana III Sobieskiego
        # 6     Jana III Sobieskiego
        # 7     Jana III Sobieskiego
        # 8     Jana III Sobieskiego
        # 9     Jana III Sobieskiego
        # 10    Jana III Sobieskiego
        # dtype: object

.. todo:: Translate input data to English

