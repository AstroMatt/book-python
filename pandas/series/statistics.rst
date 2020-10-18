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
* ``Series.count()`` - Number of non-null observations

.. code-block:: python

    len(s)          # 5
    s.size          # 5
    s.count()       # 4
    s.nunique()     # 4

.. code-block:: python

    s.values_count()
    # 5.0    1
    # 3.0    1
    # 2.0    1
    # 1.0    1
    # dtype: int64


Sum
===
* ``Series.sum()`` - Sum of values
* ``Series.cumsum()`` - Cumulative sum

.. code-block:: python

    s.sum()
    # 11.0

    s.cumsum()
    # a    1.0
    # b    3.0
    # c    6.0
    # d    NaN
    # e    11.0
    # dtype: float64


Product
=======
* ``Series.prod()`` - Product of values
* ``Series.cumprod()`` - Cumulative product

.. code-block:: python

    s.prod()
    # 30.0

    s.cumprod()
    # a    1.0
    # b    2.0
    # c    6.0
    # d    NaN
    # e    30.0
    # dtype: float64


Extremes
========
* ``Series.min()`` - Minimum value
* ``Series.idxmin()`` - Index of minimum value (Float, Int, Object, Datetime, Index)
* ``Series.argmin()`` - Range index of minimum value
* ``Series.cummin()`` - Cumulative minimum
* ``Series.max()`` - Maximum value
* ``Series.idxmax()``  - Index of maximum value (Float, Int, Object, Datetime, Index)
* ``Series.argmax()``  - Range index of maximum value
* ``Series.cummax()``  - Cumulative maximum

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

.. figure:: img/pandas-series-stats-rolling.png
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

.. figure:: img/pandas-series-stats-stdev.png
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

.. figure:: img/pandas-series-stats-sem.png
    :width: 75%
    :align: center

    Standard Error of the Mean (SEM)

.. code-block:: python
    :caption: Skewness (3rd moment)

    s.skew()

.. figure:: img/pandas-series-stats-skew.png
    :width: 75%
    :align: center

    Skewness

.. code-block:: python
    :caption: Kurtosis (4th moment)

    s.kurt()

.. figure:: img/pandas-series-stats-kurt.png
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

.. figure:: img/pandas-series-stats-corr.png
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
.. todo:: Create assignments
