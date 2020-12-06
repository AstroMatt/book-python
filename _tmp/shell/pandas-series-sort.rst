***********
Series Sort
***********


Sort Values
===========
.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [99.9, 3.14, -5.99, 0.0, 77.1],
        index = [0, 99, 6, -4, 2])

    s.sort_values()
    #  6     -5.99
    # -4      0.00
    #  99     3.14
    #  2     77.10
    #  0     99.90
    # dtype: float64

    s.sort_values(ascending=False)
    #  0     99.90
    #  2     77.10
    #  99     3.14
    # -4      0.00
    #  6     -5.99
    # dtype: float64


Sort Index
==========
.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [99.9, 3.14, -5.99, 0.0, 77.1],
        index = [0, 99, 6, -4, 2])

    s.sort_index()
    # -4      0.00
    #  0     99.90
    #  2     77.10
    #  6     -5.99
    #  99     3.14
    # dtype: float64

    s.sort_index(ascending=False)
    #  99     3.14
    #  6     -5.99
    #  2     77.10
    #  0     99.90
    # -4      0.00
    # dtype: float64


Assignments
===========
.. todo:: Create assignments
