.. _Loop For:

********
Loop For
********


Syntax
======
.. highlights::
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


Iterating Sequences
===================
.. code-block:: python
    :caption: Iterating over ``str`` will get character on each iteration. Suggested variable name: ``letter``.

    for obj in 'setosa':
        print(obj)

    # s
    # e
    # t
    # o
    # s
    # a

.. code-block:: python
    :caption: Iterating over ``list`` will get one element on each iteration. Suggested variable name: ``value``.

    DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

.. code-block:: python
    :caption: Iterating over ``tuple`` will get one element on each iteration. Suggested variable name: ``value``.

    DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

.. code-block:: python
    :caption: Iterating over ``set`` will get one element on each iteration.  Suggested variable name: ``value``.

    DATA = {5.1, 3.5, 1.4, 0.2, 'setosa'}

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

.. code-block:: python
    :caption: Iterating over ``frozenset`` will get one element on each iteration.  Suggested variable name: ``value``.

    DATA = frozenset({5.1, 3.5, 1.4, 0.2, 'setosa'})

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Range
=====
.. highlights::
    * ``range(start, stop, step)``
    * ``range(0,3)`` will generate ``(0, 1, 2)``
    * ``start`` is inclusive, default: ``0``
    * ``stop`` is exclusive, required
    * ``step`` default: ``1``

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

    range(0, 5)
    # range(0, 5)

.. code-block:: python
    :caption: Loops with ``range``

    for number in range(0, 3):
        print(number)

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

    for _ in range(0,10):
        print('-', end='')

    # ----------


Assignments
===========

.. literalinclude:: solution/loop_for_count.py
    :caption: :download:`Solution <solution/loop_for_count.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_for_counter.py
    :caption: :download:`Solution <solution/loop_for_counter.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_for_segmentation.py
    :caption: :download:`Solution <solution/loop_for_segmentation.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_for_newline.py
    :caption: :download:`Solution <solution/loop_for_newline.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_for_translate.py
    :caption: :download:`Solution <solution/loop_for_translate.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_for_months.py
    :caption: :download:`Solution <solution/loop_for_months.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_for_text.py
    :caption: :download:`Solution <solution/loop_for_text.py>`
    :end-before: # Solution
