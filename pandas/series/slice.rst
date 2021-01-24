**************
Series Slicing
**************


Numeric Index
=============
.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])

    s
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # dtype: float64

    s[:2]
    # 0    1.0
    # 1    2.0
    # dtype: float64

    s[2:]
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # dtype: float64

    s[1:-2]
    # 1    2.0
    # 2    3.0
    # dtype: float64

    s[::2]
    # 0    1.0
    # 2    3.0
    # 4    5.0
    # dtype: float64

    s[1::2]
    # 1    2.0
    # 3    4.0
    # dtype: float64


String Index
============
* Using string index upper and lower bound are inclusive!
* String indexes has also numeric index underneath

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['a', 'b', 'c', 'd', 'e'])

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    4.0
    # e    5.0
    # dtype: float64

    s['a':'d']
    # a    1.0
    # b    2.0
    # c    3.0
    # d    4.0
    # dtype: float64

    s['a':'d':2]
    # a    1.0
    # c    3.0
    # dtype: float64

    s['a':'d':'b']
    # Traceback (most recent call last):
    # TypeError: '>=' not supported between instances of 'str' and 'int'

    s['d':'a']
    # Series([], dtype: float64)

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['a', 'b', 'c', 'd', 'e'])

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    4.0
    # e    5.0
    # dtype: float64

    s[:2]
    # a    1.0
    # b    2.0
    # dtype: float64

    s[2:]
    # c    3.0
    # d    4.0
    # e    5.0
    # dtype: float64

    s[1:-2]
    # b    2.0
    # c    3.0
    # dtype: float64

    s[::2]
    # a    1.0
    # c    3.0
    # e    5.0
    # dtype: float64

    s[1::2]
    # b    2.0
    # d    4.0
    # dtype: float64

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

    s
    # aaa    1.0
    # bbb    2.0
    # ccc    3.0
    # ddd    4.0
    # eee    5.0
    # dtype: float64

    s['a':'b']
    # aaa    1.0
    # dtype: float64

    s['a':'c']
    # aaa    1.0
    # bbb    2.0
    # dtype: float64


Date Index
==========
.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s['2000-01-02':'2000-01-04']
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s['1999-12-30':'2000-01-04':2]
    # 1999-12-30    1.0
    # 2000-01-01    3.0
    # 2000-01-03    5.0
    # Freq: 2D, dtype: float64

    s['1999-12-30':'2000-01-04':-1]
    # Series([], Freq: -1D, dtype: float64)

    s['2000-01-04':'1999-12-30':-1]
    # 2000-01-03    5.0
    # 2000-01-02    4.0
    # 2000-01-01    3.0
    # 1999-12-31    2.0
    # 1999-12-30    1.0
    # Freq: -1D, dtype: float64

    s[:'1999']
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # Freq: D, dtype: float64

    s['2000':]
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s[:'1999-12']
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # Freq: D, dtype: float64

    s['2000-01':]
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s[:'2000-01-02']
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # Freq: D, dtype: float64

    s['2000-01-02':]
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s['1999-12':'1999-12']
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # Freq: D, dtype: float64

    s['2000-01':'2000-01-05']
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s[:'2000-01-05':2]
    # 1999-12-30    1.0
    # 2000-01-01    3.0
    # 2000-01-03    5.0
    # Freq: 2D, dtype: float64

    s[:'2000-01-03':-1]
    # 2000-01-03    5.0
    # Freq: -1D, dtype: float64

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0

    s[1:3]
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # Freq: D, dtype: float64

    s[:3]
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # Freq: D, dtype: float64

    s[:3:2]
    # 1999-12-30    1.0
    # 2000-01-01    3.0
    # Freq: 2D, dtype: float64

    s[::-1]
    # 2000-01-03    5.0
    # 2000-01-02    4.0
    # 2000-01-01    3.0
    # 1999-12-31    2.0
    # 1999-12-30    1.0
    # Freq: -1D, dtype: float64


Assignments
===========

.. todo:: Convert assignments to literalinclude

Series Slice Datetime
---------------------
* Assignment: Series Slice Datetime
* Filename: :download:`assignments/series_slice_datetime.py`
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Create ``pd.Series`` with 100 random numbers from standard distribution
    3. Series Index are following dates since 2000
    4. Slice dates from 2000-02-14 to end of February 2000
    5. Compare result with "Tests" section (see below)

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    3. Indeksem w serii mają być kolejne dni od 2000 roku
    4. Wytnij daty od 2000-02-14 do końca lutego 2000
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: python

        s: pd.Series
        # 2000-02-14   -0.509652
        # 2000-02-15   -0.438074
        # 2000-02-16   -1.252795
        # 2000-02-17    0.777490
        # 2000-02-18   -1.613898
        # 2000-02-19   -0.212740
        # 2000-02-20   -0.895467
        # 2000-02-21    0.386902
        # 2000-02-22   -0.510805
        # 2000-02-23   -1.180632
        # 2000-02-24   -0.028182
        # 2000-02-25    0.428332
        # 2000-02-26    0.066517
        # 2000-02-27    0.302472
        # 2000-02-28   -0.634322
        # 2000-02-29   -0.362741
        # Freq: D, dtype: float64

Hints:
    * ``np.random.seed(0)``
    * ``np.random.randn(10)``

Slicing Slice Str
-----------------
* Assignment: Slicing Slice Str
* Filename: :download:`assignments/series_slice_str.py`
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create ``pd.Series`` with 26 random integers in range ``[10, 100)``
    3. Name indexes like letters from ASCII alphabet (``ascii_lowercase: str``)
    4. Find middle letter of alphabet
    5. Slice from series 3 elements up and down from middle
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz ``pd.Series`` z 26 losowymi liczbami całkowitymi z przedziału ``<10; 100)``
    3. Nazwij indeksy jak kolejne litery alfabetu ASCII (``ascii_lowercase: str``)
    4. Znajdź środkową literę alfabetu
    5. Wytnij z serii po 3 elementy w górę i w dół od wyszukanego środka
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

Tests:
    .. code-block:: python

        s: pd.Series
        # j    97
        # k    80
        # l    98
        # m    98
        # n    22
        # o    68
        # p    75
        # dtype: int64

Hints:
    * ``np.random.randint(..., ..., size=...)``
