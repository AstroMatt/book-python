.. _OOP Inheritance:

***********
Inheritance
***********


Rationale
=========
* Child inherits all fields and methods from parent
* Used to avoid code duplication

.. glossary::

    parent
    superclass
    base class
        Class from other classes inherits

    child
    subclass
        Class which inherits from :term:`parent`

    overload
        When :term:`child` has method or attribute with the same name as :term:`parent`.
        In such case :term:`child` attribute will be used (will overload :term:`parent`).


Syntax
======
.. code-block:: python

    class Parent:
        def say_hello(self):
            return 'Hello'

    class Child(Parent):
        pass


    obj = Child()
    obj.say_hello()
    # 'Hello'


Example
=======
.. code-block:: python

    class Car:
        def engine_start():
            print('Starting engine...')

        def engine_stop():
            print('Stopping engine...')


    class Truck:
        def engine_start():
            print('Starting engine...')

        def engine_stop():
            print('Stopping engine...')

.. code-block:: python

    class Vehicle:
        def engine_start():
            print('Starting engine...')

        def engine_stop():
            print('Stopping engine...')


    class Car(Vehicle):
        pass

    class Truck(Vehicle):
        pass


Simple Inheritance
==================
.. code-block:: python

    class Vehicle:
        pass


    class Car(Vehicle):
        pass

    class Truck(Vehicle):
        pass


.. code-block:: python

    class Engineer:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

    class Astronaut(Engineer):
        pass

    class Cosmonaut(Engineer):
        pass


    mark = Astronaut('Mark', 'Watney')
    ivan = Cosmonaut('Ivan', 'Ivanovic')

.. code-block:: python

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species


    class Setosa(Iris):
        pass

    class Versicolor(Iris):
        pass

    class Virginica(Iris):
        pass


    setosa = Setosa(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa'
    )


Multilevel Inheritance
======================
.. code-block:: python
    :caption: Multilevel Inheritance

    class Scientist:
        pass

    class Engineer(Scientist):
        pass

    class Astronaut(Engineer):
        pass


    watney = Astronaut()

    isinstance(watney, Scientist)   # True
    isinstance(watney, Engineer)    # True
    isinstance(watney, Astronaut)   # True

    type(watney)                    # <class '__main__.Astronaut'>

.. code-block:: python

    class Vehicle:
        pass


    class Car(Vehicle):
        def windows_open():
            print('Opening windows...')


    class Truck(Vehicle):
        def windows_open():
            print('Opening windows...')


    class Motorcycle(Vehicle):
        pass

.. code-block:: python

    class Vehicle:
        def windows_open():
            print('Opening windows...')


    class Car(Vehicle):
        pass

    class Truck(Vehicle):
        pass

    class Motorcycle(Vehicle):
        def windows_open():
            raise NotImplementedError('Has no windows')


Multiple Inheritance
====================
.. code-block:: python
    :caption: Multiple Inheritance

    class Scientist:
        pass

    class Engineer:
        pass

    class Astronaut(Scientist, Engineer):
        pass


    watney = Astronaut()

    isinstance(watney, Scientist)   # True
    isinstance(watney, Engineer)    # True
    isinstance(watney, Astronaut)   # True

    type(watney)                    # <class '__main__.Astronaut'>

.. code-block:: python

    class Vehicle:
        pass

    class HasWindows:
        pass


    class Car(Vehicle, HasWindows):
        pass

    class Truck(Vehicle, HasWindows):
        pass

    class Motorcycle(Vehicle):
        pass


Overload
========
.. code-block:: python

    class A:
        def show(self):
            return 'a'

    class B(A):
        pass


    obj = B()
    obj.show()
    # 'a'

.. code-block:: python

    class A:
        def show(self):
            return 'a'

    class B(A):
        def show(self):
            return 'b'


    obj = B()
    obj.show()
    # 'b'


Super Function
==============
.. code-block:: python

    class A:
        def show(self):
            return 'a'

    class B(A):
        def show(self):
            old_value = super().show()
            return old_value + 'b'


    obj = B()
    obj.show()
    # 'ab'

.. code-block:: python

    class Engineer:
        def __init__(self):
            self.education = 'Engineer'
            self.profession = 'Engineer'

    class Astronaut(Engineer):
        def __init__(self):
            super().__init__()
            self.profession = 'Astronaut'


    mark = Astronaut()

    print(mark.__dict__)
    # {'education': 'Engineer',
    #  'profession': 'Astronaut'}

.. code-block:: python

    class Engineer:
        def __init__(self):
            self.education = 'Engineer'
            self.profession = 'Engineer'

    class Astronaut(Engineer):
        def __init__(self):
            self.profession = 'Astronaut'
            super().__init__()


    mark = Astronaut()

    print(mark.__dict__)
    # {'education': 'Engineer',
    #  'profession': 'Engineer'}

.. code-block:: python

    class Engineer:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
            self.education = 'Engineer'
            self.profession = 'Engineer'

    class Astronaut(Engineer):
        def __init__(self, firstname, lastname):
            super().__init__(firstname, lastname)
            self.profession = 'Astronaut'


    mark = Astronaut('Mark', 'Watney')

    print(mark.__dict__)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney',
    #  'education': 'Engineer',
    #  'profession': 'Astronaut'}


Assignments
===========

.. literalinclude:: assignments/oop_inheritance_simple.py
    :caption: :download:`Solution <assignments/oop_inheritance_simple.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_multiple.py
    :caption: :download:`Solution <assignments/oop_inheritance_multiple.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_super.py
    :caption: :download:`Solution <assignments/oop_inheritance_super.py>`
    :end-before: # Solution
