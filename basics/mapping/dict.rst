.. _Mapping Dict:

************
Mapping Dict
************


Rationale
=========
.. highlights::
    * ``dict`` are key-value storage
    * key lookup is very efficient ``O(1)``
    * Mutable - can add, remove, and modify items


Definition
==========
* ``{}`` is used more often
* ``dict()`` is more readable
* Comma after last element is optional
* Since Python 3.7: ``dict`` keeps order of elements
* Before Python 3.7: ``dict`` order is not ensured!!
* https://mail.python.org/pipermail/python-dev/2017-December/151283.html

.. code-block:: python

    data = {}
    data = dict()

.. code-block:: python

    data = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon'}

    data = {
        1961: ['First Russian Space Flight', 'First US Space Flight'],
        1969: ['First Step on the Moon']}

    data = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    data = dict(
        commander='Melissa Lewis',
        botanist='Mark Watney',
        chemist='Alex Vogel')

.. code-block:: python
    :caption: Duplicating items are overridden by latter

    data = {
        'commander': 'Melissa Lewis',
        'commander': 'Jan Twardowski'}

    data
    # {'commander': 'Jan Twardowski'}


GetItem
=======
.. highlights::
    * ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
    * ``.get()`` returns ``None`` if key not found
    * ``.get()`` can have default value, if key not found

.. code-block:: python
    :caption: Getitem Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew['commander']
    # Melissa Lewis

    crew['pilot']
    # Traceback (most recent call last):
    # KeyError: 'pilot'

.. code-block:: python
    :caption: Get Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew.get('commander')
    # Melissa Lewis

    crew.get('pilot')
    # None

    crew.get('pilot', 'not assigned')
    # 'not assigned'

.. code-block:: python
    :caption: Getting keys other than ``str``

    calendarium = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon'}

    calendarium[1961]
    # 'First Human Space Flight'

    calendarium.get(1961)
    # 'First Human Space Flight'

    calendarium['1961']
    # Traceback (most recent call last):
    # KeyError: '1961'

    calendarium.get('1961')
    # None

    calendarium.get('1961', 'unknown')
    # 'unknown'


Get Keys, Values and Key-Value Pairs
====================================
.. highlights::
    * Key can be any hashable object

In Python 2, the methods items(), keys() and values() used to "take a snapshot" of the dictionary contents and return it as a list. It meant that if the dictionary changed while you were iterating over the list, the contents in the list would not change. In Python 3, these methods return a view object whose contents change dynamically as the dictionary changes. Therefore, in order for the behavior of iterations over the result of these methods to remain consistent with previous versions, an additional call to list() has to be performed in Python 3 to "take a snapshot" of the view object contents. [Hamidi2017]_

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew.keys()
    # dict_keys(['commander', 'botanist', 'chemist'])

    crew.values()
    # dict_values(['Melissa Lewis', 'Mark Watney', 'Alex Vogel'])

    crew.items()
    # dict_items([('commander', 'Melissa Lewis'), ('botanist', 'Mark Watney'), ('chemist', 'Alex Vogel')])

    list(crew.keys())
    # ['commander', 'botanist', 'chemist']

    list(crew.values())
    # ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    list(crew.items())
    # [('commander', 'Melissa Lewis'),
    #  ('botanist', 'Mark Watney'),
    #  ('chemist', 'Alex Vogel')]


Set Item
========
.. highlights::
    * Adds if value not exist
    * Updates if value exist

.. code-block:: python
    :caption: Set Item Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew['pilot'] = 'Rick Martinez'
    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez'}

    crew['commander'] = 'Jan Twardowski'
    print(crew)
    # {'commander': 'Jan Twardowski',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez'}

.. code-block:: python
    :caption: Update Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew.update(pilot='Rick Martinez')
    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez'}

    crew.update(commander='Jan Twardowski')
    print(crew)
    # {'commander': 'Jan Twardowski',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez'}

.. code-block:: python
    :caption: Update Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    new = {
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    crew.update(new)
    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}


Delete Item
===========
.. code-block:: python
    :caption: Pop Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel',
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    left_alone_on_mars = crew.pop('botanist')

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

    print(left_alone_on_mars)
    # 'Mark Watney'

.. code-block:: python
    :caption: Popitem Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    last = crew.popitem()

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney'}

    print(last)
    # ('chemist', 'Alex Vogel')

.. code-block:: python
    :caption: Del Keyword

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    del crew['chemist']

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney'}


Merge
=====
* Merge (``|``) and update (``|=``) operators have been added to the built-in dict class.

.. versionadded:: Python 3.9
    :pep:`584` -- Add Union Operators To dict


.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    new = {
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    everyone = crew | new

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel'}

    print(new)
    # {'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

    print(everyone)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    new = {
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    crew |= new

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

    print(new)
    # {'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}


GetItem and Slice
=================
.. highlights::
    * GetItem with index on ``dict`` is not possible
    * Slicing on ``dict`` is not possible

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew[0]             # KeyError: 0
    crew[1]             # KeyError: 1
    crew[2]             # KeyError: 2
    crew[-0]            # KeyError: 0
    crew[-1]            # KeyError: -1
    crew[-2]            # KeyError: -2
    crew[1:2]           # TypeError: unhashable type: 'slice'
    crew[:2]            # TypeError: unhashable type: 'slice'
    crew[::2]           # TypeError: unhashable type: 'slice'

.. code-block:: python

    crew = {
        0: 'Melissa Lewis',
        1: 'Mark Watney',
        2: 'Alex Vogel'}

    crew[0]             # 'Melissa Lewis'
    crew[1]             # 'Mark Watney'
    crew[2]             # 'Alex Vogel'
    crew[-0]            # 'Melissa Lewis'
    crew[-1]            # KeyError: -1
    crew[-2]            # KeyError: -2
    crew[1:2]           # TypeError: unhashable type: 'slice'
    crew[:2]            # TypeError: unhashable type: 'slice'
    crew[::2]           # TypeError: unhashable type: 'slice'


Dict or Set
===========
.. highlights::
    * Both ``set`` and ``dict`` keys must be hashable
    * Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
    * Despite similar syntax, they are different types

.. code-block:: python

    {1, 2}            # set
    {1: 2}            # dict

    {1, 2, 3, 4}      # set
    {1: 2, 3: 4}      # dict

.. code-block:: python
    :caption: Empty ``dict`` and empty ``set``

    data = {1: 1}
    data.pop(1)
    # {}

    data = {1}
    data.pop()
    # set()

.. code-block:: python
    :caption: Differences

    data = {1: 1}
    isinstance(data, set)          # False
    isinstance(data, dict)         # True

    data = {1}
    isinstance(data, set)          # True
    isinstance(data, dict)         # False

    data = {}
    isinstance(data, set)          # False
    isinstance(data, dict)         # True


Length
======
.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}


    len(crew)
    # 3

    len(crew.keys())
    # 3

    len(crew.values())
    # 3

    len(crew.items())
    # 3


Examples
========
.. code-block:: python

    git = {
        'ce16a8ce': 'commit/1',
        'cae6b510': 'commit/2',
        '895444a6': 'commit/3',
        'aef731b5': 'commit/4',
        '4a92bc79': 'branch/master',
        'b3bbd85a': 'tag/v1.0',
    }


Assignments
===========

.. literalinclude:: assignments/mapping_dict_define.py
    :caption: :download:`Solution <assignments/mapping_dict_define.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_dict_items.py
    :caption: :download:`Solution <assignments/mapping_dict_items.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_dict_get.py
    :caption: :download:`Solution <assignments/mapping_dict_get.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_dict_translate.py
    :caption: :download:`Solution <assignments/mapping_dict_translate.py>`
    :end-before: # Solution


References
==========
.. [Hamidi2017] Frédéric Hamidi. Why does Python 3 need dict.items to be wrapped with list()? https://stackoverflow.com/a/17695716
