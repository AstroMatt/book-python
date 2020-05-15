.. _OOP Inheritance:

***********
Inheritance
***********


Rationale
=========
* Child inherits all fields and methods from parent
* Used to avoid code duplication

.. glossary::

    Parent
    Superclass
    Base Class
        Class from other classes inherits

    Child
    Subclass
        Class which inherits from :term:`parent``


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


Overload
========
.. glossary::

    Overload
        :term:`Child` has method or attribute with the same name as :term:`Parent`.
        In that case :term:`Child` attribute will be used.

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
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

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


Calling parent methods
======================
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
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            self.education = 'Engineer'
            self.profession = 'Engineer'

    class Astronaut(Engineer):
        def __init__(self, first_name, last_name):
            super().__init__(first_name, last_name)
            self.profession = 'Astronaut'


    mark = Astronaut('Mark', 'Watney')

    print(mark.__dict__)
    # {'first_name': 'Mark',
    #  'last_name': 'Watney',
    #  'education': 'Engineer',
    #  'profession': 'Astronaut'}


Assignments
===========

OOP Inheritance Simple
----------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_inheritance_simple.py`

:English:
    #. Create class ``Mars``
    #. Create class ``Venus``
    #. Create class ``Woman`` which inherits from ``Venus``
    #. Create class ``Man`` which inherits from ``Mars``

:Polish:
    #. Stwórz klasę ``Mars``
    #. Stwórz klasę ``Venus``
    #. Stwórz klasę ``Woman``, która dziedziczy po ``Venus``
    #. Stwórz klasę ``Man``, która dziedziczy po ``Mars``

OOP Inheritance Multiple
------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_inheritance_multiple.py`

:English:
    #. Create classes ``Engineer``, ``Scientist``, ``Pilot``, ``MedicalDoctor``
    #. Create class ``Astronaut`` which inherits from all of those classes

:Polish:
    #. Stwórz klasy ``Engineer``, ``Scientist``, ``Pilot``, ``MedicalDoctor``
    #. Stwórz klasę ``Astronaut``, która dziedziczy po tych wszystkich klasach

OOP Inheritance Init
--------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/oop_inheritance_init.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create class ``Crew``
    #. In ``__init__()`` set ``mission`` to ``Ares 3``
    #. Create class ``Astronaut`` which inherits from ``Crew``
    #. Using positional arguments at the initialization set astronaut first name and last name
    #. All astronauts must have assigned mission (inherited from ``Crew``)
    #. Return first name, last name and mission name from ``__str__()``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz klasę ``Crew``
    #. W ``__init__()`` ustaw ``mission`` na ``Ares 3``
    #. Stwórz klasę ``Astronaut`` dziedziczącą po ``Crew``
    #. Używając parametrów pozycyjnych podanych przy inicjalizacji ustaw imię i nazwisko astronauty
    #. Każdy astronauta musi mieć przydzieloną misję (odziedziczoną z ``Crew``)
    #. Zwróć imię, nazwisko i nazwę misji from ``__str__()``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        mark = Astronaut('Mark Watney')
        melissa = Astronaut('Melissa Lewis')
        alex = Astronaut('Alex Vogel')

        result = f"""
        Astronaut crew:
        - {mark}
        - {melissa}
        - {alex}
        """

        print(result)

:Output:
    .. code-block:: text

        Astronaut crew:
        - Mark Watney (Ares 3)
        - Melissa Lewis (Ares 3)
        - Alex Vogel (Ares 3)

