*****************
Series Statistics
*****************


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


Count
=====
.. code-block:: python

    s.size
    # 5

.. code-block:: python
    :caption: Number of non-null observations

    s.count()
    # 4

.. code-block:: python

    s.values_count()
    # 5.0    1
    # 3.0    1
    # 2.0    1
    # 1.0    1
    # dtype: int64

.. code-block:: python

    s.nunique()
    # 4


Sum
===
.. code-block:: python
    :caption: Sum of values

    s.sum()
    # 11.0

.. code-block:: python
    :caption: Cumulative sum

    s.cumsum()
    # a    1.0
    # b    3.0
    # c    6.0
    # d    NaN
    # e    11.0
    # dtype: float64


Product
=======
.. code-block:: python
    :caption: Product of values

    s.prod()
    # 30.0

.. code-block:: python
    :caption: Cumulative product

    s.cumprod()
    # a    1.0
    # b    2.0
    # c    6.0
    # d    NaN
    # e    30.0
    # dtype: float64


Extremes
========
.. code-block:: python
    :caption: Minimum, index of minimum and cumulative minimum

    s.min()
    # 1.0

    s.idxmin()
    # 'a'

    s.argmin()
    # 0

    s.cummin()
    # a    1.0
    # b    1.0
    # c    1.0
    # d    NaN
    # e    1.0
    # dtype: float64

.. code-block:: python
    :caption: Maximum, index of maximum and cumulative maximum

    s.max()
    # 5.0

    s.idxmax()
    # 'e'

    s.argmax()
    # 4

    s.cummax()
    # a    1.0
    # b    2.0
    # c    3.0
    # d    NaN
    # e    5.0
    # dtype: float64


Average
=======
.. code-block:: python
    :caption: Arithmetic mean of values

    s.mean()
    # 2.75

.. code-block:: python
    :caption: Arithmetic median of values

    s.median()
    # 2.5

.. code-block:: python
    :caption: Mode

    s.mode()
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    5.0
    # dtype: float64

.. code-block:: python
    :caption: Rolling Average

    s.rolling(window=2).mean()
    # a    NaN
    # b    1.5
    # c    2.5
    # d    NaN
    # e    NaN
    # dtype: float64

.. figure:: img/stats-rolling.png
    :width: 75%
    :align: center

    Rolling Average


Distribution
============
.. code-block:: python
    :caption: Absolute value

    s.abs()
    # a    1.0
    # b    2.0
    # c    3.0
    # d    NaN
    # e    5.0
    # dtype: float64

.. code-block:: python
    :caption: Standard deviation

    s.std()
    # 1.707825127659933

.. figure:: img/stats-stdev.png
    :width: 75%
    :align: center

    Standard Deviation

.. code-block:: python
    :caption: Mean absolute deviation

    s.mad()
    # 1.25

.. code-block:: python
    :caption: Standard Error of the Mean (SEM)

    s.sem()
    # 0.8539125638299665

.. figure:: img/stats-sem.png
    :width: 75%
    :align: center

    Standard Error of the Mean (SEM)

.. code-block:: python
    :caption: Skewness (3rd moment)

    s.skew()

.. figure:: img/stats-skew.png
    :width: 75%
    :align: center

    Skewness

.. code-block:: python
    :caption: Kurtosis (4th moment)

    s.kurt()

.. figure:: img/stats-kurt.png
    :width: 75%
    :align: center

    Kurtosis

.. code-block:: python
    :caption: Sample quantile (value at %). Quantile also known as Percentile.

    s.quantile(.3)
    # 1.9

    s.quantile([.25, .5, .75])
    # 0.25    1.75
    # 0.50    2.50
    # 0.75    3.50
    # dtype: float64

.. code-block:: python
    :caption: Variance

    s.var()
    # 2.9166666666666665

.. code-block:: python
    :caption: Correlation Coefficient

    s.corr(s)
    # 1.0

.. figure:: img/stats-corr.png
    :width: 75%
    :align: center

    Correlation Coefficient

Describe
========
.. code-block:: python

    s.describe()
    # count    4.000000
    # mean     2.750000
    # std      1.707825
    # min      1.000000
    # 25%      1.750000
    # 50%      2.500000
    # 75%      3.500000
    # max      5.000000
    # dtype: float64


Assignments
===========
.. todo:: Create Assignments
