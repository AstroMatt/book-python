.. _Decorator Function with Mth:

***************************
Decorator Function with Mth
***************************


Rationale
=========
* ``mydecorator`` is a decorator name
* ``method`` is a method name
* ``self`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

Syntax:
    .. code-block:: python

        class MyClass:
            @mydecorator
            def mymethod(self, *args, **kwargs):
                ...


        obj = MyClass()
        obj.mymethod()

Is equivalent to:
    .. code-block:: python

        class MyClass:
            def mymethod(self, *args, **kwargs):
                ...


        obj = MyClass()
        obj.mymethod = mydecorator(obj.mymethod)


Syntax
======
* ``mydecorator`` is a decorator name
* ``mymethod`` is a method name
* ``self`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

.. code-block:: python
    :caption: Definition

    def mydecorator(method):
        def wrapper(self, *args, **kwargs):
            return method(self, *args, **kwargs)
        return wrapper

.. code-block:: python
    :caption: Decoration

    class MyClass:

        @mydecorator
        def mymethod(self):
            ...

.. code-block:: python
    :caption: Usage

    my = MyClass()
    my.mymethod()


Example
=======
.. code-block:: python

    def run(method):
        def wrapper(self, *args, **kwargs):
            return method(self, *args, **kwargs)
        return wrapper


    class Astronaut:
        @run
        def hello(self, name):
            return f'My name... {name}'


    astro = Astronaut()
    astro.hello('José Jiménez')
    # 'My name... José Jiménez'


Use Cases
=========
.. code-block:: python

    def if_allowed(method):
        def wrapper(self, *args, **kwargs):
            if self._is_allowed:
                return method(self, *args, **kwargs)
            else:
                print('Sorry, Permission Denied')
        return wrapper


    class MyClass:
        def __init__(self):
            self._is_allowed = True

        @if_allowed
        def do_something(self):
            print('Doing...')

        @if_allowed
        def do_something_else(self):
            print('Doing something else...')


    my = MyClass()

    my.do_something()           # Doing...
    my.do_something_else()      # Doing something else...

    my._is_allowed = False

    my.do_something()           # Sorry, you cannot do anything
    my.do_something_else()      # Sorry, you cannot do anything

.. code-block:: python

    def paragraph(method):
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            return f'<p>{result}</p>'
        return wrapper


    class HTMLReport:

        @paragraph
        def first(self, *args, **kwargs):
            return 'First'

        @paragraph
        def second(self, *args, **kwargs):
            return 'Second'


    x = HTMLReport()

    x.first()
    # '<p>First</p>'

    x.second()
    # '<p>Second</p>'


Assignments
===========

.. literalinclude:: solution/decorator_method_alive.py
    :caption: :download:`Solution <solution/decorator_method_alive.py>`
    :end-before: # Solution
