.. _Protocol Classmethod:

***********
Classmethod
***********


Rationale
=========
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required


Example
=======
.. code-block:: python

    import json
    from dataclasses import dataclass


    class JSONMixin:
        def from_json(self, data):
            data = json.loads(data)
            return User(**data)


    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    User.from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: from_json() missing 1 required positional argument: 'data'

    User().from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: __init__() missing 2 required positional arguments: 'firstname' and 'lastname'

    User(None, None).from_json(DATA)
    # User(firstname='Jan', lastname='Twardowski')

.. code-block:: python
    :caption: Trying to use method with ``self``

    import json
    from dataclasses import dataclass


    class JSONMixin:
        def from_json(self, data):
            data = json.loads(data)
            return self(**data)


    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    User.from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: from_json() missing 1 required positional argument: 'data'

    User().from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: __init__() missing 2 required positional arguments: 'firstname' and 'lastname'

    User(None, None).from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: 'User' object is not callable

.. code-block:: python
    :caption: Trying to use method with ``self.__init__()``

    import json
    from dataclasses import dataclass


    class JSONMixin:
        def from_json(self, data):
            data = json.loads(data)
            return self.__init__(**data)


    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    User.from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: from_json() missing 1 required positional argument: 'data'

    User().from_json(DATA)
    # Traceback (most recent call last):
    #     ...
    # TypeError: __init__() missing 2 required positional arguments: 'firstname' and 'lastname'

    result = User(None, None).from_json(DATA)
    type(result)
    # <class 'NoneType'>

.. code-block:: python
    :caption: Trying to use staticmethod

    import json
    from dataclasses import dataclass

    class JSONMixin:

        @staticmethod
        def from_json(data):
            data = json.loads(data)
            return User(**data)

    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    User.from_json(DATA)
    # User(firstname='Jan', lastname='Twardowski')

.. code-block:: python

    import json
    from dataclasses import dataclass


    class JSONMixin:

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)


    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    User.from_json(DATA)
    # User(firstname='Jan', lastname='Twardowski')


Use Cases
=========
.. code-block:: python

    import json
    from dataclasses import dataclass


    class JSONMixin:

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)


    @dataclass
    class User:
        firstname: str
        lastname: str


    class Guest(User, JSONMixin):
        pass


    class Admin(User, JSONMixin):
        pass


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    guest = Guest.from_json(DATA)
    admin = Admin.from_json(DATA)

    type(guest)     # <class '__main__.Guest'>
    type(admin)     # <class '__main__.Admin'>

    print(guest)    # Guest(firstname='Jan', lastname='Twardowski')
    print(admin)    # Admin(firstname='Jan', lastname='Twardowski')

.. code-block:: python

    class AbstractTime:
        tzname: str
        tzcode: str

        @classmethod
        def parse(cls, text):
            result = ...
            return cls(**result)

    class MartianTime(AbstractTime):
        tzname = 'Coordinated Mars Time'
        tzcode = 'MTC'

    class LunarTime(AbstractTime):
        tzname = 'Lunar Standard Time'
        tzcode = 'LST'

    class EarthTime(AbstractTime):
        tzname = 'Universal Time Coordinated'
        tzcode = 'UTC'


    # Settings
    time = MartianTime

    # Usage
    from settings import time

    UTC = '1969-07-21T02:53:07Z'

    dt = time.parse(UTC)
    print(dt.tzname)
    # Coordinated Mars Time


Assignments
===========

Protocol Classmethod CSV
------------------------
* Assignment name: Protocol Classmethod CSV
* Last update: 2020-10-02
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_classmethod_csv.py`

:English:
    #. Use data from "Input" section (see below)
    #. To class ``CSVMixin`` add methods:

        * ``to_csv(self) -> str``
        * ``from_csv(self, text: str) -> Union['Astronaut', 'Cosmonaut']``

    #. ``CSVMixin.to_csv()`` should return attribute values separated with coma
    #. ``CSVMixin.from_csv()`` should return instance of a class on which it was called
    #. Use ``@classmethod`` decorator in proper place
    #. All tests must pass
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Do klasy ``CSVMixin`` dodaj metody:

        * ``to_csv(self) -> str``
        * ``from_csv(self, text: str) -> Union['Astronaut', 'Cosmonaut']``

    #. ``CSVMixin.to_csv()`` powinna zwracać wartości atrybutów klasy rozdzielone po przecinku
    #. ``CSVMixin.from_csv()`` powinna zwracać instancje klasy na której została wywołana
    #. Użyj dekoratora ``@classmethod`` w odpowiednim miejscu
    #. Wszystkie testy muszą przejść
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        from dataclasses import dataclass


        class CSVMixin:
            raise NotImplementedError


        @dataclass
        class Human:
            firstname: str
            lastname: str

        class Astronaut(Human, CSVMixin):
            pass

        class Cosmonaut(Human, CSVMixin):
            pass

:Output:
    .. code-block:: text

        >>> mark = Astronaut('Mark', 'Watney')
        >>> jan = Cosmonaut('Jan', 'Twardowski')
        >>> csv = mark.to_csv() + jan.to_csv()

        >>> with open('_temporary.txt', mode='wt') as file:
        ...    file.writelines(csv)

        >>> result = []
        >>> with open('_temporary.txt', mode='rt') as file:
        ...     lines = file.readlines()
        ...     result += [Astronaut.from_csv(lines[0])]
        ...     result += [Cosmonaut.from_csv(lines[1])]

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [Astronaut(firstname='Mark', lastname='Watney'),
         Cosmonaut(firstname='Jan', lastname='Twardowski')]

:Hint:
    * ``CSVMixin.to_csv()`` should add newline ``\n`` at the end of line
