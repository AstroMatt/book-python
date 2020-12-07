"""
* Assignment: Serialization JSON Datetime
* Filename: serialization_json_datetime.py
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Save data to file in JSON format
    3. Read data from file
    4. Recreate data structure
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz dane do pliku w formacie JSON
    3. Odczytaj dane z pliku
    4. Odtwórz strukturę danych
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'astronaut': {'date': datetime.date(1961, 4, 12), 'person': 'mark.watney@nasa.gov'},
     'flight': [{'datetime': datetime.datetime(1969, 7, 21, 2, 56, 15), 'action': 'landing'}]}
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
from datetime import datetime, date
import json

FILE = '_temporary.json'
DATA = {"astronaut": {"date": date(1961, 4, 12), "person": "mark.watney@nasa.gov"},
        "flight": [{"datetime": datetime(1969, 7, 21, 2, 56, 15), "action": "landing"}]}


# Solution
class JSONDatetimeEncoder(json.JSONEncoder):
    def default(self, value):

        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        elif isinstance(value, date):
            return value.strftime('%Y-%m-%d')


class JSONDatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, obj):
        for key, value in obj.items():
            if key == 'datetime':
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
            elif key == 'date':
                value = datetime.strptime(value, '%Y-%m-%d').date()
            obj[key] = value
        return obj


with open(FILE, mode='w', encoding='utf-8') as file:
    json.dump(DATA, file, cls=JSONDatetimeEncoder)


with open(FILE, encoding='utf-8') as file:
    result = json.load(file, cls=JSONDatetimeDecoder)
