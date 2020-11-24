.. _Loop While:

**********
Loop While
**********


Syntax
======
.. highlights::
    * Continue execution when argument is ``True``
    * Stops if argument is ``False``

.. code-block:: text
    :caption: ``while`` loop generic syntax

    while <condition>:
        <do something>

.. code-block:: python

    while True:
        pass


Convention
==========
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Generic names:

    * ``i`` - for loop counter
    * ``abort`` - for abort flags
    * ``abort_flag`` - for abort flags


Use Cases
=========
.. code-block:: python
    :caption: Never ending loop. Used in servers to wait forever for incoming connections

    while True:
        print('hello')

.. code-block:: python
    :caption: Stop conditions

    i = 0

    while i < 3:
        print(i)
        i += 1

    # 0
    # 1
    # 2

.. code-block:: python
    :caption: Iterating over sequence. Better idea for this is to use ``for`` loop. ``for`` loop supports Iterators. ``len()`` must write all ``numbers`` to memory, to calculate its length

    i = 0
    data = ['a', 'b', 'c']

    while i < len(data):
        print(i, data[i])
        i += 1

    # 0 'a'
    # 1 'b'
    # 2 'c'

.. code-block:: python
    :caption: Exit flag. Exit flag pattern is useful if you have for example multi-threaded application

    print('Ignition sequence started')
    abort = False
    i = 10

    while not abort:
        print(i)
        i -= 1

        if i == 6:
            print('Fuel leak detected. Abort, Abort, Abort!')
            abort = True

    # Ignition sequence started
    # 10
    # 9
    # 8
    # 7
    # Fuel leak detected. Abort, Abort, Abort!


Force Exit the Loop
===================
.. code-block:: python
    :caption: Force exit the loop using ``break`` keyword

    print('Ignition sequence started')
    i = 10

    while True:
        print(i)
        i -= 1

        if i == 6:
            print('Fuel leak detected. Abort, Abort, Abort!')
            break

    # Ignition sequence started
    # 10
    # 9
    # 8
    # 7
    # Fuel leak detected. Abort, Abort, Abort!

.. code-block:: python
    :caption: Exiting the loop using ``break`` keyword

    while True:
        number = input('Type number: ')

        if not number:
            # if user hit enter
            # without typing a number
            break


Force Skip Iteration
====================
.. highlights::
    * if ``continue`` is encountered, it will jump to next loop iteration

.. code-block:: python

    TEXT = """
        # "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12
        # Source: http://er.jsc.nasa.gov/seh/ricetalk.htm
        We choose to go to the Moon.
        We choose to go to the Moon in this decade and do the other things.
        Not because they are easy, but because they are hard.
        Because that goal will serve to organize and measure the best of our energies a skills.
        Because that challenge is one that we are willing to accept.
        One we are unwilling to postpone.
        And one we intend to win
    """

    data = TEXT.splitlines()
    i = 0

    while i < len(data):
        line = data[i].strip()
        i += 1

        if len(line) == 0:
            continue

        if line.startswith('#'):
            continue

        print(line)

    # We choose to go to the Moon.
    # We choose to go to the Moon in this decade and do the other things.
    # Not because they are easy, but because they are hard.
    # Because that goal will serve to organize and measure the best of our energies a skills.
    # Because that challenge is one that we are willing to accept.
    # One we are unwilling to postpone.
    # And one we intend to win

.. code-block:: python
    :caption: Force skip iteration using ``continue`` keyword

    all_astronauts = ['Mark Watney', 'Jan Twardowski', 'Melissa Lewis', 'José Jiménez']
    assigned_to_mission = ['Mark Watney', 'Melissa Lewis']
    i = 0

    while i < len(all_astronauts):
        name = all_astronauts[i]
        i += 1

        if name not in assigned_to_mission:
            continue

        print(name)

    # Mark Watney
    # Melissa Lewis

.. code-block:: python
    :caption: Force skip iteration using ``continue`` keyword

    i = 0

    while i < 10:
        print(i, end=', ')
        i += 1

        if i % 3:
            continue

        print(end='\n')

    # 0, 1, 2,
    # 3, 4, 5,
    # 6, 7, 8,
    # 9,


Assignments
===========

.. literalinclude:: solution/loop_while_int.py
    :caption: :download:`Solution <solution/loop_while_int.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_while_float.py
    :caption: :download:`Solution <solution/loop_while_float.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_while_translate.py
    :caption: :download:`Solution <solution/loop_while_translate.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_while_input.py
    :caption: :download:`Solution <solution/loop_while_input.py>`
    :end-before: # Solution
