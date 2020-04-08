*********
Operators
*********


Logic Operators
===============
* ``x < y`` - Less than
* ``x <= y`` - Less or equal
* ``x > y`` - Greater than
* ``x >= y`` - Greater or equal
* ``x == y`` - Equals
* ``x != y`` - Not Equals
* ``x is None`` - Object has value
* ``x is not None`` - Object don't have value

.. code-block:: python

    10 < 2              # False
    10 <= 2             # False
    10 > 2              # True
    10 >= 2             # True
    10 == 2             # False
    10 != 2             # True
    10 is None          # False
    10 is not None      # True


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
    10 / 2              # 5

Multiplication, Power and Root
==============================
* ``**`` - Power

.. code-block:: python
    :caption: ``n-th`` power of the number

    10 ** 2             # 100
    2 ** -1             # 0.5
    1.337 ** 3          # 2.389979753

    pow(10, 2)          # 100
    pow(2, -1)          # 0.5
    pow(1.337, 3)       # 2.389979753

.. code-block:: python
    :caption: ``n-th`` root of the number

    4 ** 0.5            # 2.0
    2 ** 0.5            # 1.4142135623730951

    pow(4, 0.5)         # 2.0
    pow(2, 0.5)         # 1.4142135623730951


Divisions
=========
* ``/`` - Division
* ``//`` - True division
* ``%`` - Modulo division (reminder)

.. code-block:: python

    10 / 2              # 5
    10 / 4              # 2.5

    10 // 2             # 5
    10 // 4             # 2

    10 % 2              # 0
    10 % 4              # 2

.. code-block:: python
    :caption: Even vs odd

    10 % 2 == 0         # True
    11 % 2 == 0         # False


Increment Operators
===================
* ``+=`` - Incremental addition
* ``-=`` - Incremental subtraction
* ``*=`` - Incremental multiplication
* ``/=`` - Incremental division

.. code-block:: python

    value = 10
    value += 1

    print(value)
    # 11

.. code-block:: python

    value = 10
    value -= 1

    print(value)
    # 9

.. code-block:: python

    value = 10
    value *= 2

    print(value)
    # 20

.. code-block:: python

    value = 10
    value /= 2

    print(value)
    # 5
