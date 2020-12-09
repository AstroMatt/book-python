.. _Loop For:

********
Loop For
********


Syntax
======
* ``ITERABLE`` must implement ``iterator`` interface
* More information in :ref:`Protocol Iterator`

.. code-block:: text
    :caption: ``for`` loop syntax

    for <variable> in <iterable>:
        <do something>

.. code-block:: python

    for digit in [1, 2, 3]:
        pass


Convention
==========
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Prefer locally meaningful name over generic names
* Generic names:

    * ``obj`` - generic name (in Python everything is an object)
    * ``element`` - generic name
    * ``item`` - generic name
    * ``x`` - ok for oneliners, bad for more than one line
    * ``e`` - ok for oneliners, bad for more than one line
    * ``l`` - bad
    * ``o`` - bad
    * ``d`` - bad (for digit)

* Locally meaningful name:

    * ``letter``
    * ``feature``
    * ``digit``
    * ``person``
    * ``color``
    * ``username``
    * etc.

* Special meaning (by convention):

    * ``i`` - for loop counter
    * ``_`` - if value is not used

.. code-block:: python

    for digit in [1, 2, 3]:
        print(digit)

.. code-block:: python

    for x in [1, 2, 3]:
        print(x)

.. code-block:: python

    for i in range(0,5):
        print(i)

.. code-block:: python

    for _ in range(10):
        spawn_thread()


Iterating Sequences
===================
* Iterating works for builtin sequences:

    * ``str``
    * ``bytes``
    * ``list``
    * ``tuple``
    * ``set``
    * ``frozenset``
    * ``dict`` (More information :ref:`Loop Dict`)

.. code-block:: python

    for letter in 'setosa':
        print(letter)

    # s
    # e
    # t
    # o
    # s
    # a

.. code-block:: python

    DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

    for value in DATA:
        print(value)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Range
=====
* ``range(start, stop, step)``
* ``start`` is inclusive, default: ``0``
* ``stop`` is exclusive, required
* ``step`` default: ``1``

.. code-block:: python

    range(0, 5)
    # range(0, 5)

.. code-block:: python

    list(range(5))
    # [0, 1, 2, 3, 4]

    list(range(0, 5))
    # [0, 1, 2, 3, 4]

    list(range(0, 5, 1))
    # [0, 1, 2, 3, 4]

    list(range(0, 5, 2))
    # [0, 2, 4]

.. code-block:: python
    :caption: Loops with ``range``

    for i in range(0, 3):
        print(i)

    # 0
    # 1
    # 2

.. code-block:: python
    :caption: Loops with ``range``

    for number in range(4, 11, 2):
        print(number)

    # 4
    # 6
    # 8
    # 10

.. code-block:: python

    for _ in range(10):
        print('-', end='')

    # ----------


Nested Loops
============
.. code-block:: python

    for row in [1, 2, 3]:
        print()

        for column in ['A', 'B', 'C']:
            print(f'{column}{row}', end=' ')

    # A1 B1 C1
    # A2 B2 C2
    # A3 B3 C3


Assignments
===========

.. literalinclude:: assignments/loop_for_count.py
    :caption: :download:`Solution <assignments/loop_for_count.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_counter.py
    :caption: :download:`Solution <assignments/loop_for_counter.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_segmentation.py
    :caption: :download:`Solution <assignments/loop_for_segmentation.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_newline.py
    :caption: :download:`Solution <assignments/loop_for_newline.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_translate.py
    :caption: :download:`Solution <assignments/loop_for_translate.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_months.py
    :caption: :download:`Solution <assignments/loop_for_months.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_text.py
    :caption: :download:`Solution <assignments/loop_for_text.py>`
    :end-before: # Solution
