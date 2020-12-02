.. _Type Int:

********
Type Int
********


Type Definition
===============
.. highlights::
    * Python 3 dynamically extends ``int`` when it's too big, hence there is no maximal or minimal ``int`` value
    * You can use ``_`` for easier read especially with big numbers

.. code-block:: python
    :caption: ``int`` Type Definition

    data = 1337                 # 1337
    data = +1337                # -1337
    data = -1337                # -1337

.. code-block:: python
    :caption: You can use ``_`` for easier read especially with big numbers

    million = 1000000           # 1000000
    million = 1_000_000         # 1000000


Type Casting
============
.. highlights::
    * ``int()`` - converts argument to ``int``
    * ``int()`` - does not round numbers
    * ``int()`` - works with base 2, 8, 10, 16

.. code-block:: python
    :caption: ``int()`` - does not round numbers

    int(1.001)                  # 1
    int(1.999)                  # 1

.. code-block:: python
    :caption: ``int()`` - converts argument to ``int``

    int(1)                      # 1
    int(+1)                     # 1
    int(-1)                     # -1

    int(1.337)                  # 1
    int(+1.1337)                # 1
    int(-1.337)                 # -1

    int('1')                    # 1
    int('+1')                   # 1
    int('-1')                   # -1
    int('1_000_000')            # 1000000

    int('1.337')                # ValueError: invalid literal for int() with base 10: '13.37'
    int('+1.337')               # ValueError: invalid literal for int() with base 10: '+13.37'
    int('-1.337')               # ValueError: invalid literal for int() with base 10: '-13.37'

    int('1,337')                # ValueError: invalid literal for int() with base 10: '13,37'
    int('+1,337')               # ValueError: invalid literal for int() with base 10: '+13,37'
    int('-1,337')               # ValueError: invalid literal for int() with base 10: '-13,37'

.. code-block:: python
    :caption: ``int()`` - works with base 2, 8, 10, 16

    int('100', base=2)          # 4
    int('100', base=8)          # 64
    int('100', base=10)         # 100
    int('100', base=16)         # 256

    int('0b1000101', base=2)    # 69
    int('0o105', base=8)        # 69
    int('69', base=10)          # 69
    int('0x45', base=16)        # 69

    int('0o754', base=8)        # 492
    int('0x69', base=16)        # 105
    int('0x3C', base=16)        # 60


Type Checking
=============
.. highlights::
    * ``type()`` - Returns type of an argument

.. code-block:: python
    :caption: ``type()`` - Returns type of an argument

    type(1)                     # <class 'int'>
    type(+1)                    # <class 'int'>
    type(-1)                    # <class 'int'>

    type(0)                     # <class 'int'>
    type(+0)                    # <class 'int'>
    type(-0)                    # <class 'int'>


Assignments
===========

.. literalinclude:: assignments/type_int_add.py
    :caption: :download:`Solution <assignments/type_int_add.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_sub.py
    :caption: :download:`Solution <assignments/type_int_sub.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_mul.py
    :caption: :download:`Solution <assignments/type_int_mul.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_truediv.py
    :caption: :download:`Solution <assignments/type_int_truediv.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_time.py
    :caption: :download:`Solution <assignments/type_int_time.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_bits.py
    :caption: :download:`Solution <assignments/type_int_bits.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_bytes.py
    :caption: :download:`Solution <assignments/type_int_bytes.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_bandwidth.py
    :caption: :download:`Solution <assignments/type_int_bandwidth.py>`
    :end-before: # Solution
