"""
* Assignment: OOP Relations Nested
* Filename: oop_relations_nested.py
* Complexity: medium
* Lines of code: 7 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Convert `DATA` to format with one column per each attrbute
       for example: `street1`, `street2`, `city1`, `city2`, etc.
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu,
       np. `street1`, `street2`, `city1`, `city2`, itd.
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'list'>
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Jan', 'lastname': 'Twardowski', 'street1': 'Kamienica Pod św. Janem Kapistranem', 'city1': 'Kraków', 'post_code1': '31-008', 'region1': 'Małopolskie', 'country1': 'Poland'},
     {'firstname': 'José', 'lastname': 'Jiménez', 'street1': '2101 E NASA Pkwy', 'city1': 'Houston', 'post_code1': 77058, 'region1': 'Texas', 'country1': 'USA', 'street2': '', 'city2': 'Kennedy Space Center', 'post_code2': 32899, 'region2': 'Florida', 'country2': 'USA'},
     {'firstname': 'Mark', 'lastname': 'Watney', 'street1': '4800 Oak Grove Dr', 'city1': 'Pasadena', 'post_code1': 91109, 'region1': 'California', 'country1': 'USA', 'street2': '2825 E Ave P', 'city2': 'Palmdale', 'post_code2': 93550, 'region2': 'California', 'country2': 'USA'},
     {'firstname': 'Иван', 'lastname': 'Иванович', 'street1': '', 'city1': 'Космодро́м Байкону́р', 'post_code1': '', 'region1': 'Кызылординская область', 'country1': 'Қазақстан', 'street2': '', 'city2': 'Звёздный городо́к', 'post_code2': 141160, 'region2': 'Московская область', 'country2': 'Россия'},
     {'firstname': 'Melissa', 'lastname': 'Lewis'},
     {'firstname': 'Alex', 'lastname': 'Vogel', 'street1': 'Linder Hoehe', 'city1': 'Köln', 'post_code1': 51147, 'region1': 'North Rhine-Westphalia', 'country1': 'Germany'}]
"""


# Given
import json

DATA = """[
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
]"""

result = []

# Solution
for astronaut in json.loads(DATA):
    for i, address in enumerate(astronaut.pop('addresses'), start=1):
        columns = [f'{key}{i}' for key in address.keys()]
        addresses = zip(columns, address.values())
        astronaut.update(dict(addresses))
    result.append(astronaut)


# Note that
# * dictionary merging `dict|dict` was introduced in Python 3.9
# * assignment expressions `:=` was introduced in Python 3.8
#
# result = [astronaut | dict(addresses)
#           for astronaut in json.loads(DATA)
#           for i, address in enumerate(astronaut.pop('addresses'), start=1)
#           if (columns := [f'{key}{i}' for key in address.keys()])
#           and (addresses := zip(columns, address.values()))]
