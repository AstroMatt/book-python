***************
Function Return
***************


Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    def <name>(<parameters>):
        return <do something>

.. code-block:: python

    def add_numbers(a, b):
        return a + b

.. code-block:: python

    def mean(a, b):
        mean = (a+b) / 2
        return mean

Return Keyword
==============
.. highlights::
    * ``return`` keyword indicates outcome of the function
    * Code after ``return`` will not execute

.. code-block:: python

    def hello():
        return 'ehlo world'

    print(hello())
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    print(hello())
    # 'ehlo world'


Returning Simple Types
======================
.. code-block:: python

    def my_function():
        return 42

.. code-block:: python

    def my_function():
        return 13.37

.. code-block:: python

    def my_function():
        return 'Mark Watney'

.. code-block:: python

    def my_function():
        return True


Return None
===========
* Python will ``return None`` if no explicit return is specified

.. code-block:: python

    def my_function():
        return None

.. code-block:: python

    def my_function():
        print('ehlo world')

.. code-block:: python

    def my_function():
        pass

.. code-block:: python

    def my_function():
        """My function"""


Return Sequences
================
.. code-block:: python

    def my_function():
        return 42, 13.37, 'Mark Watney'

.. code-block:: python

    def my_function():
        return (42, 13.37, 'Mark Watney')

.. code-block:: python

    def my_function():
        return [42, 13.37, 'Mark Watney']

.. code-block:: python

    def my_function():
        return {42, 13.37, 'Mark Watney'}


Return Mapping
==============
.. code-block:: python

    def my_function():
        return {'first_name': 'Mark', 'last_name': 'Watney'}


Returning nested types
======================
.. code-block:: python

    def my_function():
        return [
            ('Mark', 'Watney'),
            {'Jan Twardowski', 'Melissa Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'Roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('Mercury', 'Gemini', 'Apollo')},
        ]


Assignments
===========

Return Numbers
--------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_return_numbers.py`

:English:
    #. Define function ``add`` without parameters
    #. Function should return sum of ``42`` and ``13.37``
    #. Call function and intercept returned value
    #. Print value

:Polish:
    #. Zdefiniuj funkcję ``add`` bez parametrów
    #. Funkcja powinna zwracać sumę ``42`` and ``13.37``
    #. Wywołaj funkcję i przechwyć zwracaną wartość
    #. Wyświetl wartość
