***********
Array Slice
***********


1-dimensional Array
===================
.. code-block:: python
    :caption: 1-dimensional Array

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    a[1:5]          # array([2, 3, 4, 5])
    a[3:8]          # array([4, 5, 6, 7, 8])

    a[0:5]          # array([1, 2, 3, 4, 5])
    a[:5]           # array([1, 2, 3, 4, 5])
    a[5:9]          # array([6, 7, 8, 9])

    a[5:len(a)]     # array([6, 7, 8, 9])
    a[5:]           # array([6, 7, 8, 9])
    a[-2:]          # array([8, 9])
    a[-5:]          # array([5, 6, 7, 8, 9])
    a[-6:-2]        # array([4, 5, 6, 7])

    a[3:8:2]        # array([4, 6, 8])
    a[-8:-3:2]      # array([2, 4, 6])
    a[::2]          # array([1, 3, 5, 7, 9])
    a[1::2]         # array([2, 4, 6, 8])

    a[0:len(a)]     # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    a[0:]           # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    a[:len(a)]      # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    a[:]            # array([1, 2, 3, 4, 5, 6, 7, 8, 9])


2-dimensional Array
===================
.. code-block:: python
    :caption: Rows

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:]
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a[1:]
    # array([[4, 5, 6],
    #        [7, 8, 9]])

    a[:1]
    # array([[1, 2, 3]])

    a[1:3]
    # array([[4, 5, 6],
    #        [7, 8, 9]])

    a[::2]
    # array([[1, 2, 3],
    #        [7, 8, 9]])

    a[1::2]
    # array([[4, 5, 6]])

.. code-block:: python
    :caption: Columns

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0]
    # array([1, 4, 7])

    a[:, 1]
    # array([2, 5, 8])

    a[:, 2]
    # array([3, 6, 9])

    a[:, -1]
    # array([3, 6, 9])

    a[:, 0:1]
    # array([[1],
    #        [4],
    #        [7]])

    a[:, 0:2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])

    a[:, :2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])

    a[:, ::2]
    # array([[1, 3],
    #        [4, 6],
    #        [7, 9]])

    a[:, 1::2]
    # array([[2],
    #        [5],
    #        [8]])

.. code-block:: python
    :caption: Rows and Columns

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[0:1, 0:1]
    # array([[1]])

    a[0:1, 0:2]
    # array([[1, 2]])

    a[0:1, 0:3]
    # array([[1, 2, 3]])

    a[0:2, 0:2]
    # array([[1, 2],
    #        [4, 5]])

    a[-1:, -2:]
    # array([[8, 9]])

    a[::2, ::2]
    # array([[1, 3],
    #        [7, 9]])

    a[1::2, 1::2]
    # array([[5]])

    a[[2,1], ::2]
    # array([[7, 9],
    #        [4, 6]])


Assignments
===========

.. todo:: Convert assignments to literalinclude

Numpy Slice 1
-------------
* Assignment: Numpy Slice 1
* Filename: :download:`assignments/numpy_slice_1.py`
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Print inner 2x2 elements
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wybierz wewnętrzne 2x2 elementy
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = np.array([
            [2, 8, 1, 5],
            [8, 8, 4, 4],
            [5, 5, 2, 5],
            [1, 0, 6, 0],
        ])

Tests:

    >>> type(result)
    np.ndarray
    >>> result
    array([[8, 4],
           [5, 2]])

Numpy Slice 2
-------------
* Assignment: Numpy Slice 2
* Filename: :download:`assignments/numpy_slice_2.py`
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Print inner 4x4 elements
    3. Inner matrix is exactly in the middle of outer

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wypisz środkowe 4x4 elementy
    3. Środkowa macierz jest dokładnie w środku większej

Given:
    .. code-block:: python

        DATA = np.array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4, 7, 6, 8, 8, 1, 6],
                         [7, 7, 8, 1, 5, 9, 8, 9, 4, 3, 0, 3, 5, 0, 2, 3],
                         [8, 1, 3, 3, 3, 7, 0, 1, 9, 9, 0, 4, 7, 3, 2, 7],
                         [2, 0, 0, 4, 5, 5, 6, 8, 4, 1, 4, 9, 8, 1, 1, 7],
                         [9, 9, 3, 6, 7, 2, 0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
                         [4, 4, 8, 4, 3, 7, 5, 5, 0, 1, 5, 9, 3, 0, 5, 0],
                         [1, 2, 4, 2, 0, 3, 2, 0, 7, 5, 9, 0, 2, 7, 2, 9],
                         [2, 3, 3, 2, 3, 4, 1, 2, 9, 1, 4, 6, 8, 2, 3, 0],
                         [0, 6, 0, 6, 3, 3, 8, 8, 8, 2, 3, 2, 0, 8, 8, 3],
                         [8, 2, 8, 4, 3, 0, 4, 3, 6, 9, 8, 0, 8, 5, 9, 0],
                         [9, 6, 5, 3, 1, 8, 0, 4, 9, 6, 5, 7, 8, 8, 9, 2],
                         [8, 6, 6, 9, 1, 6, 8, 8, 3, 2, 3, 6, 3, 6, 5, 7],
                         [0, 8, 4, 6, 5, 8, 2, 3, 9, 7, 5, 3, 4, 5, 3, 3],
                         [7, 9, 9, 9, 7, 3, 2, 3, 9, 7, 7, 5, 1, 2, 2, 8],
                         [1, 5, 8, 4, 0, 2, 5, 5, 0, 8, 1, 1, 0, 3, 8, 8],
                         [4, 4, 0, 9, 3, 7, 3, 2, 1, 1, 2, 1, 4, 2, 5, 5]])

Tests:
    .. code-block:: python

        result: np.ndarray
        # array([[2, 0, 7, 5],
        #        [1, 2, 9, 1],
        #        [8, 8, 8, 2],
        #        [4, 3, 6, 9]])

.. figure:: img/random-inner-sum.png

    Inner 4x4 elements
