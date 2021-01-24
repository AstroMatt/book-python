.. _Function Basics:

*******************
Function Definition
*******************


Function definition
===================
.. highlights::
    * Reuse code
    * Improves code readability
    * Clean-up code
    * Allows for easier refactoring

.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    hello()     # My name... José Jiménez
    hello()     # My name... José Jiménez
    hello()     # My name... José Jiménez


Naming convention
=================
.. highlights::
    * Do not use ``camelCase`` names
    * ``CamelCase`` is reserved for class names
    * Use ``snake_case`` names # Python - snake ;)
    * Add underscore (``_``) at the end of name when name collide
    * System functions names starts and ends with 'dunder' - double underscore: ``__``

.. code-block:: python
    :caption: Do not use ``camelCase``, CamelCase is reserved for class names. Use ``snake_case``

    def addNumbers(a, b):
        return a + b

    def add_numbers(a, b):
        return a + b

.. code-block:: python
    :caption: Use better names, rather than comments

    def cal_var(results, m):
        """Calculate variance"""
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

    def calculate_variance(results, m):
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

.. code-block:: python
    :caption: Add underscore (``_``) at the end of name when name collide

    def print_(text):
        print(f'<strong>{text}</strong>')

.. code-block:: python
    :caption: System functions names starts and ends with 'dunder' - double underscore: ``__``

    def __import__(module_name):
        ...


Docstring
=========
.. highlights::
    * Docstring is a first multiline comment in:

        * File / Module
        * Class
        * Method / Function

    * It is accessible in ``__doc__`` property of an object
    * Used for generating ``help()`` documentation
    * Used for ``doctest`` (more in :ref:`Function Doctest`)
    * :pep:`257` Docstring convention - For multiline always use three double quote (``"""``) characters

.. code-block:: python
    :caption: Docstring used for documentation

    def my_function():
        """
        This is the My Function
        """
        print('Hello')


    help(my_function)
    # Help on function my_function in module __main__:
    #
    # my_function()
    #     This is the My Function

    print(my_function.__doc__)
    # This is the My Function


Assignments
===========

Define Function
---------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_define_print.py`

:English:
    #. Define function ``call`` without parameters
    #. Print ``Beetlejuice`` on the screen
    #. Call function three times

:Polish:
    #. Zdefiniuj funkcję ``call`` bez parametrów
    #. Wypisz ``Beetlejuice`` na ekranie
    #. Wywołaj funkcję trzy razy
