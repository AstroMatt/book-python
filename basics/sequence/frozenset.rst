.. _Sequence Frozenset:

******************
Sequence Frozenset
******************


Rationale
=========
.. highlights::
    * Only unique values
    * Immutable - cannot add, modify or remove items
    * Can store elements of any **hashable** types
    * Has all ``set`` methods such as ``.intersect()``, ``.subset()`` ``.union()``, etc.
    * One solid block in memory
    * Frozenset is unordered data structure
    * Do not support getitem
    * Do not support slice


Type Definition
===============
.. highlights::
    * Defining only with ``frozenset()`` - no short syntax
    * Comma after last element of a one element frozenset is optional
    * Brackets are required

.. code-block:: python
    :caption: ``set`` type definition

    data = frozenset()

    data = frozenset({1})
    data = frozenset({1, 2, 3})
    data = frozenset({1.1, 2.2, 3.3})
    data = frozenset({True, False})
    data = frozenset({'a', 'b', 'c'})
    data = frozenset({'a', 1, 2.2, True, None})


Type Casting
============
.. highlights::
    * ``frozenset()`` converts argument to ``frozenset``

.. code-block:: python

    data = 'abcd'
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = ('a', 'b', 'c', 'd')
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = {'a', 'b', 'c', 'd'}
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = frozenset({'a', 'b', 'c', 'd'})
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = [1, 2, 3, [4, 5]]
    frozenset(data)
    # TypeError: unhashable type: 'list'

.. code-block:: python

    data = [1, 2, 3, (4, 5)]
    frozenset(data)
    # frozenset({(4, 5), 1, 2, 3})


Frozenset or Set
================
Both:

    * unordered
    * impossible to getitem and slice
    * unique elements
    * only **hashable** elements

Frozenset:

    * immutable
    * one contingent block of data in memory

Set:

    * mutable
    * implemented in memory as list of pointers to objects
    * objects are scattered in memory


Assignments
===========

Sequence Frozenset Create
-------------------------
* Assignment name: Sequence Frozenset Create
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_frozenset_create.py`
* Last update: 2020-10-01

:English:
    #. Create frozenset ``result`` with elements:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz frozenset ``result`` z elementami:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Wypisz ``result``
    #. Wypisz liczbę elementów ``result``

:The whys and wherefores:
    * Defining ``list``

Sequence Frozenset Newline
--------------------------
* Assignment name: Sequence Frozenset Newline
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_frozenset_newline.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: str``
    #. Use ``str.join()`` to join lines of text with newline (``\n``) character
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: str``
    #. Użyj ``str.join()`` aby połączyć linie tekstu znakiem końca linii (``\n``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = frozenset({
            'We choose to go to the Moon.',
            'We choose to go to the Moon in this decade and do the other things.',
            'Not because they are easy, but because they are hard.'})

:Output:
    .. code-block:: python

        result: str
        # 'We choose to go to the Moon.\nWe choose to go to the Moon in this decade and do the other things.\nNot because they are easy, but because they are hard.'
