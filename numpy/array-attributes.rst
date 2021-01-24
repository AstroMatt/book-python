****************
Array Attributes
****************


Dimensions
==========
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.shape         # (3,)
    a.ndim          # 1
    a.size          # 3
    len(a)          # 3

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.shape         # (2, 3)
    a.ndim          # 2
    a.size          # 6
    len(a)          # 2

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.shape         # (3, 3)
    a.ndim          # 2
    a.size          # 9
    len(a)          # 3

.. code-block:: python

    import numpy as np


    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape         # (2, 3, 3)
    a.ndim          # 3
    a.size          # 18
    len(a)          # 2


Data
====
* ``int64`` takes 64 bits (8 bytes of memory)
* strides inform how many bytes numpy has to jump to access values in each dimensions

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.shape         # (3,)
    a.itemsize      # 8
    a.strides       # (8,)
    a.data          # <memory at 0x10cdfaa10>
    list(a.data)    # NotImplementedError: multi-dimensional sub-views are not implemented

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.shape         # (2, 3)
    a.itemsize      # 8
    a.strides       # (24, 8)
    a.data          # <memory at 0x10caefbb0>

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.shape         # (3, 3)
    a.itemsize      # 8
    a.strides       # (24, 8)
    a.data          # <memory at 0x10cf92210>

.. code-block:: python

    import numpy as np


    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape         # (2, 3, 3)
    a.itemsize      # 8
    a.strides       # (72, 24, 8)
    a.data          # <memory at 0x107933c70>


Assignments
===========

.. todo:: Convert assignments to literalinclude

Numpy Attributes
----------------
* Assignment: Numpy Attributes
* Filename: :download:`assignments/numpy_attributes.py`
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Print:

        a. number of dimensions;
        b. number of elements;
        c. data type;
        d. element size;
        d. shape;
        e. strides.

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wypisz:

        a. liczbę wymiarów,
        b. liczbę elementów,
        c. typ danych,
        d. rozmiar elementu,
        d. kształt,
        e. przeskoki (strides).

Given:
    .. code-block:: python

        a = np.array([[-1.1, 0.0, 1.1],
                      [ 2.2, 3.3, 4.4]])

