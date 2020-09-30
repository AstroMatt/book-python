*******************************
Function Decorator with Methods
*******************************


Rationale
=========
* ``mydecorator`` is a decorator name
* ``method`` is a method name
* ``instance`` is an instance
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
* ``instance`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

.. code-block:: python
    :caption: Definition

    def mydecorator(method):
        def wrapper(instance, *args, **kwargs):
            return method(instance, *args, **kwargs)
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
        def wrapper(instance, *args, **kwargs):
            return method(instance, *args, **kwargs)
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
        def wrapper(instance, *args, **kwargs):
            if instance._is_allowed:
                return method(instance, *args, **kwargs)
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
        def wrapper(instance, *args, **kwargs):
            result = method(instance, *args, **kwargs)
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

Decorator Methods Alive
-----------------------
* Assignment name: Decorator Methods Alive
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_method_alive.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``if_alive`` method decorator
    #. Decorator will allow running ``make_damage`` method only if ``current_health`` is greater than 0
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator metod ``if_alive``
    #. Dekotrator pozwoli na wykonanie metody ``make_damage``, tylko gdy ``current_health`` jest większe niż 0
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        class Hero:
            def __init__(self, name):
                self.name = name
                self.current_health = 100

            @if_alive
            def make_damage(self):
                return 10

:Output:
    .. code-block:: text

        >>> hero = Hero('Jan Twardowski')
        >>> hero.make_damage()
        10

        >>> hero.current_health = -10
        >>> hero.make_damage()
        Traceback (most recent call last):
            ...
        RuntimeError: Hero is dead and cannot make damage
