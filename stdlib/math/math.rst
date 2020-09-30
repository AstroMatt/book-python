.. _Math Stdlib:

***********
Math Stdlib
***********


Builtin
=======

Constans
--------
* ``inf`` or ``Infinity``
* ``-inf`` or ``-Infinity``
* ``1e6`` or ``1e-4``

Functions
---------
* ``abs()``
* ``round()``
* ``pow()``
* ``sum()``
* ``min()``
* ``max()``
* ``divmod()``
* ``complex()``


``math``
========

Constants
---------
.. code-block:: python

    import math

    math.pi         # The mathematical constant π = 3.141592…, to available precision.
    math.e          # The mathematical constant e = 2.718281…, to available precision.
    math.tau        # The mathematical constant τ = 6.283185…, to available precision.

Degree/Radians Conversion
-------------------------
.. code-block:: python

    import math

    math.degrees(x)     # Convert angle x from radians to degrees.
    math.radians(x)     # Convert angle x from degrees to radians.

Rounding to lower
-----------------
.. code-block:: python

    import math

    math.floor(3.14)                # 3
    math.floor(3.00000000000000)    # 3
    math.floor(3.00000000000001)    # 3
    math.floor(3.99999999999999)    # 3

Rounding to higher
------------------
.. code-block:: python

    import math

    math.ceil(3.14)                 # 4
    math.ceil(3.00000000000000)     # 3
    math.ceil(3.00000000000001)     # 4
    math.ceil(3.99999999999999)     # 4

Logarithms
----------
.. code-block:: python

    import math

    math.log(x)     # if base is not set, then ``e``
    math.log(x, base=2)
    math.log(x, base=10)
    math.log10()    # Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
    math.log2(x)    # Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).

    math.exp(x)

Linear Algebra
--------------
.. code-block:: python

    import math

    math.sqrt(x)     # Return the square root of x.
    math.pow(x, y)   # Return x raised to the power y.

.. code-block:: python

    import math

    math.hypot(*coordinates)    # 2D, since Python 3.8 also multiple dimensions
    math.dist(p, q)             # Euclidean distance, since Python 3.8
    math.gcd(*integers)         # Greatest common divisor
    math.lcm(*integers)         # Least common multiple, since Python 3.9
    math.perm(n, k=None)        # Return the number of ways to choose k items from n items without repetition and with order.
    math.prod(iterable, *, start=1)  # Calculate the product of all the elements in the input iterable. The default start value for the product is 1., since Python 3.8
    math.remainder(x, y)        # Return the IEEE 754-style remainder of x with respect to y.

Trigonometry
------------
.. code-block:: python

    import math

    math.sin()
    math.cos()
    math.tan()

    math.asin(x)
    math.acos(x)
    math.atan(x)
    math.atan2(x)

.. code-block:: python
    :caption: Hyperbolic functions

    import math

    math.sinh()         # Return the hyperbolic sine of x.
    math.cosh()         # Return the hyperbolic cosine of x.
    math.tanh()         # Return the hyperbolic tangent of x.

    math.asinh(x)       # Return the inverse hyperbolic sine of x.
    math.acosh(x)       # Return the inverse hyperbolic cosine of x.
    math.atanh(x)       # Return the inverse hyperbolic tangent of x.

Infinity
--------
.. code-block:: python

    float('inf')                # inf
    float('-inf')               # -inf
    float('Infinity')           # inf
    float('-Infinity')          # -inf

.. code-block:: python

    from math import isinf

    isinf(float('inf'))         # True
    isinf(float('Infinity'))    # True
    isinf(float('-inf'))        # True
    isinf(float('-Infinity'))   # True

    isinf(1e308)                # False
    isinf(1e309)                # True

    isinf(1e-9999999999999999)  # False

Absolute value
--------------
.. code-block:: python

    abs(1)          # 1
    abs(-1)         # 1

    abs(1.2)        # 1.2
    abs(-1.2)       # 1.2

.. code-block:: python

    from math import fabs

    fabs(1)         # 1.0
    fabs(-1)        # 1.0

    fabs(1.2)       # 1.2
    fabs(-1.2)      # 1.2

.. code-block:: python

    from math import fabs

    vector = [1, 0, 1]

    abs(vector)
    # TypeError: bad operand type for abs(): 'list'

    fabs(vector)
    # TypeError: must be real number, not list

.. code-block:: python

    from math import sqrt


    def vector_abs(vector):
        return sqrt(sum(n**2 for n in vector))


    vector = [1, 0, 1]
    vector_abs(vector)
    # 1.4142135623730951

.. code-block:: python

    from math import sqrt


    class Vector:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __abs__(self):
            return sqrt(self.x**2 + self.y**2 + self.z**2)


    vector = Vector(x=1, y=0, z=1)
    abs(vector)
    # 1.4142135623730951


Assignments
===========

Trigonometry
------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/math_trigonometry.py`
* Last update: 2020-10-01

:English:
    #. Read input (angle in degrees) from user
    #. User will type ``int`` or ``float``
    #. Print all trigonometric functions (sin, cos, tg, ctg)
    #. If there is no value for this angle, raise an exception

:Polish:
    #. Program wczytuje od użytkownika wielkość kąta w stopniach
    #. Użytkownik zawsze podaje ``int`` albo ``float``
    #. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
    #. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś stosowny wyjątek

:Hints:
    * ``input('Type angle [deg]: ')``

Euclidean distance 2D
---------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/math_euclidean_2d.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Given are two points ``A: Tuple[int, int]`` and ``B: Tuple[int, int]``
    #. Coordinates are in cartesian system
    #. Points ``A`` and ``B`` are in two dimensional space
    #. Calculate distance between points using Euclidean algorithm
    #. Function must pass ``doctest``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
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

.. figure:: img/math-euclidean-distance.png
    :width: 75%
    :align: center

    Calculate Euclidean distance in Cartesian coordinate system

:Hints:
    * :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2`

Euclidean distance ``n`` dimensions
-----------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/math_euclidean_multi_dim.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Given are two points ``A: Sequence[int]`` and ``B: Sequence[int]``
    #. Coordinates are in cartesian system
    #. Points ``A`` and ``B`` are in ``N``-dimensional space
    #. Points ``A` and ``B`` must be in the same space
    #. Calculate distance between points using Euclidean algorithm
    #. Function must pass ``doctest``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
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

:Hints:
    * :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + ... + (n_2 - n_1)^2}`
    * ``for n1, n2 in zip(A, B)``

Matrix multiplication
---------------------
* Complexity level: hard
* Lines of code to write: 6 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/math_matmul.py`
* Last update: 2020-10-01

:English:
    #. Use code from "Input" section (see below)
    #. Multiply matrices using nested ``for`` loops
    #. Function must pass ``doctest``

:Polish:
    #. Użyj code z sekcji "Input" (patrz poniżej)
    #. Pomnóż macierze wykorzystując zagnieżdżone pętle ``for``
    #. Funkcja musi przechodzić ``doctest``

:Input:
    .. code-block:: python

        def matrix_multiplication(A, B):
            """
            >>> A = [[1, 0], [0, 1]]
            >>> B = [[4, 1], [2, 2]]
            >>> matrix_multiplication(A, B)
            [[4, 1], [2, 2]]

            >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
            >>> B = [[4,1], [2,2], [5,1], [2,3]]
            >>> matrix_multiplication(A, B)
            [[9, 2], [7, 3], [21, 8], [28, 8]]
            """
            return

:Hints:
    * Zero matrix
    * Three nested ``for`` loops

Triangle
--------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/math_triangle.py`
* Last update: 2020-10-01

:English:
    #. Calculate triangle area
    #. User will input base and height
    #. Input numbers will be only ``int`` and ``float``
    #. Function must pass ``doctest``

:Polish:
    #. Obliczy pole trójkąta
    #. Użytkownik poda wysokość i długość podstawy
    #. Wprowadzone dane będą tylko ``int`` lub ``float``
    #. Funkcja musi przechodzić ``doctest``
