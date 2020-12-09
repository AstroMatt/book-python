.. _Function Arguments:

******************
Function Arguments
******************


Rationale
=========
.. glossary::

    argument
        Value/variable/reference being passed to the function

    positional argument
        Value passed to function - order is important

    keyword argument
        Value passed to function resolved by name - order is not important


Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    my_function(<arguments>)

.. code-block:: python

    add(1, 2)
    add(a=1, b=2)
    add(1, b=2)

Positional Arguments
====================
* Order of positional arguments has significance

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(2, 1)          # 1
    subtract(1, 2)          # -1


Keyword Arguments
=================
* Order of keyword arguments has no significance

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(a=2, b=1)      # 1
    subtract(b=1, a=2)      # 1


Positional and Keyword Arguments
================================
* Positional arguments must be at the left side
* Keyword arguments must be at the right side

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(2, b=1)        # 1
    subtract(a=2, 1)        # SyntaxError: positional argument follows keyword argument
    subtract(2, a=1)        # TypeError: subtract() got multiple values for argument 'a'


Examples
========
.. code-block:: python
    :caption: Example 1

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Mark Watney')          # My name... Mark Watney
    hello(name='Mark Watney')     # My name... Mark Watney
    hello()                       # My name... José Jiménez

.. code-block:: python
    :caption: Example 2

    connect('myusername', 'mypassword')

    connect('myusername', 'mypassword', 'example.com', 443, False, 1, True)

    connect(host='example.com', username='myusername', password='mypassword')

    connect(
        host='example.com',
        username='myusername',
        password='mypassword',
        port=443,
        ssl=True,
        persistent=True)

.. code-block:: python
    :caption: Example 3

    read_csv('iris.csv')

    read_csv('iris.csv', encoding='utf-8')

    read_csv('iris.csv', encoding='utf-8', parse_dates=['date_of_birth'])

    read_csv('iris.csv', skiprows=3, delimiter=';')

    read_csv('iris.csv',
        encoding='utf-8',
        skiprows=3,
        delimiter=';',
        usecols=['Sepal Length', 'Species'],
        parse_dates=['date_of_birth'])


Assignments
===========

.. literalinclude:: assignments/function_args_sequence.py
    :caption: :download:`Solution <assignments/function_args_sequence.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_divide.py
    :caption: :download:`Solution <assignments/function_args_divide.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_power.py
    :caption: :download:`Solution <assignments/function_args_power.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_power.py
    :caption: :download:`Solution <assignments/function_args_power.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_translate.py
    :caption: :download:`Solution <assignments/function_args_translate.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_clean.py
    :caption: :download:`Solution <assignments/function_args_clean.py>`
    :end-before: # Solution
    :name: Function Arguments Clean

.. literalinclude:: assignments/function_args_numstr.py
    :caption: :download:`Solution <assignments/function_args_numstr.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_numhuman.py
    :caption: :download:`Solution <assignments/function_args_numhuman.py>`
    :end-before: # Solution
