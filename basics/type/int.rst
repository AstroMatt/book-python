.. _Type Int:

********
Type Int
********


Type Definition
===============
.. highlights::
    * In Python 3 there is not maximal ``int`` value
    * Python 3 dynamically extends ``int``, when it's too big
    * You can use ``_`` for easier read especially with big numbers

.. code-block:: python
    :caption: ``int`` Type Definition

    data = 1337                 # 1337
    data = -1337                # -1337

.. code-block:: python

    million = 1000000           # 1000000
    million = 1_000_000         # 1000000


Type Casting
============
.. highlights::
    * ``int()`` - converts argument to ``int``
    * ``int()`` - does not round numbers

.. code-block:: python
    :caption: ``int()`` converts argument to ``int``

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

    int('0x69', base=16)        # 105
    int('0x3C', base=16)        # 60
    int('0o754', base=8)        # 492


Type Checking
=============
.. highlights::
    * ``type()`` - Returns type of an argument

.. code-block:: python

    type(1)                     # <class 'int'>
    type(+1)                    # <class 'int'>
    type(-1)                    # <class 'int'>

    type(0)                     # <class 'int'>
    type(+0)                    # <class 'int'>
    type(-0)                    # <class 'int'>


References
==========
.. [MSLREMS] Centro de Astrobiología (CSIC-INTA). Rover Environmental Monitoring Station, Mars Science Laboratory (NASA). 2019. Accessed: 2019-08-06


Assignments
===========

.. literalinclude:: solution/type_int_add.py
    :caption: :download:`Solution <solution/type_int_add.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_sub.py
    :caption: :download:`Solution <solution/type_int_sub.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_mul.py
    :caption: :download:`Solution <solution/type_int_mul.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_truediv.py
    :caption: :download:`Solution <solution/type_int_truediv.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_time.py
    :caption: :download:`Solution <solution/type_int_time.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_bits.py
    :caption: :download:`Solution <solution/type_int_bits.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_bytes.py
    :caption: :download:`Solution <solution/type_int_bytes.py>`
    :end-before: # Solution

.. literalinclude:: solution/type_int_bandwidth.py
    :caption: :download:`Solution <solution/type_int_bandwidth.py>`
    :end-before: # Solution
