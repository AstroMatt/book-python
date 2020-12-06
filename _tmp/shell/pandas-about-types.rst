************
Types Basics
************


Series
======
* 1-dimensional data structure similar to ``ndarray``
* Has index
* Can have name

.. code-block:: python

    import pandas as pd


    pd.Series([1.0, 2.0, 3.0, 4.0])
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64


DataFrame
=========
* 2-dimensional object
* All columns share the same index
* List of ``Series``
* Each column must have name
* Operations can be executed on columns or rows

.. code-block:: python

    import pandas as pd


    pd.DataFrame({
        'A': ['a', 'b', 'c', 'd'],
        'B': [11, 22, 33, 44],
        'C': [1.1, 2.2, 3.3, 4.4],
    })
    #    A   B    C
    # 0  a  11  1.1
    # 1  b  22  2.2
    # 2  c  33  3.3
    # 3  d  44  4.4


SparseArray
===========
* Data where a single value is repeated many times (e.g. ``0`` or ``NaN``) may be stored efficiently as a ``SparseArray``

.. code-block:: python
    :caption: Sparse data with Series

    import pandas as pd


    pd.arrays.SparseArray([1, None, None, None, 3])
    # [1.0, nan, nan, nan, 3.0]
    # Fill: nan
    # IntIndex
    # Indices: array([0, 4], dtype=int32)

.. code-block:: python
    :caption: Sparse data with DataFrame

    import pandas as pd


    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': pd.arrays.SparseArray([None, None, None])})

    #    A   B
    # 0  1 NaN
    # 1  2 NaN
    # 2  3 NaN

    df.dtypes
    # A                  int64
    # B    Sparse[object, nan]
    # dtype: object


Interval
========
.. code-block:: python
    :caption: Definition

    import pandas as pd


    pd.Interval(0, 5)
    # Interval(0, 5, closed='right')

    pd.Interval(left=0, right=5)
    # Interval(0, 5, closed='right')

    pd.Interval(left=0, right=5, closed='both')
    # Interval(0, 5, closed='both')

.. code-block:: python
    :caption: Contains

    import pandas as pd


    interval = pd.Interval(0, 5, closed='left')

    2.5 in interval
    # True

    5.0 in interval
    # False

.. code-block:: python
    :caption: Interval between Timestamps

    import pandas as pd


    year_1970 = pd.Interval(left=pd.Timestamp('1970-01-01 00:00:00'),
                            right=pd.Timestamp('1971-01-01 00:00:00'),
                            closed='left')

    apollo11 = pd.Timestamp('1969-07-16')
    apollo13 = pd.Timestamp('1970-04-11')

    apollo11 in year_1970
    # False

    apollo13 in year_1970
    # True

    year_1970.length
    # Timedelta('365 days 00:00:00')

.. code-block:: python

    import pandas as pd

    fiscalyear2020 = pd.Interval(
        left=pd.Timestamp('2020-01-01'),
        right=pd.Timestamp('2021-01-01'),
        closed='left')

    fiscalyear2021 = pd.Interval(
        left=pd.Timestamp('2021-01-01'),
        right=pd.Timestamp('2022-01-01'),
        closed='left')


    event1 = pd.Timestamp('2020-04-12')
    event2 = pd.Timestamp('2021-07-21')

    event1 in fiscalyear2020    # True
    event1 in fiscalyear2021    # False
    event2 in fiscalyear2020    # False
    event2 in fiscalyear2021    # True


Categorical
===========
* Limited, fixed set of values

.. code-block:: python

    import pandas as pd


    iris = pd.Categorical(['setosa', 'virginica', 'versicolor'])
    # [setosa, virginica, versicolor]
    # Categories (3, object): [setosa, versicolor, virginica]

    'arctica' in iris
    # False

.. code-block:: python

    import pandas as pd


    status = pd.Categorical(['todo', 'done', 'todo', 'done'])
    # [todo, done, todo, done]
    # Categories (2, object): [done, todo]

    'in progress' in status
    # False

    'todo' in status
    # True

    status.categories
    # Index(['done', 'todo'], dtype='object')

.. code-block:: python

    import pandas as pd


    moon_landings = pd.Categorical(['apollo11', 'apollo12', 'apollo14', 'apollo15', 'apollo16', 'apollo17'])
    # [apollo11, apollo12, apollo14, apollo15, apollo16, apollo17]
    # Categories (6, object): [apollo11, apollo12, apollo14, apollo15, apollo16, apollo17]

    'apollo11' in moon_landings
    # True

    'apollo13' in moon_landings
    # False

    moon_landings.categories
    # Index(['apollo11', 'apollo12', 'apollo14', 'apollo15', 'apollo16', 'apollo17'], dtype='object')
