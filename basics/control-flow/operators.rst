Conditional Operators
=====================


Equals
======
* ``==`` - ``eq`` (equals)

Comparing ``str``:

.. code-block:: python

    'Monty Python' == 'Python'      # False
    'Python' == 'Python'            # True
    'python' == 'Python'            # False

Comparing ``tuple``:

.. code-block:: python

    (1, 2, 3) == (1, 2)             # False
    (1, 2) == (1, 2)                # True
    (1, 2) == (2, 1)                # False

Comparing ``list``:

.. code-block:: python

    [1, 2, 3] == [1, 2]             # False
    [1, 2] == [1, 2]                # True
    [1, 2] == [2, 1]                # False

Comparing ``set``:

.. code-block:: python

    {1, 2, 3} == {1, 2}             # False
    {1, 2} == {1, 2}                # True
    {1, 2} == {2, 1}                # True

.. code-block:: python

    (1,2) == [1,2]                  # False
    (1,2) == {1,2}                  # False
    1,2 == {1,2}                    # (1, False)


Not-Equals
==========
* ``!=`` - ``ne`` (not-equals)

Comparing ``str``:

.. code-block:: python

    'Monty Python' != 'Python'      # True
    'Python' != 'Python'            # False
    'python' != 'Python'            # True

Comparing ``tuple``:

.. code-block:: python

    (1, 2, 3) != (1, 2)             # True

Comparing ``list``:

.. code-block:: python

    [1, 2, 3] != [1, 2]             # True

Comparing ``set``:

.. code-block:: python

    {1, 2, 3} != {1, 2}             # True


Greater Than
============
* ``>`` - ``gt`` (greater than)
* Set uses ``>`` for ``set.issuperset()``

.. code-block:: python

    'a' > 'b'       # False
    'b' > 'a'       # True

    'abc' > 'ab'    # True
    'abc' > 'abc'   # False
    'abc' > 'abcd'  # False

    'def' > 'abc'   # True
    'abc' > 'xy'    # False
    'abc' > 'xyz'   # False

.. code-block:: python

    (3, 9) > (3, 8)         # True
    (3, 8, 3) > (3, 7, 6)   # True
    (3, 8) > (3, 9)         # False

    (2, 7) > (3, 6)         # False
    (3, 6) > (2, 7)         # True

.. code-block:: python

    [3, 9] > [3, 8]         # True
    [3, 8, 3] > [3, 7, 6]   # True
    [3, 8] > [3, 9]         # False

    [2, 7] > [3, 6]         # False
    [3, 6] > [2, 7]         # True


Examples
========
.. code-block:: python

    import sys

    print(sys.version_info)
    # sys.version_info(major=3, minor=8, micro=3, releaselevel='final', serial=0)

    sys.version_info > (3, 7)       # True
    sys.version_info > (3, 8)       # True
    sys.version_info > (3, 9)       # False

    sys.version_info > (3, 8, 2)    # True
    sys.version_info > (3, 8, 3)    # True
    sys.version_info > (3, 8, 4)    # False


Operator Precedence
===================
.. csv-table:: Operator precedence
    :header-rows: 1
    :widths: 25, 75

    "Operator", "Description"
    "``lambda``", "Lambda expression"
    "``if``, ``elif``, ``else``", "Conditional expression"
    "``and``", "Boolean AND"
    "``or``", "Boolean OR"
    "``not x``", "Boolean NOT"
    "``in``, ``not in``, ``is``, ``is not``,

    ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``", "Comparisons, including membership tests and identity tests"
    "``|``", "Bitwise OR"
    "``^``", "Bitwise XOR"
    "``&``", "Bitwise AND"
    "``<<``, ``>>``", "Shifts"
    "``**``", "Exponentiation"
    "``*``, ``@``, ``/``, ``//``, ``%``", "Multiplication, matrix multiplication, division, floor division, remainder"
    "``+``, ``-``", "Addition and subtraction"
    "``+x``, ``-x``, ``~x``", "Positive, negative, bitwise NOT"
    "``await``", "Await expression"
    "``x[index]``, ``x[index:index]``,

    ``x(arguments...)``, ``x.attribute``", "Subscription, slicing, call, attribute reference"
    "``(expressions...)``, ``[expressions...]``,

    ``{key: value...}``, ``{expressions...}``", "Binding or tuple display, list display, dictionary display, set display"


Assignments
===========

.. literalinclude:: assignments/controlflow_operators_modulo.py
    :caption: :download:`Solution <assignments/controlflow_operators_modulo.py>`
    :end-before: # Solution
