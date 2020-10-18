**********
Array Sort
**********

Sort
====

One dimensional
---------------
.. code-block:: python

    import numpy as np


    a = np.array([2, 3, 1])
    a.sort()

    a
    # array([1, 2, 3])

Two dimensional - Default axis
------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[2, 3, 1],
                  [5, 6, 4]])
    a.sort()

    a
    # array([[1, 2, 3],
    #        [4, 5, 6]])

Two dimensional - Columns
-------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[2, 3, 1],
                  [5, 6, 4]])

    a.shape
    # (2, 3)

    a.sort(axis=0)
    # array([[2, 3, 1],
    #        [5, 6, 4]])

    a.sort(axis=1)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

Two dimensional - Rows
----------------------
.. code-block:: python

    import numpy as np

    a = np.array([[9, 1, 8],
                  [2, 3, 1],
                  [5, 6, 4]])

    a.shape
    # (3,3)

    a.sort(axis=0)
    # array([[2, 1, 1],
    #        [5, 3, 4],
    #        [9, 6, 8]])

    a.sort(axis=1)
    # array([[1, 8, 9],
    #        [1, 2, 3],
    #        [4, 5, 6]])


Flip
====
* Does not modify inplace
* Returns new ``np.ndarray``
* Reverse the order of elements in an array along the given axis

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    np.flip(a)
    # array([3, 2, 1])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.flip()
    # array([[6, 5, 4],
    #        [3, 2, 1]])

    np.flip(a, axis=0)
    # array([[4, 5, 6],
    #        [1, 2, 3]])

    np.flip(a, axis=1)
    # array([[3, 2, 1],
    #        [6, 5, 4]])


Assignments
===========

Numpy Sort
----------
* Assignment name: Numpy Sort
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_sort.py`

:English:
    #. Use data from "Input" section (see below)
    #. Sort ``result`` columns
    #. Flip ``result`` rows
    #. Print ``result``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Posortuj kolumny ``result``
    #. Flipnij wiersze ``result``
    #. Wypisz ``result``

:Input:
    .. code-block:: python

        DATA = np.array([[44, 47, 64, 67],
                         [67,  9, 83, 21],
                         [36, 87, 70, 88]])

:Output:
    .. code-block:: python

        result: np.ndarray
        # array([[36, 70, 87, 88],
        #        [ 9, 21, 67, 83],
        #        [44, 47, 64, 67]])
