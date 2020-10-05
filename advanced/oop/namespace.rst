.. _OOP Namespace:

*********
Namespace
*********

Rationale
=========
* Functions and Classes can be namespaces
* Functions can be nested in functions
* Functions can be nested in classes
* Classes can be nested in functions
* The same for methods


Example
=======
.. code-block:: python

    class MyClass:
        class MyNestedClass:
            ...

.. code-block:: python

    def myfunction():
        class MyNestedClass:
            ...

.. code-block:: python

    class MyClass:
        def mymethod(self):
            def myfunction():
                ...


Inner Functions
===============
.. code-block:: python

    def run():
        firstname = 'Mark'
        lastname = 'Watney'

.. code-block:: python

    def run():
        firstname = 'Mark'
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

.. code-block:: python

    def run():
        firstname = 'Mark'
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

        class Astronaut:
            pass

.. code-block:: python

    def run():
        firstname = 'Mark'
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

        class Astronaut:
            firstname = 'Mark'
            lastname = 'Watney'

            def hello(self):
                print(self.firstname, self.lastname)


Inner Classes
=============
.. code-block:: python

    class User:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def login(self):
            if not in DATABASE:
                raise self.DoesNotExist

        class DoesNotExist(Exception):
            pass


    try:
        user = User('Mark', 'Watney')
        user.login()
    except User.DoesNotExists:
        print('User does not exist')

.. code-block:: python

    class Person(models.Model):
        firstname = ...
        lastname = ...

        class Meta:
            ordering = ['lastname']


Assignments
===========
.. todo:: Create assignments
