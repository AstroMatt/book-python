************
DataFrame At
************


* Access a single value for a row/column pair by integer position
* Use iat if you only need to get or set a single value in a DataFrame or Series
* ``iat`` integer at (bez where i innych bajerów)

.. code-block:: python

    import numpy as np
    import pandas as pd
    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

Get value at specified row/column pair
--------------------------------------
* First argument is column
* Second argument is row

.. code-block:: python

    df.iat[0, 0]
    # -0.728881431659923

    df.iat[1, 0]
    # 1.2427906060319527

    df.iat[0, 1]
    # 2.4525672341751084

Set value at specified row/column pair
--------------------------------------
.. code-block:: python

    df.iat[0, 0] = 0.0
    df.iat[0, 0]
    # 0.0

Get value within a series
-------------------------
* ``loc`` returns Series

.. code-block:: python

    df.loc['1970-01-01'].iat[1]
    # 2.4525672341751084


Assignments
===========
.. todo:: Create assignments
