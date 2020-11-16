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

.. code-block:: python

    10 < 2              # False
    10 <= 2             # False
    10 > 2              # True
    10 >= 2             # True
    10 == 2             # False
    10 != 2             # True

.. code-block:: python

    x = 10
    y = 2

    x >= 2
    # True


Arithmetic Operators
====================
* ``+`` - Addition
* ``-`` - Subtraction
* ``*`` - Multiplication
* ``/`` - Division

.. code-block:: python

    10 + 2              # 12
    10 - 2              # 8
    10 * 2              # 20
    10 / 2              # 5.0

.. code-block:: python

    x = 10
    y = 2

    x + y
    # 12


Power and Root
==============
* ``**`` - Power

.. code-block:: python
    :caption: ``n-th`` power of the number

    10 ** 2             # 100
    2 ** -1             # 0.5
    1.337 ** 3          # 2.389979753

.. code-block:: python
    :caption: ``n-th`` root of the number

    4 ** (1/2)          # 2.0
    2 ** (1/2)          # 1.4142135623730951
    27 ** (1/3)         # 3.0

    4 ** 0.5            # 2.0
    2 ** 0.5            # 1.4142135623730951
    27 ** 0.333         # 2.9967059728946346


Divisions
=========
* ``/`` - Division
* ``//`` - True division (preserving data type)
* ``%`` - Modulo division (reminder)

.. code-block:: python

    12 / 6              # 2.0
    12 / 5              # 2.4

    12 // 6             # 2
    12 // 5             # 2

    12 % 6              # 0
    12 % 5              # 2

.. code-block:: python
    :caption: Even vs odd

    12 % 2 == 0         # True
    11 % 2 == 0         # False


Increment Operators
===================
* ``+=`` - Incremental addition
* ``-=`` - Incremental subtraction
* ``*=`` - Incremental multiplication
* ``/=`` - Incremental division

.. code-block:: python

    x = 10
    x = x + 1

    print(x)
    # 11

.. code-block:: python

    x = 10
    x += 1

    print(x)
    # 11

.. code-block:: python

    x = 10
    x -= 1

    print(x)
    # 9

.. doctest::

    >>> x++
      File "<stdin>", line 1
        x++
          ^
    SyntaxError: invalid syntax

.. doctest::

    >>> ++x
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'x' is not defined
    >>> x = 1
    >>> ++x
    1
