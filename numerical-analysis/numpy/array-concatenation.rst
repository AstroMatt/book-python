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
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/numpy_concatenation.py`

:English:
    #. Use data from "Input" section (see below)
    #. Given are one-dimensional: ``a: ndarray``, ``b: ndarray``
    #. Concatenate them
    #. Represent the result as ``ndarray``: two rows and three columns
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Dane są jednowymiarowe: ``a: ndarray``, ``b: ndarray``
    #. Połącz je ze sobą
    #. Przedstaw wynik jako ``ndarray``: dwa wiersze na trzy kolumny
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])

:Output:
    .. code-block:: python

        array([[1, 2, 3],
               [4, 5, 6]])
