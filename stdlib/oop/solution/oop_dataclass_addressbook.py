"""
* Assignment: OOP Dataclass Addressbook
* Filename: oop_dataclass_addressbook.py
* Complexity: easy
* Lines of code: 12 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Model data using `dataclasses`
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zamodeluj dane wykorzystując `dataclass`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Astronaut)
    >>> assert isclass(Address)
    >>> assert hasattr(Astronaut, 'firstname')
    >>> assert hasattr(Astronaut, 'lastname')
    >>> assert hasattr(Address, 'street')
    >>> assert hasattr(Address, 'city')
    >>> assert hasattr(Address, 'post_code')
    >>> assert hasattr(Address, 'region')
    >>> assert hasattr(Address, 'country')
"""


# Given
from dataclasses import dataclass, field


DATA = [
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

    {"firstname": "Melissa", "lastname": "Lewis"},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]


# Solution
@dataclass
class Address:
    street: str = ''
    city: str = ''
    post_code: str = ''
    region: str = ''
    country: str = ''


@dataclass
class Astronaut:
    firstname: str = ''
    lastname: str = ''
    addresses: list[Address] = field(default_factory=list)
