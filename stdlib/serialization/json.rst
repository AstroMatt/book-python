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

    [
        {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
        {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
        {"sepalLength": false, "sepalWidth": true, "petalLength": null, "petalWidth": 0.2, "species": null}
    ]

.. code-block:: json
    :caption: JSON or Python ``list[dict]``?

    [
        {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
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
            {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
    ]


Mapping to JSON
===============
* ``json.dumps(DATA: dict) -> str``
* ``json.loads(DATA: str) -> dict``

.. code-block:: python
    :caption: Serializing mapping to JSON

    import json


    DATA = {
        'firstname': 'Jan',
        'lastname': 'Twardowski'}

    result = json.dumps(DATA)
    print(result)
    # '{"firstname": "Jan", "lastname": "Twardowski"}'

.. code-block:: python
    :caption: Deserializing mapping from JSON

    import json


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    result = json.loads(DATA)
    print(result)
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

    result = json.dumps(DATA)
    print(result)
    # [{"firstname": "Jan", "lastname": "Twardowski"},
    #  {"firstname": "Melissa", "lastname": "Lewis"},
    #  {"firstname": "Mark", "lastname": "Watney"}]

.. code-block:: python

    import json
    from pprint import pprint


    DATA = '[{"firstname": "Jan", "lastname": "Twardowski"}, {"firstname": "Melissa", "lastname": "Lewis"}, {"firstname": "Mark", "lastname": "Watney"}]'

    result = json.loads(DATA)
    pprint(result)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'}]


.. code-block:: python

    import json

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor')]

    result = json.dumps(DATA)
    print(result)
    # [["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"],
    #  [5.8, 2.7, 5.1, 1.9, "virginica"],
    #  [5.1, 3.5, 1.4, 0.2, "setosa"],
    #  [5.7, 2.8, 4.1, 1.3, "versicolor"]]

.. code-block:: python

    import json
    from pprint import pprint


    DATA = '[["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"], [5.8, 2.7, 5.1, 1.9, "virginica"], [5.1, 3.5, 1.4, 0.2, "setosa"], [5.7, 2.8, 4.1, 1.3, "versicolor"]]'

    result = json.loads(DATA)
    pprint(result)
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


    FILE = r'/tmp/_temporary.json'
    DATA = {
        'firstname': 'Jan',
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


    FILE = r'/tmp/_temporary.json'


    with open(FILE) as file:
        result = json.load(file)

    # {'firstname': 'Jan', 'lastname': 'Twardowski'}


Datetime to JSON
================
.. code-block:: python
    :caption: Exception during encoding datetime

    from datetime import datetime, date
    import json


    DATA = {
        'name': 'Jan Twardowski',
        'date': date(1961, 4, 12),
        'datetime': datetime(1969, 7, 21, 2, 56, 15),
    }

    result = json.dumps(DATA)
    # Traceback (most recent call last):
    # TypeError: Object of type date is not JSON serializable

.. code-block:: python
    :caption: Encoding ``datetime`` and ``date``. Encoder will be used, when standard procedure fails

    from datetime import datetime, date
    import json


    DATA = {
        'name': 'Jan Twardowski',
        'date': date(1961, 4, 12),
        'datetime': datetime(1969, 7, 21, 2, 56, 15),
    }


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


    result = json.dumps(CREW, cls=JSONObjectEncoder, sort_keys=True, indent=2)
    print(result)
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


    result = json.loads(DATA, cls=JSONObjectDecoder)
    print(result)
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

Serialization JSON Dump
-----------------------
* Assignment: Serialization JSON Dump
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min
* Filename: :download:`assignments/serialization_json_dump.py`

English:
    #. Use data from "Given" section (see below)
    #. Extract from input a header and data
    #. Create ``result: list[dict]``

        * key: name from the header
        * value: measurement or species

    #. Write structure to file ``iris_serialize.json`` in JSON format
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Z danych wydziel nagłówek i pomiary
    #. Wygeneruj ``result: list[dict]``

        * klucz: nazwa z nagłówka
        * wartość: wyniki pomiarów lub gatunek

    #. Zapisz strukturę do pliku ``iris_serialize.json`` w formacie JSON
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa'),
                (7.0, 3.2, 4.7, 1.4, 'versicolor'),
                (7.6, 3.0, 6.6, 2.1, 'virginica'),
                (4.9, 3.0, 1.4, 0.2, 'setosa'),
                (4.9, 2.5, 4.5, 1.7, 'virginica'),
                (7.1, 3.0, 5.9, 2.1, 'virginica'),
                (4.6, 3.4, 1.4, 0.3, 'setosa'),
                (5.4, 3.9, 1.7, 0.4, 'setosa'),
                (5.7, 2.8, 4.5, 1.3, 'versicolor'),
                (5.0, 3.6, 1.4, 0.3, 'setosa'),
                (5.5, 2.3, 4.0, 1.3, 'versicolor'),
                (6.5, 3.0, 5.8, 2.2, 'virginica'),
                (6.5, 2.8, 4.6, 1.5, 'versicolor'),
                (6.3, 3.3, 6.0, 2.5, 'virginica'),
                (6.9, 3.1, 4.9, 1.5, 'versicolor'),
                (4.6, 3.1, 1.5, 0.2, 'setosa')]

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     ...]

Serialization JSON Load
-----------------------
* Assignment: Serialization JSON Load
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min
* Filename: :download:`assignments/serialization_json_load.py`

English:
    #. Use data from "Given" section (see below)
    #. Save input data to "iris_deserialize.json" file
    #. Read file and print data in ``list[tuple]`` format
    #. First line must be a header
    #. Other lines must contain data

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zapisz dane wejściowe do pliku "iris_deserialize.json"
    #. Odczytaj dane z pliku, i wyświetl je w formacie ``list[tuple]``
    #. Pierwsza linijka ma zawierać nagłówek
    #. Kolejne linie mają mieć dane

Given:
    .. literalinclude:: data/iris.json
        :language: json

Serialization JSON Datetime
---------------------------
* Assignment: Serialization JSON Datetime
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min
* Filename: :download:`assignments/serialization_json_datetime.py`

English:
    #. Use data from "Given" section (see below)
    #. Save data to file in JSON format
    #. Read data from file
    #. Recreate data structure

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zapisz dane do pliku w formacie JSON
    #. Odczytaj dane z pliku
    #. Odtwórz strukturę danych

Given:
    .. code-block:: python

        from datetime import datetime, date


        DATA = {
            "astronaut": {
                "date": date(1961, 4, 12),
                "person": "mark.watney@nasa.gov"
            },
            "flight": [
                {"datetime": datetime(1969, 7, 21, 2, 56, 15), "action": "landing"}
            ]
        }

Serialization JSON Object
-------------------------
* Assignment: Serialization JSON Object
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min
* Filename: :download:`assignments/serialization_json_object.py`

English:
    #. Use data from "Given" section (see below)
    #. Convert from JSON format to Python
    #. Create classes ``Setosa``, ``Virginica``, ``Versicolor`` representing data
    #. Reading file create instances of those classes based on value in field "species"

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Przekonwertuj dane z JSON do Python
    #. Stwórz klasy ``Setosa``, ``Virginica``, ``Versicolor`` reprezentujące dane
    #. Czytając plik twórz obiekty powyższych klas w zależności od wartości pola "species"

Given:
    .. code-block:: json

        [
            {"sepalLength": 5.0, "sepalWidth": 3.6, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 4.9, "sepalWidth": 3.1, "petalLength": 1.5, "petalWidth": 0.1, "species": "setosa"},
            {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 7.0, "sepalWidth": 3.2, "petalLength": 4.7, "petalWidth": 1.4, "species": "versicolor"},
            {"sepalLength": 4.6, "sepalWidth": 3.1, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 6.5, "sepalWidth": 3.0, "petalLength": 5.8, "petalWidth": 2.2, "species": "virginica"},
            {"sepalLength": 7.1, "sepalWidth": 3.0, "petalLength": 5.9, "petalWidth": 2.1, "species": "virginica"},
            {"sepalLength": 6.7, "sepalWidth": 2.5, "petalLength": 5.8, "petalWidth": 1.8, "species": "virginica"},
            {"sepalLength": 5.2, "sepalWidth": 2.7, "petalLength": 3.9, "petalWidth": 1.4, "species": "versicolor"},
            {"sepalLength": 5.0, "sepalWidth": 3.4, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 4.9, "sepalWidth": 2.4, "petalLength": 3.3, "petalWidth": 1.0, "species": "versicolor"},
            {"sepalLength": 6.5, "sepalWidth": 2.8, "petalLength": 4.6, "petalWidth": 1.5, "species": "versicolor"},
            {"sepalLength": 5.4, "sepalWidth": 3.9, "petalLength": 1.7, "petalWidth": 0.4, "species": "setosa"},
            {"sepalLength": 6.3, "sepalWidth": 3.3, "petalLength": 4.7, "petalWidth": 1.6, "species": "versicolor"},
            {"sepalLength": 6.4, "sepalWidth": 3.2, "petalLength": 4.5, "petalWidth": 1.5, "species": "versicolor"},
            {"sepalLength": 6.6, "sepalWidth": 2.9, "petalLength": 4.6, "petalWidth": 1.3, "species": "versicolor"},
            {"sepalLength": 5.8, "sepalWidth": 2.7, "petalLength": 5.1, "petalWidth": 1.9, "species": "virginica"},
            {"sepalLength": 6.3, "sepalWidth": 2.9, "petalLength": 5.6, "petalWidth": 1.8, "species": "virginica"},
            {"sepalLength": 7.6, "sepalWidth": 3.0, "petalLength": 6.6, "petalWidth": 2.1, "species": "virginica"},
            {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 7.3, "sepalWidth": 2.9, "petalLength": 6.3, "petalWidth": 1.8, "species": "virginica"},
            {"sepalLength": 4.7, "sepalWidth": 3.2, "petalLength": 1.3, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 6.9, "sepalWidth": 3.1, "petalLength": 4.9, "petalWidth": 1.5, "species": "versicolor"},
            {"sepalLength": 7.2, "sepalWidth": 3.6, "petalLength": 6.1, "petalWidth": 2.5, "species": "virginica"},
            {"sepalLength": 4.4, "sepalWidth": 2.9, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 5.5, "sepalWidth": 2.3, "petalLength": 4.0, "petalWidth": 1.3, "species": "versicolor"},
            {"sepalLength": 4.6, "sepalWidth": 3.4, "petalLength": 1.4, "petalWidth": 0.3, "species": "setosa"},
            {"sepalLength": 6.3, "sepalWidth": 3.3, "petalLength": 6.0, "petalWidth": 2.5, "species": "virginica"},
            {"sepalLength": 4.9, "sepalWidth": 2.5, "petalLength": 4.5, "petalWidth": 1.7, "species": "virginica"},
            {"sepalLength": 5.7, "sepalWidth": 2.8, "petalLength": 4.5, "petalWidth": 1.3, "species": "versicolor"}
        ]

Serialization JSON HTTP
-----------------------
* Assignment: Serialization JSON HTTP
* Complexity: hard
* Lines of code: 15 lines
* Time: 13 min
* Filename: :download:`assignments/serialization_json_http.py`

English:
    #. Use ``requests`` library (requires installation)
    #. Download data from https://api.github.com/users
    #. Model data as class ``User``
    #. Iterate over records and create instances of this class
    #. Collect all instances to one list

Polish:
    #. Użyj biblioteki ``requests`` (wymagana instalacja)
    #. Pobierz dane z https://api.github.com/users
    #. Zamodeluj dane za pomocą klasy ``User``
    #. Iterując po rekordach twórz instancje tej klasy
    #. Zbierz wszystkie instancje do jednej listy

