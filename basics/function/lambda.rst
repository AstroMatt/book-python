.. _Function Lambda:

***************
Function Lambda
***************


Rationale
=========
.. highlights::
    * Lambda - Anonymous functions
    * When function is used once
    * When function is short
    * You don't need to name it (hence it is anonymous)

.. glossary::

    lambda
        Anonymous function

Syntax
======
.. code-block:: python

    lambda <arguments>: <expression>

.. code-block:: python

    lambda x: x+1
    lambda x,y: x+y

.. code-block:: python

    def _(x):
        return x+1

    def _(x,y):
        return x+y


Convention
==========
.. highlights::
    * Usually parameters are named ``x`` and ``y``
    * Use shortest code possible
    * Do not assign ``lambda`` to variable
    * Lambda is anonymous function and it should stay anonymous. Do not name it
    * :pep:`8` states: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier". Lambda is anonymous function and it should stay anonymous. Do not name it.
    * Usually there are no spaces in lambda expressions (to make code shorter)

.. code-block:: python

    lambda x,y: x+y

.. code-block:: python

    square = lambda x: x**2
    square(4)
    # 16


    def square(x):
        return x**2

    square(4)
    # 16

.. code-block:: python
    :caption: :pep:`8` states: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier".

    # Correct:
    def f(x): return 2*x

    # Wrong:
    f = lambda x: 2*x


Lambda with Map
===============
.. code-block:: python
    :caption: Increment

    data = [1, 2, 3, 4]

    result = map(lambda x: x+1, data)
    list(result)
    # [2, 3, 4, 5]

.. code-block:: python
    :caption: Square

    data = [1, 2, 3, 4]

    result = map(lambda x: x**2, data)
    list(result)
    # [1, 4, 9, 16]

.. code-block:: python
    :caption: Translate

    PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
          'ł': 'l', 'ń': 'n', 'ó': 'o',
          'ś': 's', 'ż': 'z', 'ź': 'z'}

    text = 'zażółć gęślą jaźń'

    result = map(lambda x: PL.get(x,x), text)
    ''.join(result)


Lambda with Filter
==================
.. code-block:: python
    :caption: Even numbers

    DATA = [1, 2, 3, 4]

    result = filter(lambda x: x%2==0, DATA)
    list(result)
    # [2, 4]

.. code-block:: python
    :caption: Adult people

    people = [
        {'age': 21, 'name': 'Jan Twardowski'},
        {'age': 25, 'name': 'Mark Watney'},
        {'age': 18, 'name': 'Melissa Lewis'}]

    result = filter(lambda x: x['age'] >= 21, people)
    list(result)
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]

.. code-block:: python
    :caption: Astronauts

    people = [
        {'is_astronaut': False, 'name': 'Jan Twardowski'},
        {'is_astronaut': True, 'name': 'Mark Watney'},
        {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    result = filter(lambda x: x['is_astronaut'], people)
    list(result)
    # [{'is_astronaut': True, 'name': 'Mark Watney'},
    #  {'is_astronaut': True, 'name': 'Melissa Lewis'}]

.. code-block:: python

    astronauts = ['Mark Watney', 'Melissa Lewis']

    people = ['Jan Twardowski', 'Mark Watney',
              'Melissa Lewis', 'Jimenez']

    result = filter(lambda x: x in astronauts, people)
    list(result)

Assignments
===========

Function Lambda Chain
---------------------
* Assignment name: Function Lambda Chain
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_lambda_chain.py`

:English:
    #. Use data from "Input" section (see below)
    #. Inline functions ``odd()`` and ``cube()`` with ``lambda`` expressions
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wciel kod ``odd()`` i ``cube()`` wykorzystując wyrażenia ``lambda``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        def odd(x):
            return x % 2 != 0

        def cube(x):
            return x ** 3


        numbers = (x for x in range(1, 34) if x % 3 == 0)
        numbers = filter(odd, numbers)
        numbers = map(cube, numbers)
        numbers = list(numbers)
        result = sum(numbers) / len(numbers)

        print(result)

:Output:
    .. code-block:: python

        result: float
        # 11502.0

:Hints:
    * ``mean = sum(...) / len(...)``
    * type cast to ``list()`` before calculating mean to expand generator
