**************
Array New Axis
**************


Recap
=====
.. code-block:: python

    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 1]
    # array([2, 5, 8])

    a[:, 0:2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])


With Indexes
============
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 1]
    # array([2, 5, 8])

    a[np.newaxis, :, 1]
    # array([[2, 5, 8]])

    a[:, np.newaxis, 1]
    # array([[2],
    #        [5],
    #        [8]])

    a[:, 1, np.newaxis]
    # array([[2],
    #        [5],
    #        [8]])


With Slices
===========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0:2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])

    a[np.newaxis, :, 0:2]
    # array([[[1, 2],
    #         [4, 5],
    #         [7, 8]]])

    a[:, np.newaxis, 0:2]
    # array([[[1, 2]],
    #
    #        [[4, 5]],
    #
    #        [[7, 8]]])

    a[:, 0:2, np.newaxis]
    # array([[[1],
    #         [2]],
    #
    #        [[4],
    #         [5]],
    #
    #        [[7],
    #         [8]]])


Assignments
===========
.. todo:: Create assignments
