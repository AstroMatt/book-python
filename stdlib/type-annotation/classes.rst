*******
Classes
*******


.. code-block:: python

    class Astronaut:
        def __init__(self, name: str, missions: list[Mission] = ()) -> None:
            self.name = name
            self.missions = missions

    class Mission:
        def __init__(self, year: int, name: str) -> None:
            self.year = year
            self.name = name


    CREW = [
        Astronaut('Jan Twardowski', missions=(
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3'))),

        Astronaut('Mark Watney', missions=(
            Mission(2035, 'Ares 3'))),

        Astronaut('Melissa Lewis'),
    ]

.. code-block:: python

        from dataclasses import dataclass


        @dataclass
        class Astronaut:
            first_name: str
            last_name: str
            missions: tuple = ()

        @dataclass
        class Mission:
            year: int
            name: str


        twardowski = Astronaut('Jan', 'Twardowski', missions=(
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3'),
            Mission(2035, 'Ares 3'),
        ))
