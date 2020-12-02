****************
DataFrame Select
****************


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

.. figure:: img/pandas-dataframe-select.png
    :scale: 80%
    :align: center

    Pandas Select Methods


Rationale
=========
* ``df.where()`` Works with ``inplace=True``
* Use ``df.dropna()`` to remove ``NaN``
* Use ``df.fillna()`` to substitute value for ``NaN``


Query Data
==========
.. code-block:: python

    df[df['Morning'] > 0.0]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

.. code-block:: python

    query = df['Morning'] > 0.0

    df[query]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

.. code-block:: python

    query = df['Morning'] > 0.0

    df.where(query)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01       NaN       NaN       NaN       NaN
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04       NaN       NaN       NaN       NaN
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Logical NOT
===========
.. code-block:: python

    query = df['Midnight'] < 0.0

    df[~query]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674

    df.where(~query)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31       NaN       NaN       NaN       NaN
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03       NaN       NaN       NaN       NaN
    # 2000-01-04       NaN       NaN       NaN       NaN
    # 2000-01-05       NaN       NaN       NaN       NaN


Logical AND
===========
* In first and in second query

.. code-block:: text

    1 & 1 -> 1
    1 & 0 -> 0
    0 & 1 -> 0
    0 & 0 -> 0

.. code-block:: python

    df[ (df['Morning']<0.0) & (df['Midnight']<0.0) ]
    #             Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165

.. code-block:: python

    query = (df['Morning'] < 0.0) & (df['Midnight'] < 0.0)

    df[query]
    #             Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165

.. code-block:: python

    query1 = df['Morning'] < 0.0
    query2 = df['Midnight'] < 0.0

    df[query1 & query2]
    #             Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165

    df.where(query1 & query2)
    #             Morning      Noon   Evening  Midnight
    # 1999-12-30      NaN       NaN       NaN       NaN
    # 1999-12-31      NaN       NaN       NaN       NaN
    # 2000-01-01      NaN       NaN       NaN       NaN
    # 2000-01-02      NaN       NaN       NaN       NaN
    # 2000-01-03      NaN       NaN       NaN       NaN
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165
    # 2000-01-05      NaN       NaN       NaN       NaN


Logical OR
==========
* In first or in second query

.. code-block:: text

    1 | 1 -> 1
    1 | 0 -> 1
    0 | 1 -> 1
    0 | 0 -> 0

.. code-block:: python

    query1 = df['Morning'] < 0.0
    query2 = df['Midnight'] < 0.0

    df[query1 | query2]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.where(query1 | query2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30       NaN       NaN       NaN       NaN
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02       NaN       NaN       NaN       NaN
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Logical XOR
===========
* In first or in second, but not in both queries

.. code-block:: text

    1 ^ 1 -> 0
    1 ^ 0 -> 1
    0 ^ 1 -> 1
    0 ^ 0 -> 0

.. code-block:: python

    query1 = df['Morning'] < 0.0
    query2 = df['Midnight'] < 0.0

    df[query1 ^ query2]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.where(query1 ^ query2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30       NaN       NaN       NaN       NaN
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02       NaN       NaN       NaN       NaN
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04       NaN       NaN       NaN       NaN
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Assignments
===========

DataFrame Select
----------------
* Assignment: DataFrame Select
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 8 min
* Filename: :download:`solution/df_select.py`

English:
    .. todo:: Translate to English

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``iris: pd.DataFrame``
    #. Przefiltruj ``inplace`` kolumnę 'Petal length' i pozostaw wartości powyżej 2.0
    #. Wyświetl 5 pierwszych wierszy

Given:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-clean.csv'
