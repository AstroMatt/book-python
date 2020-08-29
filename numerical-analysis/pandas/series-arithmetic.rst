*****************
Series Arithmetic
*****************


Vectorized Operations
=====================
* ``a + 2``,  ``s.add(2)``
* ``s - 2``,  ``s.sub(2)``, ``s.subtract(2)``
* ``s * 2``,  ``s.mul(2)``, ``s.multiply(2)``
* ``s / 2``,  ``s.div(2)``, ``s.divide()``
* ``s // 2``, ``s.truediv(2)``
* ``s % 2``,  ``s.mod(2)``
* ``s ** 2``, ``s.pow(2)``
* ``s ** (1/2)``, ``s.pow(1/2)``
* ``divmod(s, /)``, ``s.divmod(2)``

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series(
        data = [1.0, 2.0, 3.0, np.nan, 5.0],
        index = ['a', 'b', 'c', 'd', 'e'])

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    NaN
    # e    5.0
    # dtype: float64

.. code-block:: python

    s * 5
    # a     5.0
    # b    10.0
    # c    15.0
    # d     NaN
    # e    25.0
    # dtype: float64

.. code-block:: python

    s ** 2
    # a    1.0
    # b    4.0
    # c    9.0
    # d    NaN
    # e    25.0
    # dtype: float64

.. code-block:: python

    s ** 3
    # a     1.0
    # b     8.0
    # c    27.0
    # d     NaN
    # e   125.0
    # dtype: float64


Broadcasting
============
* Uses inner join
* ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

.. code-block:: python

    import pandas as pd
    import numpy as np

    a = pd.Series(
        data = [1.0, 2.0, 3.0, np.nan],
        index = ['a', 'b', 'c', 'd'])

    a
    # a    1.0
    # b    2.0
    # c    3.0
    # d    NaN
    # dtype: float64

    b = pd.Series(
        data = [10.0, np.nan, 12.0, np.nan],
        index = ['a', 'b', 'x', 'y'])

    b
    # a    10.0
    # b    NaN
    # x    12.0
    # y    NaN
    # dtype: float64

.. code-block:: python

    a + b
    # a    11.0
    # b    NaN
    # c    NaN
    # d    NaN
    # x    NaN
    # y    NaN
    # dtype: float64

.. code-block:: python
    :caption: ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

    a.add(b, fill_value=0)
    # a    11.0
    # b     2.0
    # c     3.0
    # d     NaN
    # x    12.0
    # y     NaN
    # dtype: float64


Assignments
===========

Series Arithmetic
-----------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/series_arithmetic.py`

:English:
    #. Set random seed to zero
    #. Generate ``data: ndarray`` with 5 random digits [0, 9]
    #. Create ``index: list`` with index names as sequential letters in english alphabet
    #. Create ``s: pd.Series`` from ``data`` and ``index``
    #. Multiply ``s`` by 10
    #. Multiply ``s`` by original ``s`` values (before multiplying by 10)

:Polish:
    #. Ustaw random ziarno losowości na zero
    #. Wygeneruj ``data: np.ndarray`` z 5 losowymi cyframi <0, 9>
    #. Stwórz ``index: list`` z indeksami jak kolejne listery alfabetu angielskiego
    #. Stwórz ``s: pd.Series`` z ``data`` oraz ``index``
    #. Pomnóż ``s`` przez 10
    #. Pomnóż ``s`` przez oryginalne wartości ``s`` (przed mnożeniem przez 10)
