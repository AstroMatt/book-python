.. _Conditional Expressions:

***********************
Conditional Expressions
***********************


Conjunction
===========
.. code-block:: python
    :caption: Inside joke (see :ref:`José Jiménez`)

    firstname = 'Mark'
    lastname = 'Watney'

    if firstname == 'Mark' and lastname == 'Watney':
        print('Hello Space Pirate')
    else:
        print('Sorry, astronauts only')
    # Hello Space Pirate


Disjunction
===========
.. code-block:: python

    name = 'Watney'

    if name == 'Watney' or name == 'Twardowski':
        print('Hello astronaut')
    else:
        print('Sorry, astronauts only')
    # Hello astronaut


Boolean Algebra
===============
.. highlights::
    * Use parenthesis for explicit order

.. code-block:: python

    firstname = 'José'
    lastname = 'Jiménez'

    if (firstname == 'Mark' and lastname == 'Watney') \
            or (firstname == 'Jan' and lastname == 'Twardowski') \
            or (firstname == 'Melissa' and lastname == 'Lewis'):

        print('Hello astronaut')
    else:
        print('Sorry, astronauts only')

    # Sorry, astronauts only

.. code-block:: python
    :caption: Complex conditions

    for line in file:
        if line and (not line.startswith('#') or not line.isspace()):
            ...


    for line in file:
        if len(line) == 0:
            continue

        if line.startswith('#'):
            continue

        if line.isspace():
            continue

        ...


Contains
========
.. code-block:: python

    text = 'Monty Python'

    if 'Python' in text:
        print('Yes')
    else:
        print('No')
    # Yes

.. code-block:: python

    crew = ['Lewis', 'Watney', 'Twardowski']

    if 'Jiménez' in crew:
        print('Yes')
    else:
        print('No')
    # No

.. code-block:: python

    crew = {'Lewis', 'Watney', 'Twardowski'}

    if 'Jiménez' in crew:
        print('Yes')
    else:
        print('No')
    # No


Identity
========
.. code-block:: python

    name = None

    if name is None:
        print('Name is empty')


Negation
========
.. highlights::
    * ``not`` negates (logically inverts) condition

.. code-block:: python

    name = None

    if not name:
        print('Name is empty')

.. code-block:: python

    crew = {'Lewis', 'Watney', 'Twardowski'}

    if 'Ivanovich' not in crew:
        print('You are not assigned to the crew')
    # You are not assigned to the crew

.. code-block:: python

    name = None

    if name is not None:
        print(name)


Assignments
===========

.. literalinclude:: assignments/controlflow_conditional_expression.py
    :caption: :download:`Solution <assignments/controlflow_conditional_expression.py>`
    :end-before: # Solution
