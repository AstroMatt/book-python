************
DataFrame At
************


* Access a single value for a row/column pair by integer position
* Use iat if you only need to get or set a single value in a DataFrame or Series
* ``iat`` integer at (no fancy indexing)

.. figure:: img/pandas-dataframe-select-cell.png

    Pandas Select Cell

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

Get value at specified row/column pair
--------------------------------------
* First argument is column
* Second argument is row

.. code-block:: python

    df.iat[0,0]
    # 1.764052345967664

    df.iat[1,0]
    # 1.8675579901499675

    df.iat[0,1]
    # 0.4001572083672233

Get value from row
------------------
* ``loc`` returns Series

.. code-block:: python

    df.loc['2000-01-01'].iat[1]
    # 0.41059850193837233

Set value at a position
-----------------------
.. code-block:: python

    df.iat[0,0] = 0.0
    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  0.000000  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Assignments
===========
.. todo:: Create assignments
