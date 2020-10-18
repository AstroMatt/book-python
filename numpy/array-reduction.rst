***************
Array Reduction
***************


Sum
===
* ``a.sum()``
* ``np.sum()``
* ``np.nansum()``

.. code-block:: python

    import numpy as np


    a = np.array([[1.1, 2.2, 3.3],
                  [4.4, 5.5, 6.6]])

    a.sum()
    # 23.1

    a.sum(axis=0)
    # array([5.5, 7.7, 9.9])

    a.sum(axis=1)
    # array([ 6.6, 16.5])

    np.sum(a)
    # 23.1

.. code-block:: python

    import numpy as np


     a = np.array([[1.1, 2.2, 3.3],
                   [4.4, np.nan, 6.6]])

    a.sum()
    # nan

    np.sum(a)
    # nan

    np.nansum(a)
    # 17.6


Cumulative Sum
==============
* ``a.cumsum()``
* ``np.cumsum()``
* ``np.nancumsum()``

.. code-block:: python

    import numpy as np


    a = np.array([[1.1, 2.2, 3.3],
                  [4.4, 5.5, 6.6]])

    a.cumsum()
    # array([ 1.1,  3.3,  6.6, 11. , 16.5, 23.1])

    np.cumsum(a)
    # array([ 1.1,  3.3,  6.6, 11. , 16.5, 23.1])

.. code-block:: python

    import numpy as np


    a = np.array([[1.1, 2.2, 3.3],
                   [4.4, np.nan, 6.6]])

    a.cumsum()
    # array([ 1.1,  3.3,  6.6, 11. ,  nan,  nan])

    np.cumsum(a)
    # array([ 1.1,  3.3,  6.6, 11. ,  nan,  nan])

    np.nancumsum(a)
    # array([ 1.1,  3.3,  6.6, 11. , 11. , 17.6])


Product
=======
* ``a.prod()``
* ``np.prod()``
* ``np.nanprod()``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.prod()
    # 720


Cumulative Product
==================
* ``a.cumprod()``
* ``np.cumprod()``
* ``np.nancumprod()``


Mean
====
* ``a.mean()``
* ``np.mean()``
* ``np.nanmean()``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.mean()
    # 3.5

    a.mean(axis=0)
    # array([2.5, 3.5, 4.5])

    a.mean(axis=1)
    # array([2., 5.])


Cumulative Mean
===============
* ``a.cummean()``
* ``np.cummean()``
* ``np.nancummean()``

Variance
========
* ``a.var()``
* ``np.var()``
* ``np.nanvar()``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.var()
    # 2.9166666666666665

    a.var(axis=0)
    # array([2.25, 2.25, 2.25])

    a.var(axis=1)
    # array([0.66666667, 0.66666667])


Standard Deviation
==================
* ``a.std()``
* ``np.std()``
* ``np.nanstd()``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.std()
    # 1.707825127659933

    a.std(axis=0)
    # array([1.5, 1.5, 1.5])

    a.std(axis=1)
    # array([0.81649658, 0.81649658])


Minimal Value
=============
* ``np.ndarray.argmin()`` index of an ``np.ndarray.min()`` element in array
* ``np.nanmin()``
* ``np.nanargmin()``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.min()
    # 1

    a.min(axis=0)
    # array([1, 2, 3])

    a.min(axis=1)
    # array([1, 4])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.argmin()
    # 0

    a.argmin(axis=0)
    # array([0, 0, 0])

    a.argmin(axis=1)
    # array([0, 0])

.. code-block:: python

    import numpy as np

    a = np.array([[99,   2, 33],
                  [22,   0,  4],
                  [4,  155,  6]])

    a.min()             # 0
    a.min(axis=0)       # array([4, 0, 4])
    a.min(axis=1)       # array([2, 0, 4])
    a.min(axis=-1)      # array([2, 0, 4])

    a.argmin()          # 4
    a.argmin(axis=0)    # array([2, 1, 1])
    a.argmin(axis=1)    # array([1, 1, 0])
    a.argmin(axis=-1)   # array([1, 1, 0])

    a.flat[4]                               # 0
    np.unravel_index(4, (3, 3))             # (1, 1)
    np.unravel_index(a.argmin(), a.shape)   # (1, 1)

.. code-block:: python
    :caption: Shows the coordinates of ``argmin`` value

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.min()
    # 1

    a.argmin()
    # 0

    np.unravel_index(a.argmin(), a.shape)
    # (0, 0)

    a == a.min()
    # array([[ True, False, False],
    #        [False, False, False]])


Maximal Value
=============
* ``np.ndarray.argmax()`` index of an ``a.max()`` element in array
* ``np.nanmax()``
* ``np.nanargmax()``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.max()
    # 6

    a.max(axis=0)
    # array([4, 5, 6])

    a.max(axis=1)
    # array([3, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.argmax()
    # 5

    a.argmax(axis=1)
    # array([2, 2])

    a.argmax(axis=0)
    # array([1, 1, 1])

.. code-block:: python

    import numpy as np


    a = np.array([[99,   2, 33],
                  [22,   0,  4],
                  [4,  155,  6]])

    a.max()             # 155
    a.max(axis=0)       # array([ 99, 155,  33])
    a.max(axis=1)       # array([ 99,  22, 155])
    a.max(axis=-1)      # array([ 99,  22, 155])

    a.argmax()          # 7
    a.argmax(axis=0)    # array([0, 2, 0])
    a.argmax(axis=1)    # array([0, 0, 1])
    a.argmax(axis=-1)   # array([0, 0, 1])

    a.flat[7]                               # 155
    np.unravel_index(7, (3, 3))             # (2, 1)
    np.unravel_index(a.argmax(), a.shape)   # (2, 1)

.. code-block:: python
    :caption: Shows the coordinates of ``argmax`` value

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.max()
    # 6

    a.argmax()
    # 5

    np.unravel_index(a.argmax(), a.shape)
    # (1, 2)

    a == a.max()
    # array([[False, False, False],
    #        [False, False,  True]])


Median
======
* ``np.median()``
* ``np.nanmedian()``


Quantile
========
* ``np.quantile()``
* ``np.nanquantile()``


Percentile
==========
* ``np.percentile()``
* ``np.nanpercentile()``


Assignments
===========
.. todo:: Create assignments
