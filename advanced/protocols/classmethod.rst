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
            return data

    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    result = User.from_json(DATA)
    # TypeError: from_json() missing 1 required positional argument: 'data'

    result = User().from_json(DATA)
    # TypeError: __init__() missing 2 required positional arguments: 'firstname' and 'lastname'

    result = User(None, None).from_json(DATA)
    result = User(**result)
    print(result)
    # User(firstname='Jan', lastname='Twardowski')

.. code-block:: python
    :caption: Trying to use staticmethod

    import json
    from dataclasses import dataclass

    class JSONMixin:

        @staticmethod
        def from_json(data):
            data = json.loads(data)
            return data

    @dataclass
    class User(JSONMixin):
        firstname: str
        lastname: str


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    result = User.from_json(DATA)
    result = User(**result)
    print(result)
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

    result = User.from_json(DATA)
    print(reslt)
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


    class Guest(User, JSONMixin):
        pass


    class Admin(User, JSONMixin):
        pass


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    guest = Guest.from_json(DATA)
    admin = Admin.from_json(DATA)

    type(guest)     # <class '__main__.Guest'>
    print(guest)    # Guest(firstname="Jan", lastname="Twardowski")

    type(admin)     # <class '__main__.Admin'>
    print(admin)    # Admin(firstname="Jan", lastname="Twardowski")


Use Cases
=========
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


    # settings.py
    mission_time = MartianTime


    # kod
    from settings import mission_time

    UTC = '1969-07-21T02:53:07Z'

    dt = mission_time.parse(UTC)
    print(dt.tzname)
    # Coordinated Mars Time


Assignments
===========

Protocol Classmethod CSV
------------------------
* Assignment name: Protocol Classmethod CSV
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_classmethod_csv.py`

:English:
    #. Use data from "Input" section (see below)
    #. Model class based on input data
    #. Create class ``CSVMixin`` with methods ``.to_csv()`` and ``.from_csv()``
    #. Use ``@classmethod`` decorator
    #. Create instances for input data
    #. Dump instances data to CSV
    #. Restore intances from CSV
    #. Take care only about data, do not mind the header

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zamodeluj klasę na podstawie danych wejściowych
    #. Stwórz klasę ``CSVMixin`` z metodami ``.to_csv()`` i ``.from_csv()``
    #. Użyj dekoratora ``@classmethod``
    #. Stwórz instancje obu klas wejściowych
    #. Zrzuć dane obu instancji do pliku CSV ``protocol-classmethod.csv``
    #. Pierwszą linią ma być Astronaut Mark Watney
    #. Drugą linią ma być Cosmonaut Jan Twardowski
    #. Przywróć instancje z CSV
    #. Zatroszcz się tylko danymi, nie przejmuj się nagłówkiem

:Input:
    .. code-block:: python

        FILE = r'protocol-classmethod.csv'

        watney = Astronaut('Mark', 'Watney')
        twardowski = Cosmonaut('Jan', 'Twardowski')

        with open(FILE, mode='wt') as file:
            file.write(line1 + '\n')
            file.write(line2 + '\n')

        del watney
        del twardowski

        result = []

        with open(FILE, mode='rt') as file:
            line1 = file.readline().strip()
            line2 = file.readline().strip()
            ...

:Output:
    .. code-block:: python

        from pprint import pprint

        pprint(result)
        # [Astronaut(firstname='Mark', lastname='Watney'),
        #  Cosmonaut(firstname='Jan', lastname='Twardowski')]
