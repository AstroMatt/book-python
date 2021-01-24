*****************
DataFrame Mapping
*****************


.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Map
===
* ``.map()`` works element-wise on a Series

.. code-block:: python

    df['Morning'].map(lambda value: round(value, 2))
    # 1999-12-30    1.76
    # 1999-12-31    1.87
    # 2000-01-01   -0.10
    # 2000-01-02    0.76
    # 2000-01-03    1.49
    # 2000-01-04   -2.55
    # 2000-01-05    2.27
    # Freq: D, Name: Morning, dtype: float64

.. code-block:: python

    df['Morning'].map(int)
    # 1999-12-30    1
    # 1999-12-31    1
    # 2000-01-01    0
    # 2000-01-02    0
    # 2000-01-03    1
    # 2000-01-04   -2
    # 2000-01-05    2
    # Freq: D, Name: Morning, dtype: int64


Apply
=====
* ``.apply()`` works on a row / column basis of a DataFrame

.. code-block:: python

    df['Morning'].apply(int)
    # 1999-12-30    1
    # 1999-12-31    1
    # 2000-01-01    0
    # 2000-01-02    0
    # 2000-01-03    1
    # 2000-01-04   -2
    # 2000-01-05    2
    # Freq: D, Name: Morning, dtype: int64

.. code-block:: python

    df['Morning'].apply(lambda value: round(value, 2))
    # 1999-12-30    1.76
    # 1999-12-31    1.87
    # 2000-01-01   -0.10
    # 2000-01-02    0.76
    # 2000-01-03    1.49
    # 2000-01-04   -2.55
    # 2000-01-05    2.27


Applymap
========
* ``.applymap()`` works element-wise on a DataFrame


Summary
=======
* ``Series.map`` works element-wise on a Series
* ``Series.map`` operate on one element at time
* ``Series.map`` https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

* ``Series.apply`` operate on one element at time
* ``Series.apply`` https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html

* ``DataFrame.apply`` works on a row / column basis of a DataFrame
* ``DataFrame.apply`` operates on entire rows or columns at a time
* ``DataFrame.apply`` https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html

* ``DataFrame.applymap`` works element-wise on a DataFrame
* ``DataFrame.applymap`` operate on one element at time
* ``DataFrame.applymap`` https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.applymap.html

First major difference: **DEFINITION**

    * ``map`` is defined on Series ONLY
    * ``applymap`` is defined on DataFrames ONLY
    * ``apply`` is defined on BOTH

Second major difference: **ARGUMENT TYPE**

    * ``map`` accepts ``dict``s, ``Series``, or callable
    * ``applymap`` and ``apply`` accept callables only

Third major difference: **BEHAVIOR**

    * ``map`` is elementwise for Series
    * ``applymap`` is elementwise for DataFrames
    * ``apply`` also works elementwise but is suited to more complex operations and aggregation. The behaviour and return value depends on the function.

Fourth major difference (the most important one): **USE CASE**

    * ``map`` is meant for mapping values from one domain to another, so is optimised for performance (e.g., ``df['A'].map({1:'a', 2:'b', 3:'c'})``)
    * ``applymap`` is good for elementwise transformations across multiple rows/columns (e.g., ``df[['A', 'B', 'C']].applymap(str.strip)``)
    * ``apply`` is for applying any function that cannot be vectorised (e.g., ``df['sentences'].apply(nltk.sent_tokenize)``)

Footnotes:

    * ``map`` when passed a dictionary/Series will map elements based on the keys in that dictionary/Series. Missing values will be recorded as NaN in the output.
    * ``applymap`` in more recent versions has been optimised for some operations. You will find ``applymap`` slightly faster than ``apply`` in some cases. My suggestion is to test them both and use whatever works better.
    * ``map`` is optimised for elementwise mappings and transformation. Operations that involve dictionaries or Series will enable pandas to use faster code paths for better performance.
    * ``Series.apply`` returns a scalar for aggregating operations, Series otherwise. Similarly for ``DataFrame.apply``. Note that ``apply`` also has fastpaths when called with certain NumPy functions such as ``mean``, ``sum``, etc.

.. figure:: img/pd-mapping.png
    :width: 75%
    :align: center

.. note:: Source: https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas


Cleaning User Input
===================
.. highlights::
    * 80% of machine learning and data science is cleaning data

Is This the Same Address?
-------------------------
.. highlights::
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

Spelling and Abbreviations
--------------------------
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

    '1/2'
    '1 / 2'
    '1/ 2'
    '1 /2'
    '3/5/7'

.. code-block:: text

    '1 m. 2'
    '1 m 2'
    '1 apt 2'
    '1 apt. 2'

.. code-block:: text

    '180f/8f'
    '180f/8'
    '180/8f'

.. code-block:: text

    '13d bud. A'

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
    +48 123555678,1,2,3


Conversion
==========
.. code-block:: python

    LETTERS_EN = 'abcdefghijklmnopqrstuvwxyz'
    LETTERS_PL = 'aąbcćdeęfghijklłmnńoóprsśtuwyzżź'
    LETTERS_PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                    'ł': 'l', 'ń': 'n', 'ó': 'o',
                    'ś': 's', 'ż': 'z', 'ź': 'z'}

.. code-block:: python

    MONTHS_EN = ['January', 'February', 'March', 'April',
                 'May', 'June', 'July', 'August', 'September',
                 'October', 'November', 'December']

    MONTHS_PL = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień',
                 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień',
                 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']

    MONTHS_PLEN = {'Styczeń': 'January',
                   'Luty': 'February',
                   'Marzec': 'March',
                   'Kwiecień': 'April',
                   'Maj': 'May',
                   'Czerwiec': 'June',
                   'Lipiec': 'July',
                   'Sierpień': 'August',
                   'Wrzesień': 'September',
                   'Październik': 'October',
                   'Listopad': 'November',
                   'Grudzień': 'December'}

    MONTHS_ENPL = {'January': 'Styczeń',
                   'February': 'Luty',
                   'March': 'Marzec',
                   'April': 'Kwiecień',
                   'May': 'Maj',
                   'June': 'Czerwiec',
                   'July': 'Lipiec',
                   'August': 'Sierpień',
                   'September': 'Wrzesień',
                   'October': 'Październik',
                   'November': 'Listopad',
                   'December': 'Grudzień'}


Assignments
===========

DataFrame Mapping
-----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/df_mapping_split.py`

:English:
    #. Download :download:`data/phones.csv`
    #. Use ``parse_dates=['date']`` on reading file
    #. Split column with datetime into two separate: date and time columns

:Polish:
    #. Pobierz :download:`data/phones.csv`
    #. Użyj ``parse_dates=['date']`` przy wczytywaniu pliku
    #. Podziel kolumnę z datetime na dwie osobne: datę i czas

:Hint:
    * ``phones['date'].dt``

DataFrame Cleaning Translate
----------------------------
* Complexity level: easy
* Lines of code to write: 10-15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/df_mapping_substitute.py`

:English:
    #. Download :download:`data/astro-dates.csv`
    #. Set header and index to data from file
    #. Convert Polish month names to English
    #. Parse dates to ``datetime`` objects

:Polish:
    #. Pobierz :download:`data/astro-dates.csv`
    #. Ustaw nagłówek i index na dane zaczytane z pliku
    #. Przekonwertuj polskie nazwy miesięcy na angielskie
    #. Sparsuj daty do obiektów ``datetime``

:Hint:
    * ``df['column'].replace(regex=True)``
    * ``df['column'].apply()``
    * ``pd.Timestamp``

DataFrame Cleaning Substitute
-----------------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/df_mapping_translate.py`

:English:
    #. Download :download:`data/trl.xlsx`
    #. Select ``Polish`` spreadsheet
    #. Set header and index to data from file
    #. Mind the encoding
    #. Substitute Polish Diacritics to English alphabet letters
    #. Compare ``df.replace(regex=True)`` with ``df.applymap()``

:Polish:
    #. Pobierz :download:`data/trl.xlsx`
    #. Wybierz arkusz ``Polish``
    #. Ustaw nagłówek i index na dane zaczytane z pliku
    #. Zwróć uwagę na encoding
    #. Podmień polskie znaki diakrytyczne na litery z alfabetu angielskiego
    #. Porównaj ``df.replace(regex=True)`` z ``df.applymap()``

:Example:
    .. code-block:: text
        :caption: Polish -> English conversion table

        ą: a
        ć: c
        ę: e
        ł: l
        ń: n
        ó: o
        ś: s
        ż: z
        ź: z

:Hint:
        * ``df.set_index()``
        * ``df.applymap()``
        * ``s.map()``

DataFrame Cleaning Month number to text
---------------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/df_mapping_month.py`

:English:
    #. Use data from "Input" section (see below)
    #. Download :download:`data/phones.csv`
    #. Add column ``year`` and ``month_name`` by parsing ``month`` column
    #. Month name must be a string month name, not a number (i.e.: 'January', 'May')

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Pobierz :download:`data/phones.csv`
    #. Dodaj kolumnę ``year`` i ``month_name`` poprzez sparsowanie kolumny ``month``
    #. Nazwa miesiąca musi być ciągiem znaków, a nie liczbą (i.e. 'January', 'May')

:Example:
    #. if ``month`` column is "2015-01"
    #. ``year``: 2015
    #. ``month_name``: January

:Input:
    .. code-block:: text

        1, January
        2, February
        3, March
        4, April
        5, May
        6, June
        7, July
        8, August
        9, September
        10, October
        11, November
        12, December

:Hint:
    * ``Series.str.split()``
    * ``df[ ['A', 'b'] ]``
