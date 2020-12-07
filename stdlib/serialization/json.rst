******************
Serialization JSON
******************


JSON Syntax
===========
* JavaScript Object Notation
* JSON format is similar to ``dict`` notation in Python
* Differences:

    * Coma ``,`` is not allowed after the last element in list or object
    * Fields are enclosed only by double quote ``"`` character
    * ``true`` and ``false`` is always lower-cased
    * Instead of ``None`` there is ``null``
    * ``camelCase`` is convention, although ``snake_case`` is also valid

.. code-block:: json
    :caption: Example JSON file

    [{"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": false, "sepalWidth": true, "petalLength": null, "petalWidth": 0.2, "species": null}]

.. code-block:: json
    :caption: JSON or Python ``list[dict]``?

    [{"firstname": "Jan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

     {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

     {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

     {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

     {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

     {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}]


Mapping to JSON
===============
* ``json.dumps(DATA: dict) -> str``
* ``json.loads(DATA: str) -> dict``

.. code-block:: python
    :caption: Serializing mapping to JSON

    import json


    DATA = {'firstname': 'Jan',
            'lastname': 'Twardowski'}

    json.dumps(DATA)
    # '{"firstname": "Jan", "lastname": "Twardowski"}'

.. code-block:: python
    :caption: Deserializing mapping from JSON

    import json


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    json.loads(DATA)
    # {'firstname': 'Jan',
    #  'lastname': 'Twardowski'}


Sequence to JSON
================
* ``json.dumps(DATA: Sequence[dict]) -> str``
* ``json.loads(DATA: str) -> list[dict]``

.. code-block:: python
    :caption: Serializing sequence to JSON

    import json


    DATA = [{'firstname': 'Jan', 'lastname': 'Twardowski'},
            {'firstname': 'Melissa', 'lastname': 'Lewis'},
            {'firstname': 'Mark', 'lastname': 'Watney'}]

    json.dumps(DATA)
    # [{"firstname": "Jan", "lastname": "Twardowski"},
    #  {"firstname": "Melissa", "lastname": "Lewis"},
    #  {"firstname": "Mark", "lastname": "Watney"}]

.. code-block:: python

    import json
    from pprint import pprint


    DATA = '[{"firstname": "Jan", "lastname": "Twardowski"}, {"firstname": "Melissa", "lastname": "Lewis"}, {"firstname": "Mark", "lastname": "Watney"}]'

    json.loads(DATA)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'}]


.. code-block:: python

    import json

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor')]

    json.dumps(DATA)
    # [["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"],
    #  [5.8, 2.7, 5.1, 1.9, "virginica"],
    #  [5.1, 3.5, 1.4, 0.2, "setosa"],
    #  [5.7, 2.8, 4.1, 1.3, "versicolor"]]

.. code-block:: python

    import json
    from pprint import pprint


    DATA = '[["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"], [5.8, 2.7, 5.1, 1.9, "virginica"], [5.1, 3.5, 1.4, 0.2, "setosa"], [5.7, 2.8, 4.1, 1.3, "versicolor"]]'

    json.loads(DATA)
    # [['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'],
    #  [5.8, 2.7, 5.1, 1.9, 'virginica'],
    #  [5.1, 3.5, 1.4, 0.2, 'setosa'],
    #  [5.7, 2.8, 4.1, 1.3, 'versicolor']]


Write JSON File
===============
* ``json.dump(DATA: dict, file: TextIOWrapper) -> None``
* file extension ``.json``

.. code-block:: python
    :caption: Serialize to JSON

    import json


    FILE = r'_temporary.json'
    DATA = {'firstname': 'Jan',
            'lastname': 'Twardowski'}

    with open(FILE, mode='w') as file:
        json.dump(DATA, file)

    # {"firstname": "Jan", "lastname": "Twardowski"}


Read JSON File
==============
* ``json.load(file: TextIOWrapper) -> dict``
* file extension ``.json``

.. code-block:: python
    :caption: Serialize to JSON

    import json


    FILE = r'_temporary.json'


    with open(FILE) as file:
        result = json.load(file)

    result
    # {'firstname': 'Jan', 'lastname': 'Twardowski'}


Datetime to JSON
================
.. code-block:: python
    :caption: Exception during encoding datetime

    from datetime import datetime, date
    import json


    DATA = {'name': 'Jan Twardowski',
            'date': date(1961, 4, 12),
            'datetime': datetime(1969, 7, 21, 2, 56, 15)}

    json.dumps(DATA)
    # Traceback (most recent call last):
    # TypeError: Object of type date is not JSON serializable

.. code-block:: python
    :caption: Encoding ``datetime`` and ``date``. Encoder will be used, when standard procedure fails

    from datetime import datetime, date
    import json


    DATA = {'name': 'Jan Twardowski',
            'date': date(1961, 4, 12),
            'datetime': datetime(1969, 7, 21, 2, 56, 15)}


    class JSONDatetimeEncoder(json.JSONEncoder):
        def default(self, value):
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            if isinstance(value, date):
                return value.strftime('%Y-%m-%d')


    result = json.dumps(DATA, cls=JSONDatetimeEncoder)
    print(result)
    # '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'

JSON to Datetime
================
.. code-block:: python
    :caption: Simple loading returns ``str`` not ``datetime`` or ``date``

    import json
    from pprint import pprint


    DATA = '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'

    result = json.loads(DATA)
    pprint(result)
    # {'date': '1961-04-12',
    #  'datetime': '1969-07-21T02:56:15.000Z',
    #  'name': 'Jan Twardowski'}

.. code-block:: python
    :caption: Decoding ``datetime`` and ``date``

    from datetime import datetime, timezone
    import json
    from pprint import pprint


    DATA = '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'


    class JSONDatetimeDecoder(json.JSONDecoder):
        DATE_FIELDS = ['date', 'date_of_birth']
        DATETIME_FIELDS = ['datetime']

        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, result: dict) -> dict:
            for field, value in result.items():

                if field in self.DATE_FIELDS:
                    value = datetime.strptime(value, '%Y-%m-%d').date()

                if field in self.DATETIME_FIELDS:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)

                result[field] = value
            return result


    result = json.loads(DATA, cls=JSONDatetimeDecoder)
    pprint(result)
    # {'date': datetime.date(1961, 4, 12),
    #  'datetime': datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc),
    #  'name': 'Jan Twardowski'}


Python Object to JSON
=====================
.. code-block:: python
    :caption: Encoding nested objects with relations to JSON

    import json


    class Astronaut:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = missions


    class Mission:
        def __init__(self, year, name):
            self.year = year
            self.name = name


    CREW = [
        Astronaut('Melissa Lewis'),
        Astronaut('Mark Watney', missions=(
            Mission(2035, 'Ares 3'))),
        Astronaut('Jan Twardowski', missions=(
            Mission(1969, 'Apollo 18'),
            Mission(2024, 'Artemis 3'))),
    ]


    class JSONObjectEncoder(json.JSONEncoder):
        def default(self, obj):
            result = obj.__dict__
            result['__class_name__'] = obj.__class__.__name__
            return result


    json.dumps(CREW, cls=JSONObjectEncoder, sort_keys=True, indent=2)
    # [{"__class_name__": "Astronaut", "name": "Melissa Lewis", "missions": []},
    #  {"__class_name__": "Astronaut", "name": "Mark Watney", "missions": [
    #       {"__class_name__": "Mission", "name": "Ares 3", "year": 2035}]},
    #  {"__class_name__": "Astronaut", "name": "Jan Twardowski", "missions": [
    #       {"__class_name__": "Mission", "name": "Apollo 18", "year": 1969},
    #       {"__class_name__": "Mission", "name": "Artemis 3", "year": 2024}]}]


JSON to Python Object
=====================
.. code-block:: python
    :caption:  Encoding nested objects with relations to JSON

    import json
    import sys

    DATA = """[{"__class_name__": "Astronaut", "missions": [], "name": "Melissa Lewis"}, {"__class_name__": "Astronaut",
    "missions": {"__class_name__": "Mission", "name": "Ares 3", "year": 2035}, "name": "Mark Watney"}, {"__class_name__":
    "Astronaut", "missions": [{"__class_name__": "Mission", "name": "Apollo 18", "year": 1969}, {"__class_name__": "Mission",
    "name": "Artemis 3", "year": 2024}], "name": "Jan Twardowski"}]"""


    class Astronaut:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = missions

        def __repr__(self):
            return f'\nAstronaut(name="{self.name}", missions={self.missions})'


    class Mission:
        def __init__(self, year, name):
            self.year = year
            self.name = name

        def __repr__(self):
            return f'\n\tMission(year={self.year}, name="{self.name}")'


    class JSONObjectDecoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, obj):
            class_name = obj.pop('__class_name__')
            cls = getattr(sys.modules[__name__], class_name)
            return cls(**obj)


    json.loads(DATA, cls=JSONObjectDecoder)
    # [
    # Astronaut(name="Melissa Lewis", missions=[]),
    # Astronaut(name="Mark Watney", missions=
    #     Mission(year=2035, name="Ares 3")),
    # Astronaut(name="Jan Twardowski", missions=[
    #     Mission(year=1969, name="Apollo 18"),
    #     Mission(year=2024, name="Artemis 3")])]


Pretty Printing JSON
====================
* JSON can be minified to save space for network transmission
* It is not very readable

.. code-block:: console
    :caption: Minified JSON file

    $ DATA='https://raw.githubusercontent.com/AstroMatt/book-python/master/stdlib/serialization/data/iris.json'
    $ curl $DATA
    [{"sepalLength":5.1,"sepalWidth":3.5,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.7,"sepalWidth":3.2,"petalLength":1.3,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.6,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5.4,"sepalWidth":3.9,"petalLength":1.7,"petalWidth":0.4,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.4,"petalLength":1.4,"petalWidth":0.3,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.4,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.4,"sepalWidth":2.9,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.1,"species":"setosa"},{"sepalLength":7,"sepalWidth":3.2,"petalLength":4.7,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.4,"sepalWidth":3.2,"petalLength":4.5,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":6.9,"sepalWidth":3.1,"petalLength":4.9,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.5,"sepalWidth":2.3,"petalLength":4,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.5,"sepalWidth":2.8,"petalLength":4.6,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.7,"sepalWidth":2.8,"petalLength":4.5,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":4.7,"petalWidth":1.6,"species":"versicolor"},{"sepalLength":4.9,"sepalWidth":2.4,"petalLength":3.3,"petalWidth":1,"species":"versicolor"},{"sepalLength":6.6,"sepalWidth":2.9,"petalLength":4.6,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":5.2,"sepalWidth":2.7,"petalLength":3.9,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":6,"petalWidth":2.5,"species":"virginica"},{"sepalLength":5.8,"sepalWidth":2.7,"petalLength":5.1,"petalWidth":1.9,"species":"virginica"},{"sepalLength":7.1,"sepalWidth":3,"petalLength":5.9,"petalWidth":2.1,"species":"virginica"},{"sepalLength":6.3,"sepalWidth":2.9,"petalLength":5.6,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.5,"sepalWidth":3,"petalLength":5.8,"petalWidth":2.2,"species":"virginica"},{"sepalLength":7.6,"sepalWidth":3,"petalLength":6.6,"petalWidth":2.1,"species":"virginica"},{"sepalLength":4.9,"sepalWidth":2.5,"petalLength":4.5,"petalWidth":1.7,"species":"virginica"},{"sepalLength":7.3,"sepalWidth":2.9,"petalLength":6.3,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.7,"sepalWidth":2.5,"petalLength":5.8,"petalWidth":1.8,"species":"virginica"},{"sepalLength":7.2,"sepalWidth":3.6,"petalLength":6.1,"petalWidth":2.5,"species":"virginica"}]

.. code-block:: console
    :caption: Pretty Printing JSON

    $ DATA='https://raw.githubusercontent.com/AstroMatt/book-python/master/stdlib/serialization/data/iris.json'
    $ curl $DATA |python -m json.tool
    [
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 5.1,
            "sepalWidth": 3.5,
            "species": "setosa"
        },
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 4.9,
            "sepalWidth": 3,
            "species": "setosa"
        },
    ...

.. code-block:: console
    :caption: ``json.tool`` checks JSON syntax validity

    $ echo '{"sepalLength":5.1,"sepalWidth":3.5,}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 37 (char 36)


Assignments
===========

.. literalinclude:: assignments/serialization_json_dump.py
    :caption: :download:`Solution <assignments/serialization_json_dump.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_load.py
    :caption: :download:`Solution <assignments/serialization_json_load.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_datetime.py
    :caption: :download:`Solution <assignments/serialization_json_datetime.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_object.py
    :caption: :download:`Solution <assignments/serialization_json_object.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_http.py
    :caption: :download:`Solution <assignments/serialization_json_http.py>`
    :end-before: # Solution
