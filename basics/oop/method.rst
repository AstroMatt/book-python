.. _OOP Methods:

*******
Methods
*******


Rationale
=========
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)

.. code-block:: python
    :caption: Syntax

    class MyClass:
        def mymethod(self):
            ...

    my = MyClass()
    my.mymethod()


Methods Without Arguments
=========================
.. code-block:: python
    :caption: Methods without arguments

    class Astronaut:
        def say_hello(self):
            print('My name... José Jiménez')


    jose = Astronaut()
    jose.say_hello()
    # My name... José Jiménez


Methods With Required Argument
==============================
.. code-block:: python
    :caption: Methods with required argument

    class Astronaut:
        def say_hello(self, name):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # Traceback (most recent call last):
    # TypeError: say_hello() missing 1 required positional argument: 'name'


Methods With Optional Argument
==============================
.. code-block:: python
    :caption: Methods with arguments with default value

    class Astronaut:
        def say_hello(self, name='Unknown'):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # My name... Unknown


Assignments
===========

.. literalinclude:: assignments/oop_method_call.py
    :caption: :download:`Solution <assignments/oop_method_call.py>`
    :end-before: # Solution
