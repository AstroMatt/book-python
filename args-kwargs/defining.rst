****************************************************
Defining function with arbitrary number of arguments
****************************************************


Recap information about function parameters
===========================================
* positional arguments
* keyword (named) arguments
* default values
* keyword arguments must be on the right side
* order of keyword arguments doesn't matter

.. code-block:: python

    def echo(a, b):
        print(a)
        print(b)


    echo(1, 2)       # positional arguments
    echo(a=1, b=2)   # keyword arguments
    echo(b=2, a=1)   # keyword arguments, order doesn't matter
    echo(1, b=2)     # positional and keyword arguments
    echo(a=1, 2)     # SyntaxError: positional argument follows keyword argument


Arbitrary number of positional arguments
========================================
- ``*`` in this context, is not multiplication in mathematical sense
- ``*`` is used for positional arguments
- ``args`` is a convention, but you can use any name
- ``*args`` unpacks to ``tuple``

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


Arbitrary number of keyword arguments
=====================================
- ``**`` in this context, is not power in mathematical sense
- ``**`` is used for keyword arguments
- ``kwargs`` is a convention, but you can use any name
- ``**kwargs`` unpacks to ``dict``

.. code-block:: python

    def echo(**kwargs):
        print(kwargs)


    echo(a=1)                                       # {'a': 1}
    echo(color='red')                               # {'color': 'red'}
    echo(first_name='Jan', last_name='Twardowski')  # {'first_name': 'Jan', 'last_name': Twardowski}

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


Arbitrary number of positional and named arguments
==================================================
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
        print(c)       # 0
        print(args)    # ()
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, d=7, e=8)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, 4, 5, 6, d=7, e=8)


Keyword only
============
* All arguments after ``*`` is keyword only
* Since Python 3.8 there will be ``/`` to indicate positional only arguments

.. code-block:: python

    def echo(a, *, b):
        print(a)
        print(b)

    echo(1, b=2)
    # 1
    # 2

    echo(1, 2)
    # TypeError: echo() takes 1 positional argument but 2 were given

    echo(1)
    # TypeError: echo() missing 1 required keyword-only argument: 'b'

.. code-block:: python

    def echo(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)

    echo(1, 2, 3, 4, e=5, f=6)      # is valid
    echo(1, 2, 3, d=4, e=5, f=6)    # d must be a positional argument
    echo(1, 2, 3, 4, 5, f=6)        # e must be a keyword argument


Use cases
=========
.. code-block:: python

    def add(*args):
        total = 0

        for arg in args:
            total += arg

        return total


    add()            # 0
    add(1)           # 1
    add(1, 4)        # 5
    add(3, 1)        # 4
    add(1, 2, 3, 4)  # 10

.. code-block:: python
    :caption: Converts arguments between different units

    def kelvin_to_celsius(*degrees):
        return [x+273.15 for x in degrees]


    kelvin_to_celsius(1)
    # [274.15]

    kelvin_to_celsius(1, 2, 3, 4, 5)
    # [274.15, 275.15, 276.15, 277.15, 278.15]


.. code-block:: python
    :caption: Generate HTML list from function arguments

    def html_list(*args):
        print('<ul>')

        for element in args:
            print(f'<li>{element}</li>')

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

Average
-------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/defining_average.py`

:English:
    #. Create function ``average()``, which calculates arithmetic mean
    #. Function can have arbitrary number of positional arguments

:Polish:
    #. Napisz funkcję ``average()``, wyliczającą średnią arytmetyczną
    #. Funkcja przyjmuje dowolną ilość pozycyjnych argumentów

args
----
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/defining_args.py`

:English:
    #. Create function ``is_numeric``
    #. Function can have arbitrary number of positional arguments
    #. Arguments can be of any type
    #. Using ``type()`` check:

        #. Return ``True`` if all arguments are ``int`` or ``float`` only
        #. Return ``False`` if any argument is different type

    #. Do not use ``all()`` and ``any()``

:Polish:
    #. Stwórz funkcję ``is_numeric``
    #. Funkcja może przyjmować tylko argumenty pozycyjne
    #. Podawane argumenty mogą być dowolnego typu
    #. Za pomocą ``type()`` sprawdź:

        #. Zwróć ``True`` jeżeli wszystkie argumenty są tylko typów ``int`` lub ``float``
        #. Zwróć ``False`` jeżeli którykolwiek jest innego typu

    #. Nie używaj ``all()`` oraz ``any()``

:The whys and wherefores:
    * Defining and calling functions
    * Arbitrary number of positional arguments
    * Corner case checking
    * Function arguments checking
    * Type casting

args and kwargs
---------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/defining_kwargs.py`

:English:
    #. Create function ``is_numeric``
    #. **Function can have arbitrary number of positional and keyword arguments**
    #. Arguments can be of any type
    #. Using ``type()`` check:

        #. Return ``True`` if all arguments are ``int`` or ``float`` only
        #. Return ``False`` if any argument is different type

    #. Do not use ``all()`` and ``any()``

:Polish:
    #. Stwórz funkcję ``is_numeric``
    #. **Funkcja może przyjmować zarówno argumenty pozycyjne jak i nazwane**
    #. Podawane argumenty mogą być dowolnego typu
    #. Za pomocą ``type()`` sprawdź:

        #. Zwróć ``True`` jeżeli wszystkie argumenty są tylko typów ``int`` lub ``float``
        #. Zwróć ``False`` jeżeli którykolwiek jest innego typu

    #. Nie używaj ``all()`` oraz ``any()``

:The whys and wherefores:
    * Defining and calling functions
    * Arbitrary number of positional arguments
    * Corner case checking
    * Function arguments checking
    * Type casting
