*******
``int``
*******


Defining ``int``
================
* Python 3 dynamically extends ``int``, when it's too big
* In Python 3 there is not maximal ``int`` value
* You can use ``_`` for easier read especially with big numbers

.. code-block:: python

    value = 30              # 30
    value = -30             # -30

.. code-block:: python

    million = 1000000       # 1000000
    million = 1_000_000     # 1000000


Converting to ``int``
=====================
* Also known as "type casting"
* ``int()`` converts argument to ``int``

.. code-block:: python

    int(10)                 # 10

.. code-block:: python

    int(10.0)               # 10
    int(10.9)               # 10

.. code-block:: python

    int(1.23)               # 1
    int(-1.23)              # -1

.. code-block:: python

    int('10')               # 10
    int('10.5')             # ValueError: invalid literal for int() with base 10: ' 10.5'


Numerical Operators
===================

Add and subtract
----------------
.. csv-table:: Add and subtract
    :header: "Operand", "Description"
    :widths: 15, 85

    "``-x``", "``x`` negation"
    "``+x``", "``x``"
    "``x + y``", "Sum ``x`` and ``y``"
    "``x - y``", "Subtract ``x`` and ``y``"

Multiplication
--------------
.. csv-table:: Numerical types operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``x * y``", "Multiply ``x`` and ``y``"
    "``x ** y``", "``x`` to the power of ``y``"

Division
--------
.. csv-table:: Numerical types operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``x / y``", "Divide ``x`` and ``y``"
    "``x // y``", "Quotient of division ``x`` by ``y``"
    "``x % y``", "Modulo. Reminder of division ``x`` by ``y``"

Incremental assignments
-----------------------
* Add ``y`` to ``x`` and assign result to ``x`` as new value

.. csv-table:: Incremental assignments
    :header: "Operand", "Description"
    :widths: 15, 85

    "``x += y``", "Add and assign"
    "``x -= y``", "Subtract and assign"
    "``x *= y``", "Multiply and assign"
    "``x /= y``", "Divide and assign"


Numeric Functions
=================

Absolute value
--------------
.. code-block:: python

    abs(1)          # 1
    abs(-1)         # 1

Number to the ``n-th`` power
----------------------------
.. code-block:: python

    pow(2, 2)       # 4
    pow(3, 4)       # 81
    pow(-1, 2)      # 1

.. code-block:: python

    2 ** 2          # 4
    3 ** 4          # 81
    -1 ** 2         # 1
