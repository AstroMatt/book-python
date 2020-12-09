.. _OOP Classes and Instances:

*********************
Classes and Instances
*********************



Rationale
=========
* Object Oriented Paradigm
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    instance
    object
        Object created from class.

.. code-block:: python

    class MyClass:
        pass


    my = MyClass()


Classes
=======
* Capitalized ``CamelCase`` name convention
* Classes are templates for objects

.. code-block:: python
    :caption: Defining class. Classes should have capitalized name

    class Astronaut:
        pass

.. code-block:: python
    :caption: Multi-word class names should use ``CamelCase``

    class AstronautPilot:
        pass


Instances
=========
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

.. code-block:: python
    :caption: One class and one instance

    class Astronaut:
        pass


    watney = Astronaut()

.. code-block:: python
    :caption: One class and three instances

    class Astronaut:
        pass


    watney = Astronaut()
    twardowski = Astronaut()
    jimenez = Astronaut()

.. code-block:: python
    :caption: Two classes and two instances

    class Astronaut:
        pass

    class Cosmonaut:
        pass


    mark = Astronaut()
    ivan = Cosmonaut()

.. code-block:: python
    :caption: Two classes and four instances (two instances of an ``Astronaut`` class, and two of a ``Cosmonaut`` class)

    class AstronautPilot:
        pass

    class CosmonautPilot:
        pass


    mark_watney = AstronautPilot()
    melissa_lewis = AstronautPilot()
    ivan_ivanovich = CosmonautPilot()
    jan_twardowski = CosmonautPilot()


Class vs Instance
=================
.. figure:: img/oop-classes-class.jpg

    Class. Source: [class]_

.. figure:: img/oop-classes-instances.jpg

    Instances. Source: [instances]_


Convention
==========
* Never print in a class
* One class per file - when classes are long
* All classes in one file - when classes are short
* You can mix classes and functions in one file

.. code-block:: python
    :caption: Classes and Objects

    class AstronautEngineer:
        pass

    class AstronautScientist:
        pass

    class AstronautPilot:
        pass


    mark_watney = AstronautScientist()
    melissa_lewis = AstronautScientist()
    jose_jimenez = AstronautEngineer()
    jan_twardowski = AstronautPilot()

.. code-block:: python

    def hello():
        pass

    class Astronaut:
        pass


    mark = Astronaut()
    jose = Astronaut()


References
==========
.. [class] http://makieta.pl/12344-thickbox_default/faller-130803-blok-z-wielkiej-plyty-skala-h0.jpg
.. [instances] https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Os_Rusa_Poznań_RB1.jpg/1200px-Os_Rusa_Poznań_RB1.jpg


Assignments
===========

.. literalinclude:: assignments/oop_class_iris.py
    :caption: :download:`Solution <assignments/oop_class_iris.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_class_instance.py
    :caption: :download:`Solution <assignments/oop_class_instance.py>`
    :end-before: # Solution

