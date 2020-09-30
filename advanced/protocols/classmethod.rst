***********
Classmethod
***********


Rationale
=========
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required


Examples
========
.. code-block:: python

    import json


    class JSONMixin:
        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)


    class User:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __str__(self):
            cls = self.__class__.__name__
            return f'{cls}(firstname="{self.firstname}", lastname="{self.lastname}")'


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
