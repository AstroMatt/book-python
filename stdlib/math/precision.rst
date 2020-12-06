.. _Math Precision:

**************
Math Precision
**************


Minimal and Maximal Values
==========================
.. code-block:: python
    :caption: Maximal and minimal ``float`` values

    import sys

    sys.float_info.min      # 2.2250738585072014e-308
    sys.float_info.max      # 1.7976931348623157e+308


Infinity
========
.. code-block:: python
    :caption: Infinity representation

    1e308                   # 1e+308
    -1e308                  # -1e+308

    1e309                   # inf
    -1e309                  # -inf

    float('inf')            # inf
    float('-inf')           # -inf

    float('Infinity')       # inf
    float('-Infinity')      # -inf


Not-a-Number
============
.. code-block:: python

    float('nan')
    # nan

    float('-nan')
    # nan


NaN vs Inf
==========
.. code-block:: python

    float('inf') + float('inf')     # inf
    float('inf') + float('-inf')    # nan
    float('-inf') + float('inf')    # nan
    float('-inf') + float('-inf')   # -inf

    float('inf') - float('inf')     # nan
    float('inf') - float('-inf')    # inf
    float('-inf') - float('inf')    # -inf
    float('-inf') - float('-inf')   # nan

    float('inf') * float('inf')     # inf
    float('inf') * float('-inf')    # -inf
    float('-inf') * float('inf')    # -inf
    float('-inf') * float('-inf')   # inf

    float('inf') / float('inf')     # nan
    float('inf') / float('-inf')    # nan
    float('-inf') / float('inf')    # nan
    float('-inf') / float('-inf')   # nan


Floating Numbers Precision
==========================
* Filename: Store values as ``int``, do operation and then divide. For example instead of 1.99 USD, store price as 199 US cents
* Filename: Use ``Decimal`` type

.. code-block:: python
    :caption: Problem

    0.1 + 0.2
    # 0.30000000000000004

    0.1 + 0.2 == 0.3
    # False


IEEE 754 standard
=================
.. figure:: img/float-anatomy.png

    What is ``float`` as defined by IEEE 754 standard

.. figure:: img/float-expression.png

    Points chart

.. figure:: img/float-mantissa-1.png

    How computer store ``float``?
    As defined by IEEE 754 standard

.. figure:: img/float-mantissa-2.png

    How to read/write ``float`` from/to memory?

.. figure:: img/float-normalized.png

    Normalized Line


Floats in Doctest
=================
.. code-block:: python

    def add_numbers(a, b):
        """
        >>> add_numbers(2.5, 1.2)
        3.7

        >>> add_numbers(0.1, 0.2)
        0.30000000000000004

        >>> add_numbers(0.1, 0.2)   # doctest: +ELLIPSIS
        0.1 + 0.2 == 0.3000...
        """
        return a + b


Decimal Type
============
.. code-block:: python

    from decimal import Decimal


    a = Decimal('0.1')
    b = Decimal('0.2')

    a + b
    # Decimal('0.3')

.. code-block:: python

    from decimal import Decimal


    a = Decimal('0.3')

    float(a)
    # 0.3

