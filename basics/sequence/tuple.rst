******************
Sequence ``tuple``
******************


.. highlights::
    * Can store elements of any types
    * Immutable - cannot add, modify or remove items


Type Definition
===============
.. highlights::
    * ``()`` is used more often
    * ``tuple()`` is more readable
    * Single element ``tuple`` require comma at the end (**important!**)
    * Brackets are optional
    * Comma after last element is optional

.. code-block:: python
    :caption: ``tuple`` type definition

    data = ()
    data = tuple()

    data = 1,
    data = (1,)

    data = 1, 2
    data = (1, 2)

    data = 1, 2.0, None, False, 'Iris'
    data = (1, 2.0, None, False, 'Iris')


Getting Items
=============
.. highlights::
    * More in :ref:`Sequence Indexing` and :ref:`Sequence Slicing`

.. code-block:: python

    data = ('a', 'b', 'c', 'd')

    data[0]         # 'a'
    data[1]         # 'b'
    data[3]         # 'd'


``tuple`` vs. others
====================
.. code-block:: python

    type(1.2)        # float
    type(1,2)        # tuple
    type(1.2,)       # tuple
    type(1,2.3)      # tuple

    type(1.)         # float
    type(1,)         # tuple
    type(1.,)        # tuple
    type(.2)         # float
    type(.2,)        # tuple
    type(1.2)        # float
    type(1)          # int

    type(1.,1.)      # tuple
    type(.2,.2)      # tuple
    type(1.,.2)      # tuple

    type('foo')      # str
    type('foo',)     # tuple
    type('foo'.)     # SyntaxError: invalid syntax


When Use ``tuple`` or ``list``
==============================
Tuple:

    * is immutable
    * one contingent block of data in memory

List:

    * mutable
    * implemented in memory as list of pointers to objects
    * objects are scattered in memory


Assignments
===========

Tuple Create
------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_tuple_create.py`

:English:
    #. Create tuple ``result`` with elements:

        * 1
        * 1.1
        * 'Mark Watney'

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz tuple ``result`` z elementami:

        * 1
        * 1.1
        * 'Mark Watney'

    #. Wypisz ``result``
    #. Wypisz liczbę elementów ``result``

Tuple Many
----------
* Complexity level: medium
* Lines of code to write: 13 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/sequence_tuple_many.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create a ``tuple`` representing all Species
    #. Calculate mean for each numerical values column
    #. To convert table use multiline select with ``alt`` key in your IDE

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``tuple`` z nazwami gatunków
    #. Wylicz średnią arytmetyczną dla każdej z kolumn numerycznych
    #. Do przekonwertowania tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE

:Input:
    .. code-block:: text

        "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        "5.8", "2.7", "5.1", "1.9", "virginica"
        "5.1", "3.5", "1.4", "0.2", "setosa"
        "5.7", "2.8", "4.1", "1.3", "versicolor"
        "6.3", "2.9", "5.6", "1.8", "virginica"
        "6.4", "3.2", "4.5", "1.5", "versicolor"
        "4.7", "3.2", "1.3", "0.2", "setosa"
        "7.0", "3.2", "4.7", "1.4", "versicolor"
        "7.6", "3.0", "6.6", "2.1", "virginica"
        "4.9", "3.0", "1.4", "0.2", "setosa"
        "4.9", "2.5", "4.5", "1.7", "virginica"
        "7.1", "3.0", "5.9", "2.1", "virginica"

:The whys and wherefores:
    * Defining ``tuple``
    * Learning IDE features

:Hints:
    * ``mean = sum(...) / len(...)``
