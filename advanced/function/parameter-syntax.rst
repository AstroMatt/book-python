****************
Parameter Syntax
****************


Recap
=====
.. code-block:: python

    def echo(a, b, c=3):
         print(a, b, c)


    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Keyword-only Parameters
=======================
* All parameters after ``*`` must be keyword-only

.. code-block:: python

    def echo(a, *, b, c=3):
        print(a, b, c)


    echo(1, 2)              # TypeError: echo() takes 1 positional argument but 2 were given
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required keyword-only argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 1 positional argument but 3 were given
    echo(1, 2, c=3)         # TypeError: echo() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Positional-only Parameters
==========================
.. versionadded:: Python 3.8
    :pep:`570` -- Python Positional-Only Parameters

* All parameters before ``/`` must be positional-only

.. code-block:: python

    def echo(a, /, b, c=3):
        print(a, b, c)


    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Positional and Keyword Parameters
=================================
.. code-block:: python

    def echo(a, /, b, *, c=3):
        print(a, b, c)


    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 2 positional arguments but 3 were given
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Examples
========
.. code-block:: python
    :caption: https://docs.python.org/3/library/functions.html#sorted

    sorted(iterable, *, key=None, reverse=False)

.. code-block:: python
    :caption: https://docs.python.org/3/library/functions.html#sum

    sum(iterable, /, start=0)

.. code-block:: python

    def add(a, b, /):
        return a + b

.. code-block:: python

    def divmod(a, b, /):
        return (a // b, a % b)

.. code-block:: python

    def quantiles(dist, /, *, n=4, method='exclusive')
        ...


Assignments
===========

.. literalinclude:: assignments/function_parameter_syntax_kwargs.py
    :caption: :download:`Solution <assignments/function_parameter_syntax_kwargs.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_parameter_syntax_args.py
    :caption: :download:`Solution <assignments/function_parameter_syntax_args.py>`
    :end-before: # Solution
