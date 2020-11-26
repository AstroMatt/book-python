**************
Series Getitem
**************


Range Index
===========
.. code-block:: python

    import pandas as pd


    s = pd.Series([1.1, 2.2, 3.3, None, 5.5])

    s
    # 0    1.1
    # 1    2.2
    # 2    3.3
    # 3    NaN
    # 4    5.5
    # dtype: float64

    s.index
    # RangeIndex(start=0, stop=5, step=1)

    s[0]        # 1.1
    s[3]        # nan
    s[100]      # KeyError: 100

    s[-1]       # KeyError: -1
    s[-100]     # KeyError: -100


Float and Int Index
===================
.. code-block:: python

    import pandas as pd


    s = pd.Series(
        data = [1.1, 2.2, 3.3, None, 5.5],
        index = [1, 0, 3.3, 99, -1])

    s
    #  1.0     1.1
    #  0.0     2.2
    #  3.3     3.3
    #  99.0    NaN
    # -1.0     5.5
    # dtype: float64

    s.index
    # Float64Index([1.0, 0.0, 3.3, 99.0, -1.0], dtype='float64')

    s[0]        # 2.2
    s[3]        # KeyError: 3
    s[100]      # KeyError: 100

    s[-1]       # 5.5
    s[-100]     # KeyError: -100


String Index
============
.. code-block:: python

    import pandas as pd


    s = pd.Series(
        data = [1.1, 2.2, 3.3, None, 5.5],
        index = ['a', 'b', 'c', 'd', 'e'])

    s
    # a    1.1
    # b    2.2
    # c    3.3
    # d    NaN
    # e    5.5
    # dtype: float64

    s.index
    # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

    s['a']      # 1.1
    s['d']      # nan
    s['e']      # 5.5
    s['x']      # KeyError: 'x'

    s[0]        # 1.1
    s[3]        # nan
    s[100]      # IndexError: index 100 is out of bounds for axis 0 with size 5
    s[-1]       # 5.5
    s[-100]     # IndexError: index -100 is out of bounds for axis 0 with size 5


Date Index
==========
.. code-block:: python

    import pandas as pd


    s = pd.Series(
        data = [1.1, 2.2, 3.3, None, 5.5],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.1
    # 1999-12-31    2.2
    # 2000-01-01    3.3
    # 2000-01-02    NaN
    # 2000-01-03    5.5
    # Freq: D, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01', '2000-01-02', '2000-01-03'],
    #               dtype='datetime64[ns]', freq='D')

    s['2000-01-03']
    # 5.5

    s['2000-01']
    # 2000-01-01    3.3
    # 2000-01-02    NaN
    # 2000-01-03    5.5
    # Freq: D, dtype: float64

    s['1999']
    # 1999-12-30    1.1
    # 1999-12-31    2.2
    # Freq: D, dtype: float64

    s[0]        # 1.1
    s[3]        # nan
    s[100]      # IndexError: index 100 is out of bounds for axis 0 with size 5
    s[-1]       # 5.5
    s[-100]     # IndexError: index -100 is out of bounds for axis 0 with size 5

    s['a']      # KeyError: 'a'


Assignments
===========

Series Getitem
--------------
* Assignment: Series Getitem
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Filename: :download:`solution/series_getitem.py`

English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 100 random numbers from standard normal distribution
    #. Series Index are following dates since 2000
    #. Print values:

        * at 2000-02-29,
        * first value in the series (without using ``.head()``),
        * last value in the series (without using ``.tail()``),
        * middle value in the series.

Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    #. Indeksem w serii mają być kolejne dni od 2000 roku
    #. Wypisz wartości:

        * dnia 2000-02-29,
        * pierwszą wartość w serii (nie używając ``.head()``),
        * ostatnią wartość w serii (nie używając ``.tail()``),
        * środkowa wartość serii.

Hints:
    * ``np.random.seed(0)``
    * ``np.random.randn(10)``
