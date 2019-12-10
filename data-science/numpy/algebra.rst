**************
Linear Algebra
**************



Linear Algebra
==============
* ``np.sign()``
* ``np.abs()``
* ``np.sqrt()``
* ``np.power()``

Logarithms
==========
* ``np.log()``
* ``np.log10()``
* ``np.exp()``


Vector and matrix mathematics
=============================

Dot product of two arrays
-------------------------
* ``np.dot()``
* If either a or b is 0-D (scalar), it is equivalent to ``multiply`` and using ``numpy.multiply(a, b)`` or ``a * b`` is preferred.
* If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
* If both a and b are 2-D arrays, it is matrix multiplication, but using ``matmul`` or ``a @ b`` is preferred.
* If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
* If a is an N-D array and b is an M-D array (where ``M>=2``), it is a sum product over the last axis of a and the second-to-last axis of b: ``dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])``

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], float)
    b = np.array([0, 1, 1], float)

    np.dot(a, b)
    # 5.0

.. code-block:: python

    import numpy as np


    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([2, 3], float)
    c = np.array([[1, 1], [4, 0]], float)

    a
    # array([[ 0., 1.],
    #        [ 2., 3.]])

    np.dot(b, a)
    # array([ 6., 11.])

    np.dot(a, b)
    # array([ 3., 13.])

    np.dot(a, c)
    # array([[ 4., 0.],
    #        [ 14., 2.]])

    np.dot(c, a)
    # array([[ 2., 4.],
    #        [ 0., 4.]])

Determinant of a square matrix
------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    np.linalg.det(a)
    # -53.999999999999993

Inner product
-------------
* Compute inner product of two vectors
* ``np.inner()``
* Ordinary inner product of vectors for 1-D arrays (without complex conjugation).
* In higher dimensions a sum product over the last axes.

.. code-block:: python
    :caption: Ordinary inner product for vectors

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([0, 1, 0])

    np.inner(a, b)
    # 2

.. code-block:: python
    :caption: Multidimensional example

    import numpy as np


    a = np.arange(24).reshape((2,3,4))
    b = np.arange(4)

    np.inner(a, b)
    # array([[ 14,  38,  62],
    #        [ 86, 110, 134]])

Outer product
-------------
* Compute the outer product of two vectors
* ``np.outer()``

.. code-block:: python

    import numpy as np


    a = np.array([1, 4, 0], float)
    b = np.array([2, 2, 1], float)

    np.outer(a, b)
    # array([[ 2., 2., 1.],
    #        [ 8., 8., 4.],
    #        [ 0., 0., 0.]])

.. code-block:: python
    :caption: An example using a "vector" of letters

    import numpy as np


    a = np.array(['a', 'b', 'c'], dtype=object)

    np.outer(a, [1, 2, 3])
    # array([['a', 'aa', 'aaa'],
    #        ['b', 'bb', 'bbb'],
    #        ['c', 'cc', 'ccc']], dtype=object)

Cross product
-------------
* The cross product of a and b in R^3 is a vector perpendicular to both a and b.
* ``np.cross()``

.. code-block:: python
    :caption: Vector cross-product

    import numpy as np


    x = [1, 2, 3]
    y = [4, 5, 6]

    np.cross(x, y)
    # array([-3,  6, -3])

.. code-block:: python
    :caption: One vector with dimension 2

    import numpy as np

    x = [1, 2]
    y = [4, 5, 6]

    np.cross(x, y)
    # array([12, -6, -3])


Eigenvalues and vectors of a square matrix
==========================================
* Each of a set of values of a parameter for which a differential equation has a nonzero solution (an eigenfunction) under given conditions.
* Any number such that a given matrix minus that number times the identity matrix has a zero determinant.

.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    vals, vecs = np.linalg.eig(a)

    vals
    # array([ 9. , 2.44948974, -2.44948974])

    vecs
    # array([[-0.3538921 , -0.56786837, 0.27843404],
    #        [-0.88473024, 0.44024287, -0.89787873],
    #        [-0.30333608, 0.69549388, 0.34101066]])


Inverse of a square matrix
==========================
.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    np.linalg.inv(a)
    # array([[ 0.14814815, 0.07407407, -0.25925926],
    #        [ 0.2037037 , -0.14814815, 0.51851852],
    #        [-0.27777778, 0.11111111, 0.11111111]])

.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    b = np.linalg.inv(a)

    np.dot(a, b)
    # array([[ 1.00000000e+00, 5.55111512e-17, 2.22044605e-16],
    #        [ 0.00000000e+00, 1.00000000e+00, 5.55111512e-16],
    #        [ 1.11022302e-16, 0.00000000e+00, 1.00000000e+00]])


Singular value decomposition of a matrix
========================================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 3, 4], [5, 2, 3]], float)

    U, s, Vh = np.linalg.svd(a)

    U
    # array([[-0.6113829 , -0.79133492],
    #        [-0.79133492, 0.6113829 ]])

    s
    # array([ 7.46791327, 2.86884495])

    Vh
    # array([[-0.61169129, -0.45753324, -0.64536587],
    #        [ 0.78971838, -0.40129005, -0.46401635],
    #        [-0.046676 , -0.79349205, 0.60678804]])


Linear Algebra
==============
.. csv-table:: Linear algebra basics
    :header-rows: 1

    "Function", "Description"
    "norm", "Vector or matrix norm"
    "inv", "Inverse of a square matrix"
    "solve", "Solve a linear system of equations"
    "det", "Determinant of a square matrix"
    "slogdet", "Logarithm of the determinant of a square matrix"
    "lstsq", "Solve linear least-squares problem"
    "pinv", "Pseudo-inverse (Moore-Penrose) calculated using a singular value decomposition"
    "matrix_power", "Integer power of a square matrix"
    "matrix_rank", "Calculate matrix rank using an SVD-based method"

.. csv-table:: Eigenvalues and decompositions
    :header-rows: 1

    "Function", "Description"
    "eig", "Eigenvalues and vectors of a square matrix"
    "eigh", "Eigenvalues and eigenvectors of a Hermitian matrix"
    "eigvals", "Eigenvalues of a square matrix"
    "eigvalsh", "Eigenvalues of a Hermitian matrix"
    "qr", "QR decomposition of a matrix"
    "svd", "Singular value decomposition of a matrix"
    "cholesky", "Cholesky decomposition of a matrix"

.. csv-table:: Tensor operations
    :header-rows: 1

    "Function", "Description"
    "tensorsolve", "Solve a linear tensor equation"
    "tensorinv", "Calculate an inverse of a tensor"

.. csv-table:: Exceptions
    :header-rows: 1

    "Function", "Description"
    "LinAlgError", "Indicates a failed linear algebra operation"


Assignments
===========

Euclidean distance 2D
---------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/algebra_euclidean_2d.py`

:English:
    #. Given are two points ``A: Tuple[int, int]`` and ``B: Tuple[int, int]``
    #. Coordinates are in cartesian system
    #. Points ``A`` and ``B`` are in two dimensional space
    #. Calculate distance between points using Euclidean algorithm
    #. Function must pass ``doctest``

:Polish:
    #. Dane są dwa punkty ``A: Tuple[int, int]`` i ``B: Tuple[int, int]``
    #. Koordynaty są w systemie kartezjańskim
    #. Punkty ``A`` i ``B`` są w dwuwymiarowej przestrzeni
    #. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    #. Funkcja musi przechodzić ``doctest``

:Input:
    .. code-block:: python

        def euclidean_distance(A, B):
            """
            >>> A = (1, 0)
            >>> B = (0, 1)
            >>> euclidean_distance(A, B)
            1.4142135623730951

            >>> euclidean_distance((0,0), (1,0))
            1.0

            >>> euclidean_distance((0,0), (1,1))
            1.4142135623730951

            >>> euclidean_distance((0,1), (1,1))
            1.0

            >>> euclidean_distance((0,10), (1,1))
            9.055385138137417
            """
            x1 = ...
            y1 = ...
            x2 = ...
            y2 = ...
            return ...

.. figure:: img/euclidean-distance.png
    :scale: 100%
    :align: center

    Calculate Euclidean distance in Cartesian coordinate system

:Hint:
    * :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2`

Euclidean distance ``n`` dimensions
-----------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/algebra_euclidean_multi_dim.py`

:English:
    #. Given are two points ``A: Sequence[int]`` and ``B: Sequence[int]``
    #. Coordinates are in cartesian system
    #. Points ``A`` and ``B`` are in ``N``-dimensional space
    #. Points ``A` and ``B`` must be in the same space
    #. Calculate distance between points using Euclidean algorithm
    #. Function must pass ``doctest``

:Polish:
    #. Dane są dwa punkty ``A: Sequence[int]`` i ``B: Sequence[int]``
    #. Koordynaty są w systemie kartezjańskim
    #. Punkty ``A`` i ``B`` są w ``N``-wymiarowej przestrzeni
    #. Punkty ``A`` i ``B`` muszą być w tej samej przestrzeni
    #. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    #. Funkcja musi przechodzić ``doctest``

:Input:
    .. code-block:: python

        def euclidean_distance(A, B):
            """
            >>> A = (0,1,0,1)
            >>> B = (1,1,0,0)
            >>> euclidean_distance(A, B)
            1.4142135623730951

            >>> euclidean_distance((0,0,0), (0,0,0))
            0.0

            >>> euclidean_distance((0,0,0), (1,1,1))
            1.7320508075688772

            >>> euclidean_distance((0,1,0,1), (1,1,0,0))
            1.4142135623730951

            >>> euclidean_distance((0,0,1,0,1), (1,1,0,0,1))
            1.7320508075688772

            >>> euclidean_distance((0,0,1,0,1), (1,1))
            Traceback (most recent call last):
                ...
            ValueError: Points must be in the same dimensions
            """
            return ...

:Hint:
    * :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + ... + (n_2 - n_1)^2}`
    * ``for n1, n2 in zip(A, B)``

Finding number
--------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/algebra_find.py`

#. Mamy liczbę trzycyfrową.
#. Jeżeli od liczny dziesiątek odejmiemy liczbę jedności otrzymamy 6.
#. Jeżeli do liczby dziesiątek dodamy liczbę jedności otrzymamy 10.
#. Znajdź wszystkie liczby trzycyfrowe spełniające ten warunek
#. Znajdź liczby trzycyfrowe podzielne przez 3

:Hints:
    - Ax=B
    - x=A−1B

.. code-block:: python

    liczba_dziesiatek - liczba_jednosci = 6
    liczba_dziesiatek + liczba_jednosci = 10

    liczba_dziesiatek = liczba_jednosci + 6
    liczba_dziesiatek + liczba_jednosci = 10

    liczba_dziesiatek = liczba_jednosci + 6
    (liczba_jednosci + 6) + liczba_jednosci 10

    liczba_dziesiatek = liczba_jednosci + 6
    2 * liczba_jednosci + 6 = 10

    liczba_dziesiatek = liczba_jednosci + 6
    liczba_jednosci = 8 / 2

    liczba_dziesiatek = 2 + 6
    liczba_jednosci = 2

    liczba_dziesiatek = 8
    liczba_jednosci = 2

.. code-block:: python

    x1 - x2 = 6
    x1 + x2 = 10

    x1 = 6 + x2
    6 + x2 + x2 = 10

    2 * x2 = 4
    x2 = 2
    x1 = 8


    import numpy as np

    A = np.matrix([[1, -1], [1, 1]])
    # matrix([[ 1, -1],
    #        [ 1,  1]])

    B = np.matrix([6, 10]).T  # Transpose matrix
    # matrix([[ 6],
    #        [10]])

    x = A**(-1) * B
    # matrix([[8.],
    #        [2.]])

    A*x == B
    # matrix([[ True],
    #        [ True]])

    res1 = np.arange(1, 10)*100 + 10*x[0,0] + 1*x[1,0]
    # array([182., 282., 382., 482., 582., 682., 782., 882., 982.])

    res1[res1 % 3 == 0]
    # array([282., 582., 882.])

    m = res1 % 3 == 0
    # array([False,  True, False, False,  True, False, False,  True, False])

    res1[m]
    # array([282., 582., 882.])

    res2 = res1[m]
    # array([282., 582., 882.])
