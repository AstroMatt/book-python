.. _OOP Argument Mutability:

*******************
Argument Mutability
*******************


Bad
===
.. code-block:: python
    :caption: Initial arguments mutability and shared state

    class Astronaut:
        def __init__(self, name, missions=[]):
            self.name = name
            self.missions = missions


    watney = Astronaut('Mark Watney')
    watney.missions.append('Ares 3')
    print(watney.missions)
    # ['Ares 3']

    twardowski = Astronaut('Jan Twardowski')
    print(twardowski.missions)
    # ['Ares 3']


Good
====
.. code-block:: python
    :caption: Initial arguments mutability and shared state

    class Astronaut:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = list(missions)


    watney = Astronaut('Mark Watney')
    watney.missions.append('Ares 3')
    print(watney.missions)
    # ['Ares 3']

    twardowski = Astronaut('Jan Twardowski')
    print(twardowski.missions)
    # []


Assignments
===========
.. todo:: Create assignments
