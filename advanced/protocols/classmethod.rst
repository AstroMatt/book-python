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
    # TypeError: from_json() missing 1 required positional argument: 'data'

    User().from_json(DATA)
    # Traceback (most recent call last):
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
    # TypeError: from_json() missing 1 required positional argument: 'data'

    User().from_json(DATA)
    # Traceback (most recent call last):
    # TypeError: __init__() missing 2 required positional arguments: 'firstname' and 'lastname'

    User(None, None).from_json(DATA)
    # Traceback (most recent call last):
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
    # TypeError: from_json() missing 1 required positional argument: 'data'

    User().from_json(DATA)
    # Traceback (most recent call last):
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

.. literalinclude:: solution/protocol_classmethod_csv.py
    :caption: :download:`Solution <solution/protocol_classmethod_csv.py>`
    :end-before: # Solution
