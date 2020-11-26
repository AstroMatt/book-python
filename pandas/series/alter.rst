************
Series Alter
************


Drop Rows
=========
* Drop element at index
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0, None, 5.0])

    s.drop(1)
    # 0    1.0
    # 2    3.0
    # 3    NaN
    # 4    5.0
    # dtype: float64

    s.drop([0,2,4])
    # 1    2.0
    # 3    NaN
    # dtype: float64


Drop Duplicates
===============
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 2.0, None, 5.0])

    s.drop_duplicates()
    # 0    1.0
    # 1    2.0
    # 3    NaN
    # 4    5.0
    # dtype: float64


Reset Index
===========
* Works with ``inplace=True``
* ``drop=True`` prevents the old index being added as a column

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0, None, 5.0])

    s.drop([0,1], inplace=True)
    # 2    3.0
    # 3    NaN
    # 4    5.0
    # dtype: float64

    s.reset_index()
    #    index    0
    # 0      2  3.0
    # 1      3  NaN
    # 2      4  5.0

    s.reset_index(drop=True, inplace=True)
    # 0    3.0
    # 1    NaN
    # 2    5.0
    # dtype: float64


Assignments
===========

Series Alter
------------
* Assignment: Series Alter
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/series_alter.py`

English:
    #. Use data from "Given" section (see below)
    #. From input data create ``pd.Series``
    #. Drop values at index 2, 4, 6
    #. Drop duplicates
    #. Reindex series (without old copy)
    #. Print series

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Z danych wejściowych stwórz ``pd.Series``
    #. Usuń wartości na indeksach 2, 4, 6
    #. Usuń duplikujące się wartości
    #. Zresetuj indeks (bez kopii starego)
    #. Wypisz serię

Given:
    .. code-block:: python

        DATA = [1, None, 5, None, 1, 2, 1]

Tests:
    .. code-block:: python

        s: pd.Series
        # 0    1.0
        # 1    NaN
        # 2    2.0
        # dtype: float64
