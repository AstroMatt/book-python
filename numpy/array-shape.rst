***********
Array Shape
***********


* Any shape operation changes only ``np.ndarray.shape`` and ``np.ndarray.strides`` and does not touch data

Shape
=====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.shape     # (3,)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.shape     # (2, 3)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.shape     # (3, 3)

.. code-block:: python

    import numpy as np


    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],
                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape         # (2, 3, 3)


Reshape
=======
* Returns new array
* Does not modify inplace
* ``a.reshape(1, 2)`` is equivalent to ``a.reshape((1, 2))``


.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.reshape(1, 3)
    # array([[1, 2, 3]])

    a.reshape(3, 1)
    # array([[1],
    #        [2],
    #        [3]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.reshape(3, 2)
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6]])

    a.reshape(1, 6)
    # array([[1, 2, 3, 4, 5, 6]])

    a.reshape(6, 1)
    # array([[1],
    #        [2],
    #        [3],
    #        [4],
    #        [5],
    #        [6]])

    a.reshape(5, 2)
    # Traceback (most recent call last):
    #     ...
    # ValueError: cannot reshape array of size 6 into shape (5,2)

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    a.reshape(2, 4)
    # array([[1, 2, 3, 4],
    #        [5, 6, 7, 8]])

    a.reshape(2, 4, 1)
    # array([[[1],
    #         [2],
    #         [3],
    #         [4]],
    #        [[5],
    #         [6],
    #         [7],
    #         [8]]])

    a.reshape(2, 2, 2)
    # array([[[1, 2],
    #         [3, 4]],
    #        [[5, 6],
    #         [7, 8]]])

    a.reshape(1, 2, 4)
    # array([[[1, 2, 3, 4],
    #         [5, 6, 7, 8]]])

    a.reshape(4, 2, 1)
    #array([[[1],
    #        [2]],
    #       [[3],
    #        [4]],
    #       [[5],
    #        [6]],
    #       [[7],
    #        [8]]])

    a.reshape(1, 8, 1)
    # array([[[1],
    #         [2],
    #         [3],
    #         [4],
    #         [5],
    #         [6],
    #         [7],
    #         [8]]])

    a.reshape(2, 3, 1)
    # Traceback (most recent call last):
    #     ...
    # ValueError: cannot reshape array of size 8 into shape (2,3,1)


Flatten
=======
* Returns new array (makes memory copy - expensive)
* Does not modify inplace

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.flatten()
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.flatten()
    # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

.. code-block:: python

    import numpy as np

    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.flatten()
    # array([ 1,  2,  3,  4,  5,  6,  5,  6,  7, 11, 22, 33, 44, 55, 66, 77, 88, 99])


Ravel
=====
* Ravel is the same as Flatten but returns a reference (or view) of the array if possible (i.e. memory is contiguous)
* Otherwise returns new array (makes memory copy)

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.ravel()
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.ravel()
    # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

.. code-block:: python

    import numpy as np

    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])


    a.ravel()
    # array([ 1,  2,  3,  4,  5,  6,  5,  6,  7, 11, 22, 33, 44, 55, 66, 77, 88, 99])


Assignments
===========

Numpy Shape
-----------
* Assignment: Numpy Shape
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Filename: :download:`solution/numpy_shape.py`

English:
    #. Use data from "Given" section (see below)
    #. Given ``a: np.ndarray`` (see below)
    #. Flatten using method ``.ravel()``
    #. Print ``a``
    #. Change shape back to 3x3
    #. Print ``a``

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Dany ``a: np.ndarray`` (patrz sekcja input)
    #. Spłaszcz używając metody ``.ravel()``
    #. Wypisz ``a``
    #. Zmień kształt na powrót na 3x3
    #. Wypisz ``a``

Given:
    .. code-block:: python

        a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
