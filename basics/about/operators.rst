*********
Operators
*********


Comparison Operators
====================
* ``x < y`` - Less than
* ``x <= y`` - Less or equal
* ``x > y`` - Greater than
* ``x >= y`` - Greater or equal
* ``x == y`` - Equals
* ``x != y`` - Not Equals

.. doctest::

    >>> 10 < 2
    False

    >>> 10 <= 2
    False

    >>> 10 > 2
    True

    >>> 10 >= 2
    True

    >>> 10 == 2
    False

    >>> 10 != 2
    True

.. doctest::

    >>> x = 10
    >>> y = 2
    >>> x >= 2
    True


Arithmetic Operators
====================
* ``+`` - Addition
* ``-`` - Subtraction
* ``*`` - Multiplication
* ``/`` - Division

.. doctest::

    >>> 10 + 2
    12

    >>> 10 - 2
    8

    >>> 10 * 2
    20

    >>> 10 / 2
    5.0

.. doctest::

    >>> x = 10
    >>> y = 2
    >>> x + y
    12


Power and Root
==============
* ``a ** b`` - ``b`` power of the number ``a``
* ``a ** (1/b)`` - ``b``-th root of the number ``a``

.. doctest::

    >>> 10 ** 2
    100

    >>> 2 ** -1
    0.5

    >>> 1.337 ** 3
    2.389979753

.. doctest::

    >>> 4 ** (1/2)
    2.0

    >>> 2 ** (1/2)
    1.4142135623730951

    >>> 27 ** (1/3)
    3.0

.. doctest::

    >>> 4 ** 0.5
    2.0

    >>> 2 ** 0.5
    1.4142135623730951

    >>> 27 ** 0.333
    2.9967059728946346


Divisions
=========
* ``/`` - Division
* ``//`` - True division (preserving data type)
* ``%`` - Modulo division (reminder)

.. doctest::

    >>> 12 / 6
    2.0

    >>> 12 / 5
    2.4

.. doctest::

    >>> 12 // 6
    2

    >>> 12 // 5
    2

.. doctest::

    >>> 12 % 6
    0

    >>> 12 % 5
    2

Testing if value is even or odd is made with dividing using modulo (``%``) operator

.. doctest::

    >>> 12 % 2 == 0
    True

    >>> 11 % 2 == 0
    False


Increment Operators
===================
* ``+=`` - Incremental addition
* ``-=`` - Incremental subtraction
* ``*=`` - Incremental multiplication
* ``/=`` - Incremental division

.. doctest::

    >>> x = 10
    >>> x = x + 1
    >>> print(x)
    11

.. doctest::

    >>> x = 10
    >>> x += 1
    >>> print(x)
    11

.. doctest::

    >>> x = 10
    >>> x -= 1
    >>> print(x)
    9

.. doctest::

    >>> x = 1
    >>> x++
    Traceback (most recent call last):
    SyntaxError: invalid syntax

.. doctest::

    >>> x = 1
    >>> ++x
    1
