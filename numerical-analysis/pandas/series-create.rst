*************
Series Create
*************


From Python sequence
====================
* ``list``
* ``tuple``
* ``set``
* ``frozenset``

.. code-block:: python

    import pandas as pd
    import numpy as np


    pd.Series([1, 2, 3, 4])
    # 0    1
    # 1    2
    # 2    3
    # 3    4
    # dtype: int64

    pd.Series([1., 2., 3., 4.])
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64

    pd.Series([1, 2, None, 4])
    # 0    1.0
    # 1    2.0
    # 2    NaN
    # 3    4.0
    # dtype: float64

    pd.Series(['a', 'b', 'c', 'd'])
    # 0    a
    # 1    b
    # 2    c
    # 3    d
    # dtype: object

.. code-block:: python

    import pandas as pd

    list('abcd')
    # ['a', 'b', 'c', 'd']

    pd.Series(list('abcd'))
    # 0    a
    # 1    b
    # 2    c
    # 3    d
    # dtype: object


From Python range
=================
.. code-block:: python

    import pandas as pd

    pd.Series(range(4))
    # 0    0
    # 1    1
    # 2    2
    # 3    3
    # dtype: int64


From Numpy ``ndarray``
======================
.. code-block:: python

    import pandas as pd
    import numpy as np

    pd.Series(np.arange(4.0))
    # 0    0.0
    # 1    1.0
    # 2    2.0
    # 3    3.0
    # dtype: float64


From Date Range
===============
* From ``pd.Timestamp``
* From ``pd.date_range()``
* Read more in :ref:`Date and Time Types`

.. code-block:: python

    import pandas as pd


    pd.Series(pd.date_range(start='1969-07-16', end='1969-07-24'))
    # 0   1969-07-16
    # 1   1969-07-17
    # 2   1969-07-18
    # 3   1969-07-19
    # 4   1969-07-20
    # 5   1969-07-21
    # 6   1969-07-22
    # 7   1969-07-23
    # 8   1969-07-24
    # dtype: datetime64[ns]


Length
======
.. code-block:: python

    import pandas as pd

    s = pd.Series([1, 2, 3, 4])

    len(s)
    # 9


Assignments
===========

Series Create Float
-------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/series_create_float.py`
* Last update: 2020-10-01

:English:
    #. Create ``pd.Series`` with 5 float numbers
    #. One of those values must be ``None``

:Polish:
    #. Stwórz ``pd.Series`` z 5 liczbami zmiennoprzecinkowymi
    #. Jedną z tych wartości musi być ``None``

Series Create Randint
---------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/series_create_randint.py`
* Last update: 2020-10-01

:English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 10 random digits (``int`` from ``0`` to ``9``)

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 10 losowymi cyframi  (``int`` from ``0`` to ``9``)

Series Create Even
------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/series_create_even.py`
* Last update: 2020-10-01

:English:
    #. Create ``pd.Series`` with 10 even numbers

:Polish:
    #. Stwórz ``pd.Series`` z 10 liczbami parzystymi

Series Create Dates
-------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/series_create_dates.py`
* Last update: 2020-10-01

:English:
    #. Gagarin flown to space on 1961-04-12
    #. Armstrong set foot on the Moon on 1969-07-21
    #. Create ``pd.Series`` with days between Gagarin's launch and Armstrong's first step
    #. How many days passed?

:Polish:
    #. Gagarin poleciał w kosmos w 1961-04-12
    #. Armstrong postawił stopę na Księżycu w 1969-07-21
    #. Stwórz ``pd.Series`` z dniami pomiędzy startem Gagarina a pierwszym krokiem Armstronga
    #. Jak wiele dni upłynęło?
