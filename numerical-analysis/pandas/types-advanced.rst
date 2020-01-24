**************
Types Advanced
**************


SparseArray
===========
* Data where a single value is repeated many times (e.g. ``0`` or ``NaN``) may be stored efficiently as a ``SparseArray``

Sparse data with Series
-----------------------
.. code-block:: python

    import pandas as pd

    sa = pd.SparseArray([1, 2, 3])
    # [1, 2, 3]
    # Fill: 0
    # IntIndex
    # Indices: array([0, 1, 2], dtype=int32)

Sparse data with DataFrame
--------------------------
.. code-block:: python

    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': pd.SparseArray([np.nan, np.nan, np.nan])})

    #    A   B
    # 0  1 NaN
    # 1  2 NaN
    # 2  3 NaN

    df.dtypes
    # A                   int64
    # B    Sparse[float64, nan]
    # dtype: object


Interval
========

Definition
----------
.. code-block:: python

    import pandas as pd


    pd.Interval(0, 5)
    # Interval(0, 5, closed='right')

    pd.Interval(left=0, right=5)
    # Interval(0, 5, closed='right')

    pd.Interval(left=0, right=5, closed='both')
    # Interval(0, 5, closed='both')

Contains
--------
.. code-block:: python

    import pandas as pd


    interval = pd.Interval(0, 5, closed='left')

    2.5 in interval
    # True

    5.0 in interval
    # False

Interval between Timestamps
---------------------------
.. code-block:: python

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


    moon_landings = pd.Categorical(['apollo11', 'apollo12', 'apollo14', 'apollo15', 'apollo16', 'apollo17'])
    # [apollo11, apollo12, apollo14, apollo15, apollo16, apollo17]
    # Categories (6, object): [apollo11, apollo12, apollo14, apollo15, apollo16, apollo17]

    'apollo11' in moon_landings
    # True

    'apollo13' in moon_landings
    # False

    moon_landings.categories
    # Index(['apollo11', 'apollo12', 'apollo14', 'apollo15', 'apollo16', 'apollo17'], dtype='object')


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
