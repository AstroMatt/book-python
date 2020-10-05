.. _OOP Static and Dynamic:

******************
Static and Dynamic
******************


Static Fields
=============
* Fields created on class
* Must have default values
* Share state

.. code-block:: python
    :caption: Static Fields

    class Astronaut:
        agency = 'NASA'


    watney = Astronaut()
    jimenez = Astronaut()

    print(watney.agency)
    # NASA

    print(jimenez.agency)
    # NASA

    print(Astronaut.agency)
    # NASA


Dynamic Fields
==============
* Fields created on instance
* Do not share state
* By convention initialized in ``__init__()``
* You can also initialize on living object directly

.. code-block:: python
    :caption: Dynamic fields

    class Astronaut:
        def __init__(self, agency='NASA'):
            self.agency = agency


    watney = Astronaut()
    twardowski = Astronaut()

    print(watney.agency)
    # NASA

    print(twardowski.agency)
    # NASA

    print(Astronaut.agency)
    # AttributeError: type object 'Astronaut' has no attribute 'agency'


Static vs. Dynamic Fields
=========================
.. code-block:: python
    :caption: Static vs. Dynamic fields

    class Astronaut:
        agency = 'NASA'


    watney = Astronaut()
    twardowski = Astronaut()
    ivanovic = Astronaut()

    # Print field
    print(watney.agency)           # NASA
    print(twardowski.agency)       # NASA
    print(ivanovic.agency)         # NASA
    print(Astronaut.agency)        # NASA

    # Change field on the instance
    ivanovic.agency = 'Roscosmos'

    # Print field
    print(watney.agency)           # NASA
    print(twardowski.agency)       # NASA
    print(ivanovic.agency)         # Roscosmos
    print(Astronaut.agency)        # NASA

    # Change field on a class
    Astronaut.agency = 'POLSA'

    # Print field
    print(watney.agency)           # POLSA
    print(twardowski.agency)       # POLSA
    print(ivanovic.agency)         # Roscosmos
    print(Astronaut.agency)        # POLSA


Static or Dynamic?
==================
.. code-block:: python

    class Astronaut:
        firstname = ...
        lastname = ...

.. code-block:: python

    class Cosmonaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

.. code-block:: python

    class Taikonaut:
        pass

    t = Taikonaut()
    t.firstname = ...
    t.lastname = ...

.. code-block:: python

    class Taikonaut:
        pass

    Taikonaut.firstname
    Taikonaut.lastname

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class GaganYatri:
        firstname: str
        lastname: list



Assignments
===========
.. todo:: Create assignments
