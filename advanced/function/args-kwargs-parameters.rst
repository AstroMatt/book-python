.. _Function Arbitrary Number of Parameters:

******************************
Arbitrary Number of Parameters
******************************


Recap
=====
* parameter - Receiving variable used within the function/block
* required parameters - Parameter which is necessary to call function
* optional parameters (with default value) - Parameter which is optional and has default value (if not specified at call time)

.. code-block:: python

    def echo(a, b=0):
        print(a)
        print(b)


Rationale
=========
.. figure:: img/function-unpacking,args,kwargs.png
    :scale: 40%
    :align: center

    Unpacking and Arbitrary Number of Parameters and Arguments. More info: :ref:`Function Unpack` :ref:`Function Arbitrary Number of Parameters`, :ref:`Function Arbitrary Number of Arguments`.


Positional Parameters
=====================
* ``*`` is used for positional arguments
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks to ``tuple``

.. code-block:: python

    def echo(*args):
        print(args)


    echo()                     # ()
    echo(1)                    # (1,)
    echo(2, 3)                 # (2, 3)
    echo('a', 'b')             # ('a', 'b')
    echo('a', 2, 3.3)          # ('a', 2, 3.3)

.. code-block:: python

    def echo(a, b, c=0, *args):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, *args):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)


    echo(1, 2, 3, 4, 5, 6)


Keyword Parameters
==================
* ``**`` is used for keyword arguments
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks to ``dict``

.. code-block:: python

    def echo(**kwargs):
        print(kwargs)


    echo(a=1)                                       # {'a': 1}
    echo(color='red')                               # {'color': 'red'}
    echo(firstname='Jan', lastname='Twardowski')    # {'firstname': 'Jan', 'lastname': Twardowski}

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(kwargs)  # {}


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, d=7, e=8)


Positional and Keyword Parameters
=================================
.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()
        print(kwargs)  # {}


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {}


    echo(1, 2, 3, 4, 5, 6)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # ()
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, d=7, e=8)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, 4, 5, 6, d=7, e=8)


Examples
========
.. code-block:: python
    :caption: Sum

    def sum(*values):
        total = 0

        for value in values:
            total += value

        return total


    sum()            # 0
    sum(1)           # 1
    sum(1, 4)        # 5
    sum(3, 1)        # 4
    sum(1, 2, 3, 4)  # 10

.. code-block:: python
    :caption: Kelvin to Celsius

    def kelvin_to_celsius(*degrees):
        return [x+273.15 for x in degrees]


    kelvin_to_celsius(1)
    # [274.15]

    kelvin_to_celsius(1, 2, 3, 4, 5)
    # [274.15, 275.15, 276.15, 277.15, 278.15]

.. code-block:: python
    :caption: Generate HTML list from function arguments

    def html_list(*fruits):
        print('<ul>')

        for fruit in fruits:
            print(f'<li>{fruit}</li>')

        print('</ul>')


    html_list('apple', 'banana', 'orange')
    # <ul>
    # <li>apple</li>
    # <li>banana</li>
    # <li>orange</li>
    # </ul>

.. code-block:: python
    :caption: Intuitive definition of ``print`` function

    def print(*values, sep=' ', end='\n', ...):
        return sep.join(values) + end


Assignments
===========

.. literalinclude:: solution/function_argskwargs_parameters_define.py
    :caption: :download:`Solution <solution/function_argskwargs_parameters_define.py>`
    :end-before: # Solution

.. literalinclude:: solution/function_argskwargs_parameters_args.py
    :caption: :download:`Solution <solution/function_argskwargs_parameters_args.py>`
    :end-before: # Solution

.. literalinclude:: solution/function_argskwargs_parameters_kwargs.py
    :caption: :download:`Solution <solution/function_argskwargs_parameters_kwargs.py>`
    :end-before: # Solution
