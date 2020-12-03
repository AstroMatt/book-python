.. _Function Basics:

*******************
Function Definition
*******************


Rationale
=========
.. highlights::
    * Reuse code
    * Improves code readability
    * Clean-up code
    * Allows for easier refactoring


Syntax
======
.. code-block:: python

    def <name>():
        <do something>


Definition
==========
.. code-block:: python

    def say_hello():
        print('My name... José Jiménez')

    say_hello()     # My name... José Jiménez
    say_hello()     # My name... José Jiménez
    say_hello()     # My name... José Jiménez


Convention
==========
.. highlights::
    * Do not use ``camelCase`` names
    * ``CamelCase`` is reserved for class names
    * Use ``snake_case`` names # Python - snake ;)
    * Add underscore (``_``) at the end of name when name collide
    * System functions names starts and ends with 'dunder' - double underscore: ``__``

.. code-block:: python
    :caption: Do not use ``camelCase``, CamelCase is reserved for class names. Use ``snake_case``

    def sayHello():
        print('This is camelCase() name')
        print('It is c/c++/Java/JavaScript convention')

    def say_hello():
        print('This is snake_case() name')
        print('It is Pythonic way')

.. code-block:: python
    :caption: Use better names, rather than comments

    def cal_var(data, m):
        # Calculate variance
        return sum((Xi-m) ** 2 for Xi in data) / len(data)

    def calculate_variance(data, m):
        return sum((Xi-m) ** 2 for Xi in data) / len(data)

.. code-block:: python
    :caption: Add underscore (``_``) at the end of name when name collide. Although prefer naming it differently.

    def print_(text):
        # Add underscore (``_``) at the end of name when name collide.
        print(f'<strong>{text}</strong>')

    def print_html(text):
        # Although prefer naming it differently.
        print(f'<strong>{text}</strong>')

.. code-block:: python
    :caption: System functions names starts and ends with 'dunder' - double underscore: ``__``

    def __import__(module_name):
        ...


Docstring
=========
.. highlights::
    * Docstring is a first multiline comment in: File/Module, Class, Method/Function
    * Used for generating ``help()`` documentation
    * It is accessible in ``__doc__`` property of an object
    * Used for ``doctest``
    * :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters
    * More information in :ref:`Function Doctest`

.. code-block:: python
    :caption: Docstring used for documentation

    def say_hello():
        """This is the say_hello function"""
        print('Hello')


    help(say_hello)
    # Help on function say_hello in module __main__:
    #
    # say_hello()
    #     This is the say_hello function

    print(say_hello.__doc__)
    # This is the say_hello function

.. code-block:: python
    :caption: Docstring used for documentation

    def say_hello():
        """
        This is the say_hello function
        And the description is longer then one line
        """
        print('Hello')


    help(say_hello)
    # Help on function say_hello in module __main__:
    #
    # say_hello()
    #     This is the say_hello function
    #     And the description is longer then one line

    print(say_hello.__doc__)
    #    This is the say_hello function
    #    And the description is longer then one line


Assignments
===========

.. literalinclude:: assignments/function_definition_print.py
    :caption: :download:`Solution <assignments/function_definition_print.py>`
    :end-before: # Solution
