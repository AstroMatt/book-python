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

    sorted(a)
    # [1, 2, 3]

    a.sort()
    # array([1, 2, 3])

Two dimensional - Default axis
------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[2, 3, 1],
                  [5, 6, 4]])

    sorted(a)
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    a.sort()
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
* Returns new ``ndarray``
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
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_sort.py`

:English:
    #. Set random seed to zero
    #. Generate ``result: ndarray`` of 12 random integers from 0 to 100 (exclusive)
    #. Reshape ``result`` to 3x4
    #. Sort ``result`` columns
    #. Flip ``result`` rows
    #. Print ``result``

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``result: ndarray`` z 12 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    #. Zmień kształt na 3x4
    #. Posortuj kolumny ``result``
    #. Flipnij wiersze ``result``
    #. Wypisz ``result``
