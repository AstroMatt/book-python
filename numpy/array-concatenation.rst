*******************
Array Concatenation
*******************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    np.concatenate(a, b)
    # Traceback (most recent call last):
    # TypeError: only integer scalar arrays can be converted to a scalar index

    np.concatenate((a, b))
    # array([1, 2, 3, 4, 5, 6])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([7, 8, 9])

    np.concatenate((a, b, c))
    # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])

    np.concatenate((a, b))
    # array([1, 2, 3, 2, 3, 4])


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    np.concatenate((a, b))
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6],
    #        [7, 8]])

    np.concatenate((a, b), axis=0)
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6],
    #        [7, 8]])

    np.concatenate((a, b), axis=1)
    # array([[1, 2, 5, 6],
    #        [3, 4, 7, 8]])


Assignments
===========

Numpy Concatenation
-------------------
* Assignment: Numpy Concatenation
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 3 min
* Filename: :download:`assignments/numpy_concatenation.py`

English:
    #. Use data from "Given" section (see below)
    #. Given are one-dimensional: ``a: np.ndarray``, ``b: np.ndarray``
    #. Concatenate them as ``result: np.ndarray``
    #. Reshape ``result`` into two rows and three columns
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Dane są jednowymiarowe: ``a: np.ndarray``, ``b: np.ndarray``
    #. Połącz je ze sobą jako ``result: np.ndarray``
    #. Przekształć ``result`` w dwa wiersze na trzy kolumny
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])

Tests:
    >>> result
    array([[1, 2, 3],
           [4, 5, 6]])
