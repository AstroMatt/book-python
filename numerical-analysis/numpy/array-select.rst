************
Array Select
************


Unique
======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3, 1],
                  [1, 4, 5, 6]])

    np.unique(a)
    # array([1, 2, 3, 4, 5, 6])

    np.unique(a, axis=0)
    # array([[1, 2, 3, 1],
    #        [1, 4, 5, 6]])

    np.unique(a, axis=1)
    # array([[1, 1, 2, 3],
    #        [1, 6, 4, 5]])


Diagonal
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2],
                  [3, 4]])

    a.diagonal()
    # array([1, 4])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.diagonal()
    # array([1, 5])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.diagonal()
    # array([1, 5, 9])

Nonzero
=======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 0, 2],
                  [3, 0, 4]])

    a.nonzero()
    # (array([0, 0, 1, 1]), array([0, 2, 0, 2]))


Where
=====

Single argument
---------------
* ``where(boolarray)``
* indexes of elements

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.where(a != 2)
    # (array([0, 2]),)

    np.where(a > 1)
    # (array([1, 2]),)

    np.where(a % 2 != 0)
    # (array([0, 2]),)


.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.where(a != 3)
    # (array([0, 0, 1, 1, 1]), array([0, 1, 0, 1, 2]))

    np.where(a % 2 != 0)
    # (array([0, 0, 1]), array([0, 2, 1]))

Multiple argument
-----------------
* ``where(boolarray, truearray, falsearray)``:

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.where(a % 2, 'odd', 'even')
    # array([['odd', 'even', 'odd'],
    #        ['even', 'odd', 'even']], dtype='<U4')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.where(a > 4, 99, 77)
    # array([[77, 77, 77],
    #        [77, 99, 99]])

.. code-block:: python

    import numpy as np


    a = np.array([[1., 2., 3.],
                  [4., 5., 6.]])

    np.where(a != 3, a, np.nan)       # if ``a != 3`` return element, otherwise ``np.nan``
    # array([[ 1.,  2., nan],
    #        [ 4.,  5.,  6.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = np.logical_and(a > 0, a % 3 == 0)
    # array([[False, False,  True],
    #        [False, False,  True]])

    a[b]
    # array([3, 6])


Fancy indexing
==============
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a > 2
    # array([[False, False,  True],
    #        [ True,  True,  True]])

    a[a > 2]
    # array([3, 4, 5, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    even = (a % 2 == 0)
    a[even]
    # array([2, 4, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[np.logical_and(a > 2, a <= 5)]
    # array([3, 4, 5])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    at_index = np.array([0, 1, 0])
    a[at_index]
    # array([1, 2, 1])

    at_index = np.array([0, 2])
    a[at_index]
    # array([1, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[[0,2]]
    # array([[1, 2, 3],
    #        [7, 8, 9]])

    a[[0,2], [1,2]]
    # array([2, 9])

    a[:2, [1,2]]
    # array([[2, 3],
    #        [5, 6]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 4], [9, 16]], float)
    b = np.array([0, 0, 1, 1, 0], int)
    c = np.array([0, 1, 1, 1, 1], int)

    a[b,c]
    # array([ 1., 4., 16., 16., 4.])

.. code-block:: python

    a[ [1,2] ]
    array([[4, 5, 6],
           [7, 8, 9]])


Take
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    at_index = np.array([0, 0, 1, 2, 2, 1])

    a.take(at_index)
    # array([1, 1, 2, 3, 3, 2])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    at_index = np.array([0, 0, 1])

    a.take(at_index, axis=0)
    # array([[1, 2, 3],
    #        [1, 2, 3],
    #        [4, 5, 6]])

    a.take(at_index, axis=1)
    # array([[1, 1, 2],
    #        [4, 4, 5]])


Assignments
===========

Select
------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/numpy_select.py`

:English:
    #. Set random seed to 0
    #. Generate ``a: ndarray`` of size 50x50
    #. ``a`` must contains random integers from 0 to 1024 inclusive
    #. Create ``b: ndarray`` with elements selected from ``a`` which are power of two
    #. Sort ``b`` in descending order
    #. Print ``b``

:Polish:
    #. Ustaw ziarno losowości na 0
    #. Wygeneruj ``a: ndarray`` rozmiaru 50x50
    #. ``a`` musi zawierać losowe liczby całkowite z zakresu od 0 do 1024 włącznie
    #. Stwórz ``b: ndarray`` z elementami wybranymi z ``a``, które są potęgami dwójki
    #. Posortuj ``b`` w kolejności malejącej
    #. Wypisz ``b``

:Hint:
    * ``np.isin(a, b)``
    * ``np.flip(a)``
