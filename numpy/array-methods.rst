*************
Array Methods
*************


Copy
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = a
    c = a.copy()

    a[0] = 99

    a
    # array([99, 2, 3])

    b
    # array([99, 2, 3])

    c
    # array([1, 2, 3])


Put
===

One dimensional
---------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])

    a.put([0, 2, 5], 99)

    a
    # array([99,  2, 99,  4,  5, 99])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])
    at_index = [0, 2, 5]

    a.put(at_index, 99)

    a
    # array([99,  2, 99,  4,  5, 99])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])
    b = np.array([99, 88, 77, 66, 55, 44, 33, 22])
    at_index = [0, 2, 5]

    a.put(at_index, b)

    a
    # array([99,  2, 88,  4,  5, 77])

Two dimensional
---------------
* Equivalent to ``a.flat[indexes] = value``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    b = np.array([99, 88, 77, 66, 55, 44, 33, 22])
    at_index = [0, 2, 5]

    a.put(at_index, b)

    a
    # array([[99,  2, 88],
    #        [ 4,  5, 77],
    #        [ 7,  8,  9]])


Fill
====
* Modifies inplace

.. code-block:: python
    :caption: Fill all

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.fill(0)
    # array([[0, 0, 0],
    #        [0, 0, 0],
    #        [0, 0, 0]])

.. code-block:: python
    :caption: Fill slice

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0].fill(0)
    # array([[0, 2, 3],
    #        [0, 5, 6],
    #        [0, 8, 9]])

.. code-block:: python
    :caption: Fill NaN (dtype=np.int)

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=np.float)

    a[:, 0].fill(np.nan)

    a
    # array([[-9223372036854775808, 2, 3],
    #        [-9223372036854775808, 5, 6],
    #        [-9223372036854775808, 8, 9]])

.. code-block:: python
    :caption: Fill NaN (dtype=np.float)

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=np.float)

    a[:, 0].fill(np.nan)

    a
    # array([[nan,  2.,  3.],
    #        [nan,  5.,  6.],
    #        [nan,  8.,  9.]])


Transpose
=========
* ``a.transpose()`` or ``a.T``
* ``a.transpose()`` is preferred

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.transpose()
    # array([[1, 4],
    #        [2, 5],
    #        [3, 6]])

    a.T
    # array([[1, 4],
    #        [2, 5],
    #        [3, 6]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.transpose()
    # array([[1, 4, 7],
    #        [2, 5, 8],
    #        [3, 6, 9]])


.. _Numpy signum:

Signum
======
.. figure:: img/numpy-methods-signum.png
    :width: 75%

.. code-block:: python

    import numpy as np


    a = np.array([[-2, -1, 0],
                  [0, 1, 2]])

    np.sign(a)
    # array([[-1, -1,  0],
    #        [ 0,  1,  1]])

.. code-block:: python

    import numpy as np

    # t1 = 230 lux
    # t2 = 218 lux
    # t3 = 230 lux
    # t4 = 2 lux
    # t5 = 0 lux
    # t6 = 0 lux
    # t7 = 10 lux
    # t8 = 0 lux

    a = np.array([230, 218, 230, 2, 0, 0, 10, 0])

    np.sign(a)
    # array([1, 1, 1, 1, 0, 0, 1, 0])


Assignments
===========

Numpy Methods
-------------
* Assignment: Numpy Methods
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min
* Filename: :download:`assignments/numpy_methods.py`

English:
    #. Use data from "Given" section (see below)
    #. Reshape ``result`` to 3x4
    #. Fill last column with zeros (0)
    #. Transpose ``result``
    #. Convert ``result`` to float
    #. Fill first row with ``np.nan``
    #. Print ``result``

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zmień kształt na 3x4
    #. Wypełnij ostatnią kolumnę zerami (0)
    #. Transponuj ``result``
    #. Przekonwertuj ``result`` do float
    #. Wypełnij pierwszy wiersz ``np.nan``
    #. Wypisz ``result``

Given:
    .. code-block:: python

        DATA = np.array([[44, 47, 64, 67],
                         [67,  9, 83, 21],
                         [36, 87, 70, 88]])

Tests:
    >>> type(result)
    np.ndarray
    >>> result
    array([[nan, nan, nan],
           [47.,  9., 87.],
           [64., 83., 70.],
           [ 0.,  0.,  0.]])
