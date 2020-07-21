*******************************
Function Decorator with Methods
*******************************


Syntax
======
* ``mydecorator`` is a decorator name
* ``method`` is a method name
* ``instance`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

Syntax:
    .. code-block:: python

        class MyClass:
            @mydecorator
            def my_method(self, *args, **kwargs):
                pass


        obj = MyClass()
        obj.my_method()

Is equivalent to:
    .. code-block:: python

        class MyClass:
            def my_method(self, *args, **kwargs):
                pass


        obj = MyClass()
        obj.my_method = mydecorator(obj.my_method)


Definition
==========
* ``decorator`` is a decorator name
* ``method`` is a method name
* ``instance`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

.. code-block:: python

    def decorator(method):
        def wrapper(instance, *args, **kwargs):
            return method(instance, *args, **kwargs)
        return wrapper


Usage
=====
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


Examples
========
.. code-block:: python

    def make_paragraph(method):

        def wrapper(instance, *args, **kwargs):
            value = method(instance, *args, **kwargs)
            print(f'<p>{value}</p>')
            return value

        return wrapper


    class HTMLReport:

        @make_paragraph
        def first_method(self, *args, **kwargs):
            return 'First Method'

        @make_paragraph
        def second_method(self, *args, **kwargs):
            return 'Second Method'


    if __name__ == "__main__":
        x = HTMLReport()
        x.first_method()
        x.second_method()


    # <p>First Method</p>
    # <p>Second Method</p>


Assignments
===========

Decorator Methods Alive
-----------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_method_alive.py`

:Polish:
    #. Stwórz dekorator ``if_alive``
    #. Dekotrator pozwoli na wykonanie metody ``make_damage``, tylko gdy punkty życia są większe niż 0

:Input:
    .. code-block:: python

        class Hero:
            def __init__(self, name):
                self.name = name
                self.current_health = 100

            @if_alive
            def make_damage(self):
                return 10


        hero = Hero('Jan Twardowski')
        print(hero.make_damage())
        # 10

        hero.current_health = -10
        print(hero.make_damage())
        # Traceback (most recent call last):
        #     ...
        # RuntimeError: Hero is dead and cannot make damage
