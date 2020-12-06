*****************
Series Attributes
*****************


.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s
    # 0    a
    # 1    b
    # 2    c
    # dtype: object


Shape
=====
.. code-block:: python

    s.shape
    # (3,)


Size
====
.. code-block:: python

    s.size
    # 3


Number of Dimensions
====================
.. code-block:: python

    s.ndim
    # 1


Index
=====
.. code-block:: python

    s.index
    # RangeIndex(start=0, stop=3, step=1)


Values
======
.. code-block:: python

    s.values
    # array(['a', 'b', 'c'], dtype=object)


Assignments
===========
.. todo:: Create assignments
