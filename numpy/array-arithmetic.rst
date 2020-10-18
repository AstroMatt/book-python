****************
Array Arithmetic
****************


Rationale
=========
.. glossary::

    Scalar
        Single Value

    Vectorized Operations
        Single statement without a loop that explains a looping concept.
        Applies operation to each element.

            .. code-block:: python

                import numpy as np


                a = np.array([1, 2, 3])

                a + 1
                # array([2, 3, 4])


Addition
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a + 2
    # array([[3, 4, 5],
    #        [6, 7, 8]])


Subtraction
===========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a - 2
    # array([[-1,  0,  1],
    #        [ 2,  3,  4]])


Division
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a / 2
    # array([[0.5, 1. , 1.5],
    #        [2. , 2.5, 3. ]])


True Division
=============
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a // 2
    # array([[0, 1, 1],
    #        [2, 2, 3]])


Modulo
======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a % 2
    # array([[1, 0, 1],
    #        [0, 1, 0]])


Multiplication
==============
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a * 2
    # array([[ 2,  4,  6],
    #        [ 8, 10, 12]])


Power
=====
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a ** 2
    # array([[ 1,  4,  9],
    #        [16, 25, 36]])


Roots
=====
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a ** (1/2)
    # array([[1.        , 1.41421356, 1.73205081],
    #        [2.        , 2.23606798, 2.44948974]])


Assignments
===========
.. todo:: Create assignments
