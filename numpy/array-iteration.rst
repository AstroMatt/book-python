***************
Array Iteration
***************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    data = np.array([1, 2, 3])

    for value in data:
        print(value)

    # 1
    # 2
    # 3


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for value in data:
        print(value)

    # [1 2 3]
    # [4 5 6]
    # [7 8 9]

.. code-block:: python

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for row in data:
        for value in row:
            print(value)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9


Flat
====
.. code-block:: python
    :caption: Flatten

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for value in data.flatten():
        print(value)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

.. code-block:: python
    :caption: Ravel

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for value in data.ravel():
        print(value)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

Enumerate
=========
.. code-block:: python

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for i, value in enumerate(data):
        print(i, value)

    # 0 [1 2 3]
    # 1 [4 5 6]
    # 2 [7 8 9]

.. code-block:: python

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for i, value in enumerate(data.ravel()):
        print(i, value)
    # 0 1
    # 1 2
    # 2 3
    # 3 4
    # 4 5
    # 5 6
    # 6 7
    # 7 8
    # 8 9

.. code-block:: python

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            print(i, j, value)

    # 0 0 1
    # 0 1 2
    # 0 2 3
    # 1 0 4
    # 1 1 5
    # 1 2 6
    # 2 0 7
    # 2 1 8
    # 2 2 9


Assignments
===========

Numpy Iteration
---------------
* Assignment: Numpy Iteration
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 3 min
* Filename: :download:`solution/numpy_iteration.py`

English:
    #. Use data from "Given" section (see below)
    #. Use ``for`` to iterate over ``DATA``
    #. Print even numbers

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Używając ``for`` iteruj po ``DATA``
    #. Wypisz liczby parzyste

Hints:
    * ``number % 2 == 0``

Given:
    .. code-block:: python

        DATA = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

