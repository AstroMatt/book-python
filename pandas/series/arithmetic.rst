*****************
Series Arithmetic
*****************


Vectorized Operations
=====================
* ``s + 2``,  ``s.add(2)``, ``s.__add__(2)``
* ``s - 2``,  ``s.sub(2)``, ``s.subtract(2)``, ``s.__sub__(2)``
* ``s * 2``,  ``s.mul(2)``, ``s.multiply(2)``, ``s.__mul__(2)``
* ``s ** 2``, ``s.pow(2)``, ``s.__pow__(2)``
* ``s ** (1/2)``, ``s.pow(1/2)``, ``s.__sub__(1/2)``
* ``s / 2``,  ``s.div(2)``, ``s.divide()``, ``s.__div__(2)``
* ``s // 2``, ``s.truediv(2)``, ``s.__truediv__(2)``
* ``s % 2``,  ``s.mod(2)``, ``s.__mod__(2)``
* ``divmod(s, 2)``, ``s.divmod(2)``, ``s.__divmod__(2)``, ``(s//2, s%2)``

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series(
        data = [1.1, 2.2, np.nan, 4.4],
        index = ['a', 'b', 'c', 'd'])

    s
    # a    1.1
    # b    2.2
    # c    NaN
    # d    4.4
    # dtype: float64

.. code-block:: python

    s + 2
    # a    3.1
    # b    4.2
    # c    NaN
    # d    6.4
    # dtype: float64

.. code-block:: python

    s ** 2
    # a     1.21
    # b     4.84
    # c      NaN
    # d    19.36
    # dtype: float64

.. code-block:: python

    s ** (1/2)
    # a    1.048809
    # b    1.483240
    # c         NaN
    # d    2.097618
    # dtype: float64


Broadcasting
============
* Uses inner join
* ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

.. code-block:: python

    import pandas as pd


    a = pd.Series([1, 2, 3])
    b = pd.Series([4, 5, 6])

    a + b
    # 0    5
    # 1    7
    # 2    9
    # dtype: int64

.. code-block:: python

    import pandas as pd


    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([4, 5, 6])

    a + b
    # 0    5.0
    # 1    7.0
    # 2    9.0
    # 3    NaN
    # dtype: float64

.. code-block:: python

    import pandas as pd

    a = pd.Series([1, 2, 3])
    b = pd.Series([4, 5, 6, 7])

    a + b
    # 0    5.0
    # 1    7.0
    # 2    9.0
    # 3    NaN
    # dtype: float64

.. code-block:: python

    import pandas as pd

    a = pd.Series([1, 2, None])
    b = pd.Series([4, 5, 6])

    a + b
    # 0    5.0
    # 1    7.0
    # 2    NaN
    # dtype: float64

.. code-block:: python

    import pandas as pd

    a = pd.Series([1, 2, None])
    b = pd.Series([4, 5, None])

    a + b
    # 0    5.0
    # 1    7.0
    # 2    NaN
    # dtype: float64

.. code-block:: python

    import pandas as pd

    a = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'])
    b = pd.Series(data=[4, 5, 6], index=['a', 'b', 'x'])

    a + b
    # a    5.0
    # b    7.0
    # c    NaN
    # x    NaN
    # dtype: float64

.. code-block:: python
    :caption: ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

    a = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'])
    b = pd.Series(data=[4, 5, 6], index=['a', 'b', 'x'])

    a.add(b, fill_value=0)
    # a    5.0
    # b    7.0
    # c    3.0
    # x    6.0
    # dtype: float64


Assignments
===========

.. todo:: Convert assignments to literalinclude

Series Arithmetic
-----------------
* Assignment: Series Arithmetic
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min
* Filename: :download:`assignments/series_arithmetic.py`

English:
    #. Set random seed to zero
    #. Generate ``data: ndarray`` with 5 random digits [0, 9]
    #. Create ``index: list`` with index names as sequential letters in english alphabet
    #. Create ``s: pd.Series`` from ``data`` and ``index``
    #. Multiply ``s`` by 10
    #. Multiply ``s`` by original ``s`` values (before multiplying by 10)

Polish:
    #. Ustaw random ziarno losowości na zero
    #. Wygeneruj ``data: np.ndarray`` z 5 losowymi cyframi <0, 9>
    #. Stwórz ``index: list`` z indeksami jak kolejne listery alfabetu angielskiego
    #. Stwórz ``s: pd.Series`` z ``data`` oraz ``index``
    #. Pomnóż ``s`` przez 10
    #. Pomnóż ``s`` przez oryginalne wartości ``s`` (przed mnożeniem przez 10)
