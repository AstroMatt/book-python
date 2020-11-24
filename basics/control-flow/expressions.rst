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

Conditional Expression
----------------------
* Assignment: Conditional Expression
* Filename: controlflow_conditional_expression.py
* Complexity: medium
* Lines of code to write: 25 lines
* Estimated time: 21 min

English:
    #. Use data from "Given" section (see below)
    #. Table contains Blood Pressure classification according to American Heart Association :cite:`Whelton2018`
    #. User inputs blood pressure in ``XXX/YY`` or ``XXX/YYY`` format
    #. User will not try to input invalid data
    #. Data format:

        * ``XXX: int`` systolic pressure
        * ``YY: int`` or ``YYY: int`` diastolic pressure

    #. Print status of given blood pressure
    #. If systolic and diastolic values are in different categories, assume worst case

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Tabela zawiera klasyfikację ciśnienia krwi wg American Heart Association :cite:`Whelton2018`
    #. Użytkownik wprowadza ciśnienie krwi w formacie ``XXX/YY`` lub ``XXX/YYY``
    #. Użytkownik nie będzie próbował wprowadzać danych niepoprawnych
    #. Format danych:

        * ``XXX: int`` to wartość ciśnienia skurczowego (ang. *systolic*)
        * ``YY: int`` lub ``YYY: int`` to wartość ciśnienia rozkurczowego (ang. *diastolic*)

    #. Wypisz status wprowadzonego ciśnienia krwi
    #. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek

.. csv-table:: Classification of blood pressure in adults :cite:`Whelton2018`
    :header-rows: 1

    "Blood Pressure Category", "Systolic [mm Hg]", "Operator", "Diastolic [mm Hg]"
    "Normal", "Less than 120", "and", "Less than 80"
    "Elevated", "120-129", "and", "Less than 80"
    "Hypertension stage 1", "130-139", "or", "80-89"
    "Hypertension stage 2", "140 or higher", "or", "90 or higher"
    "Hypertensive Crisis", "Higher than 180", "and/or", "Higher than 120"

Given:
    .. code-block:: text

        '119/79': 'Normal',
        '120/80': 'Hypertension stage 1',
        '121/79': 'Elevated',
        '120/81': 'Hypertension stage 1',
        '130/80': 'Hypertension stage 1',
        '130/89': 'Hypertension stage 1',
        '140/85': 'Hypertension stage 2',
        '140/89': 'Hypertension stage 2',
        '141/90': 'Hypertension stage 2',
        '141/91': 'Hypertension stage 2',
        '180/120': ('Hypertension stage 2', 'Hypertensive Crisis')

Tests:
    TODO doctests
