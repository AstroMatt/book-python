.. _Loops:

************
``for`` loop
************


Syntax
======

No context syntax
-----------------
.. code-block:: python
    :caption: ``for`` loop syntax

    for ... in ... :
        ...

Generic syntax
--------------
* More on iterators in chapter :ref:`Iterators`

.. code-block:: python
    :caption: ``for`` loop generic syntax

    for my_variable in ITERATOR:
        print(my_variable)

Example
-------
.. code-block:: python
    :caption: ``for`` loop syntax: printing each number from ``list``

    DATA = ['a', 'b', 'c']

    for number in DATA:
        print(number)

    # 'a'
    # 'b'
    # 'c'

.. code-block:: python
    :caption: ``for`` loop syntax: data can be inline

    for number in ['a', 'b', 'c']:
        print(number)

    # 'a'
    # 'b'
    # 'c'


Iterating over ``str``
======================
* Iterating ``str`` will get character on each iteration

.. code-block:: python
    :caption: Iterating over ``str``

    for character in 'setosa':
        print(character)

    # s
    # e
    # t
    # o
    # s
    # a


Iterating simple collections
============================

Iterating over ``list``
-----------------------
.. code-block:: python
    :caption: Iterating over ``list``

    DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``tuple``
------------------------
.. code-block:: python
    :caption: Iterating over ``tuple``

    DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``set``
----------------------
.. code-block:: python
    :caption: Iterating over ``set``

    DATA = {5.1, 3.5, 1.4, 0.2, 'setosa'}

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Working with Generators and Iterators
=====================================

Loops with ``range``
--------------------
* ``range(0, 3)`` will generate ``(0, 1, 2)``
* ``range().start`` is inclusive
* ``range().stop`` is exclusive
* can also define ``range().step``

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

``enumerate``
-------------
* Pythonic way
* Preferred over ``i=0`` and every iteration ``i+=1``
* ``enumerate()`` will return ``counter`` and ``value`` for every iteration

.. code-block:: python
    :caption: ``enumerate()`` will return ``counter`` and ``value`` for every iteration

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA):
        print(f'{i} -> {letter}')

    # 0 -> a
    # 1 -> b
    # 2 -> c

.. code-block:: python
    :caption: ``enumerate()`` can start with custom number

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA, start=5):
        print(f'{i}, {letter}')

    # 5 -> a
    # 6 -> b
    # 7 -> c


Bad practice
============

``range(len())``
----------------
* Very common bad practice
* poor variable naming and readability
* ``range(len(...))`` will evaluate generator to calculate length
* ``DATA[i]`` lookups has ``O(n)`` complexity!!
* Does not use generator at all!

.. code-block:: python
    :caption: Bad practice

    DATA = ['a', 'b', 'c']

    for i in range(len(DATA)):
        print(DATA[i])

    # a
    # b
    # c

.. code-block:: python
    :caption: Better solution

    DATA = ['a', 'b', 'c']

    for letter in DATA:
        print(letter)

    # a
    # b
    # c


Example
=======

Create ``dict`` from two ``list``
---------------------------------
.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    output = {}

    for i, element in enumerate(keys):
        key = keys[i]
        value = values[i]
        output[key] = value

    print(output)
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    # }

``else``
========
* ``else`` will execute, if ``break`` was not used to exit the loop

.. code-block:: python

    DATA = """
    127.0.0.1       localhost
    127.0.0.1       astromatt
    10.13.37.1      nasa.gov esa.int roscosmos.ru
    255.255.255.255 broadcasthost
    ::1             localhost
    """
    hostnames = []

    for line in DATA.splitlines():
        if not line:
            continue

        ip, *hosts = line.split()
        # line.split() == ['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']
        # ip == '10.13.37.1'
        # hosts == ['nasa.gov', 'esa.int', 'roscosmos.ru']

        for record in hostnames:
            if record['ip'] == ip:
                record['hostnames'].update(hosts)
                break
        else:
            hostnames.append({
                'hostnames': set(hosts),
                'ip': ip,
            })

    print(hostnames)
    # [
    #   {'ip': '127.0.0.1', 'hostnames': {'astromatt', 'localhost'}},
    #   {'ip': '10.13.37.1', 'hostnames': {'roscosmos.ru', 'esa.int', 'nasa.gov'}},
    #   {'ip': '255.255.255.255', 'hostnames': {'broadcasthost'}},
    #   {'ip': '::1', 'hostnames': {'localhost'}},
    # ]


Assignments
===========

Counter
-------
* Filename: ``for_counter.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Dane są liczby na listingu :numref:`listing-for-counter`
#. Policz ile jest wystąpień każdej z cyfr w tej liście
#. Zwróć ``counter: Dict[int, int]``

    - klucz - cyfra
    - wartość - ilość wystąpień

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Iterowanie po liście

.. code-block:: python
    :name: listing-for-counter
    :caption: Numbers for ``dict`` counter

    [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
     0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
     2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
     1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
     4, 8, 1, 9, 6, 3]

Digit Segmentation
------------------
* Filename: ``for_segmentation.py``
* Lines of code to write: 12 lines
* Estimated time of completion: 10 min

#. Dane są liczby na listingu :numref:`listing-for-segmentation`
#. Policz ile jest wystąpień każdej z grup w tej liście

    - grupa cyfr ``małe``: cyfry z przedziału [0-2]
    - grupa cyfr ``średnie``: cyfry z przedziału [3-7]
    - grupa cyfr ``duże``: cyfry z przedziału [8-9]

#. Zwróć ``counter: Dict[str, int]``

    - klucz - grupa
    - wartość - ilość wystąpień

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Iterowanie po liście

.. code-block:: python
    :name: listing-for-segmentation
    :caption: Numbers for ``dict`` counter

    [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
     0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
     2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
     1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
     4, 8, 1, 9, 6, 3]

Get elements from nested data structure
---------------------------------------
* Filename: ``for_nested.py``
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min

#. Na podstawie ``DATA`` z :numref:`listing-for-elements-fom-nested`
#. Po odrzuceniu nagłówka iteruj po danych
#. Wyświetl na ekranie nazwy gatunków zaczynające się na "v".

.. code-block:: python
    :caption: Iris sample dataset
    :name: listing-for-elements-fom-nested

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
        (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
        (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
        (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
        (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
        (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
        (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
        (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
        (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'}),
    ]

Text analysis
-------------
* Filename: ``for_text_analysis.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min

#. Dany jest tekst przemówienia John F. Kennedy'ego "Moon Speech" wygłoszony na Rice Stadium :numref:`listing-for-moon-speech`
#. Zdania oddzielone są kropkami
#. Każde zdanie oczyść z białych znaków na początku i końcu
#. Wyrazy oddzielone są spacjami
#. Policz ile jest wyrazów w każdym zdaniu
#. Wypisz na ekranie słownik o strukturze:

    * ``Dict[str, int]``
    * klucz: zdanie
    * wartość: ilość wyrazów

#. Na końcu wypisz także ile jest łącznie w całym tekście:

    * przysłówków (słów zakończonych na "ly")
    * zdań
    * słów
    * znaków (łącznie ze spacjami wewnątrz zdań, ale bez kropek)

:The whys and wherefores:
    * Dzielenie stringów
    * Sprawdzanie długości ciągów znaków
    * Iterowanie po elementach listy
    * Nazywanie zmiennych

.. code-block:: text
    :name: listing-for-moon-speech
    :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`Kennedy1962`

    We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win
