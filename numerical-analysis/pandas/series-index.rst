************
Series Index
************


Index Types
===========
* Range Index
* Int64 Index
* Float64 Index
* String Index
* Datetime Index

.. code-block:: python

    RangeIndex(start=0, stop=5, step=1)

.. code-block:: python

    Int64Index([0, 1, 2, 3, 4], dtype='int64')

.. code-block:: python

    Float64Index([0.0, 1.1, 2.2, 3.3, 4.4], dtype='float64')

.. code-block:: python

    Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

.. code-block:: python

    DatetimeIndex(['1999-01-28', '1999-01-29', '1999-01-30', '1999-01-31', '1999-02-01'],
                  dtype='datetime64[ns]', freq='D')

.. code-block:: python

    import pandas as pd
    import numpy as np


    DATA = [11, 22, 33, 44, 55]

    # Range Index
    r1 = pd.Series(DATA)
    r2 = pd.Series(DATA, index=range(5))
    r2 = pd.Series(DATA, index=range(len(DATA)))

    # Integer Index
    i1 = pd.Series(DATA, index=[0, 1, 2, 3, 4])
    i2 = pd.Series(DATA, index=np.arange(5))
    i3 = pd.Series(DATA, index=np.arange(len(DATA)))
    i4 = pd.Series(DATA, index=[99, 3, -5, 0, 77])

    # Float Index
    f1 = pd.Series(DATA, index=[0.0, 1.1, 2.2, 3.3, 4.4])
    f2 = pd.Series(DATA, index=np.arange(0.0, 5.5, 1.1)
    f3 = pd.Series(DATA, index=[99.9, 3.14, -5.99, 0.0, 77.1])

    # Object Index
    o1 = pd.Series(DATA, index=['a', 'b', 'c', 'd', 'e'])
    o2 = pd.Series(DATA, index=list('abcde'))
    o3 = pd.Series(DATA, index=list('abcdefghijklmnopqrstuvwz')[:len(DATA)])
    o4 = pd.Series(DATA, index=['aaa', 'baba', 'cac', 'do or not', 'e,c,h,o'])

    # Datetime Index
    d1 = pd.Series(DATA, index=pd.date_range('1999-01-28', periods=len(DATA)))
    d2 = pd.Series(DATA, index=pd.date_range('1999-01-28', periods=len(DATA), freq='D'))
    d3 = pd.Series(DATA, index=[
        pd.Timestamp('1999-01-28'),
        pd.Timestamp('2000-01-01'),
        pd.Timestamp('1961-04-12'),
        pd.Timestamp('1969-07-21'),
        pd.Timestamp('1970-01-01')])


Range Index
===========
* Default

.. code-block:: python
    :caption: Define Range Index

    import pandas as pd


    DATA = [11, 22, 33, 44, 55]

    r1 = pd.Series(DATA)
    r2 = pd.Series(DATA, index=range(5))

    r1.index

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0])

    s.index
    # RangeIndex(start=0, stop=3, step=1)

    s
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # dtype: float64

.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s.index
    # RangeIndex(start=0, stop=3, step=1)

    s
    # 0    a
    # 1    b
    # 2    c
    # dtype: object


Int64 Index
=============
* Int64 Index

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.1, 2.2, 3.3, 4.4],
        index = [9, 1337, -2, 0])

    s.index
    # Int64Index([9, 1337, -2, 0], dtype='int64')

    s
    #  9      1.1
    #  1337   2.2
    # -2      3.3
    #  0      4.4
    # dtype: float64


Float64 Index
=============
* Int64 Index

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.1, 2.2, 3.3, 4.4],
        index = [9.9, 133.7, -2.7, 0.0])

    s.index
    # Float64Index([9.9, 133.7, -2.7, 0.0], dtype='float64')

    s
    #  9.9      1.1
    #  133.7    2.2
    # -2.7      3.3
    #  0.0      4.4
    # dtype: float64


String Index
============
* Also has ``RangeIndex``

.. code-block:: python

    import pandas as pd
    import string

    string.ascii_lowercase
    # 'abcdefghijklmnopqrstuvwxyz'

    s = pd.Series(
        data = [1.1, 2.2, 3.3, 4.4]
        index = list(string.ascii_lowercase)[:4])

    s.index
    # Index(['a', 'b', 'c', 'd'], dtype='object')

    s
    # a    1.1
    # b    2.2
    # c    3.3
    # d    4.4
    # dtype: float64

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['a', 'b', 'c', 'd', 'e'])

    s.index
    # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    4.0
    # e    5.0
    # dtype: float64

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    s = pd.Series(
        data = np.random.randn(3),
        index = list('abc'))

    s.index
    # Index(['a', 'b', 'c'], dtype='object')

    s
    # a    1.764052
    # b    0.400157
    # c    0.978738
    # dtype: float64

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

    s.index
    # Index(['aaa', 'bbb', 'ccc', 'ddd', 'eee'], dtype='object')

    s
    # aaa    1.0
    # bbb    2.0
    # ccc    3.0
    # ddd    4.0
    # eee    5.0
    # dtype: float64


Date Index
==========
* Also has ``RangeIndex``
* Default is "Daily"
* Works also with ISO time format ``1970-01-01T00:00:00``
* ``00:00:00`` is assumed if time is not provided

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01',
    #                '2000-01-02', '2000-01-03'],
    #               dtype='datetime64[ns]', freq='D')

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

.. code-block:: python
    :caption: Every year

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='Y'))

    s.index
    # DatetimeIndex(['1999-12-31', '2000-12-31', '2001-12-31',
    #                '2002-12-31', '2003-12-31'],
    #               dtype='datetime64[ns]', freq='A-DEC')

    s
    # 1999-12-31    1.0
    # 2000-12-31    2.0
    # 2001-12-31    3.0
    # 2002-12-31    4.0
    # 2003-12-31    5.0
    # Freq: A-DEC, dtype: float64

.. code-block:: python
    :caption: Every quarter

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='Q'))

    s.index
    # DatetimeIndex(['1999-12-31', '2000-03-31', '2000-06-30',
    #                '2000-09-30', '2000-12-31'],
    #               dtype='datetime64[ns]', freq='Q-DEC')

    s
    # 1999-12-31    1.0
    # 2000-03-31    2.0
    # 2000-06-30    3.0
    # 2000-09-30    4.0
    # 2000-12-31    5.0
    # Freq: Q-DEC, dtype: float64

.. code-block:: python
    :caption: Every month

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='M'))

    s.index
    # DatetimeIndex(['1999-12-31', '2000-01-31', '2000-02-29',
    #                '2000-03-31', '2000-04-30'],
    #               dtype='datetime64[ns]', freq='M')

    s
    # 1999-12-31    1.0
    # 2000-01-31    2.0
    # 2000-02-29    3.0
    # 2000-03-31    4.0
    # 2000-04-30    5.0
    # Freq: M, dtype: float64

.. code-block:: python
    :caption: Every day

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='D'))

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01',
    #                '2000-01-02', '2000-01-03'],
    #               dtype='datetime64[ns]', freq='D')

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

.. code-block:: python
    :caption: Every two days

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='2D'))

    s.index
    # DatetimeIndex(['1999-12-30', '2000-01-01', '2000-01-03',
    #                '2000-01-05', '2000-01-07'],
    #               dtype='datetime64[ns]', freq='2D')

    s
    # 1999-12-30    1.0
    # 2000-01-01    2.0
    # 2000-01-03    3.0
    # 2000-01-05    4.0
    # 2000-01-07    5.0
    # Freq: 2D, dtype: float64

.. code-block:: python
    :caption: Every hour

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='H'))

    s.index
    # DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 01:00:00',
    #                '1999-12-30 02:00:00', '1999-12-30 03:00:00',
    #                '1999-12-30 04:00:00'],
    #               dtype='datetime64[ns]', freq='H')

    s
    # 1999-12-30 00:00:00    1.0
    # 1999-12-30 01:00:00    2.0
    # 1999-12-30 02:00:00    3.0
    # 1999-12-30 03:00:00    4.0
    # 1999-12-30 04:00:00    5.0
    # Freq: H, dtype: float64

.. code-block:: python
    :caption: Every minute

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='T'))

    s.index
    # DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 00:01:00',
    #                '1999-12-30 00:02:00', '1999-12-30 00:03:00',
    #                '1999-12-30 00:04:00'],
    #               dtype='datetime64[ns]', freq='T')

    s
    # 1999-12-30 00:00:00    1.0
    # 1999-12-30 00:01:00    2.0
    # 1999-12-30 00:02:00    3.0
    # 1999-12-30 00:03:00    4.0
    # 1999-12-30 00:04:00    5.0
    # Freq: T, dtype: float64

.. code-block:: python
    :caption: Every second

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='S'))

    s.index
    # DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 00:00:01',
    #                '1999-12-30 00:00:02', '1999-12-30 00:00:03',
    #                '1999-12-30 00:00:04'],
    #               dtype='datetime64[ns]', freq='S')

    s
    # 1999-12-30 00:00:00    1.0
    # 1999-12-30 00:00:01    2.0
    # 1999-12-30 00:00:02    3.0
    # 1999-12-30 00:00:03    4.0
    # 1999-12-30 00:00:04    5.0
    # Freq: S, dtype: float64

.. code-block:: python
    :caption: Every business day. More in :ref:`Date and Time Frequency` and :ref:`Date and Time Calendar`

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='B'))

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-03',
    #                '2000-01-04', '2000-01-05'],
    #               dtype='datetime64[ns]', freq='B')

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-03    3.0
    # 2000-01-04    4.0
    # 2000-01-05    5.0
    # Freq: B, dtype: float64


Assignments
===========
.. todo:: Create assignments
