"""
>>> assert type(result) is list

>>> assert all(type(astro) is Astronaut
...            for astro in result)

>>> assert all(type(addr) is Address
...            for astro in result
...            for addr in astro.addresses)

>>> result  # doctest: +NORMALIZE_WHITESPACE
[Astronaut(firstname='Jan', lastname='Twardowski', addresses=[Address(street='Kamienica Pod św. Janem Kapistranem', city='Kraków', postcode='31-008', region='Małopolskie', country='Poland')]),
 Astronaut(firstname='José', lastname='Jiménez',
           addresses=[Address(street='2101 E NASA Pkwy', city='Houston', postcode=77058, region='Texas', country='USA'),
                      Address(street='', city='Kennedy Space Center', postcode=32899, region='Florida', country='USA')]),
 Astronaut(firstname='Mark', lastname='Watney',
           addresses=[Address(street='4800 Oak Grove Dr', city='Pasadena', postcode=91109, region='California', country='USA'),
                      Address(street='2825 E Ave P', city='Palmdale', postcode=93550, region='California', country='USA')]),
 Astronaut(firstname='Иван', lastname='Иванович',
           addresses=[Address(street='', city='Космодро́м Байкону́р', postcode='', region='Кызылординская область', country='Қазақстан'),
                      Address(street='', city='Звёздный городо́к', postcode=141160, region='Московская область', country='Россия')]),
 Astronaut(firstname='Alex', lastname='Vogel',
           addresses=[Address(street='Linder Hoehe', city='Köln', postcode=51147, region='North Rhine-Westphalia', country='Germany')])]
"""

from dataclasses import dataclass
from typing import List, Optional, Union


DATA = [
    {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "postcode": "31-008", "region": "Małopolskie", "country": "Poland"}]},
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},
    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "city": "Космодро́м Байкону́р", "postcode": "", "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": "", "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},
    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},
    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]


@dataclass
class Address:
    street: str
    city: str
    postcode: Union[int, str]
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: Optional[List[Address]] = None


result = [
    Astronaut(**row, addresses=[Address(**a) for a in addr])
    for row in DATA
    if (addr := row.pop('addresses'))]


# result = []
#
# for row in DATA:
#     addr = row.pop('addresses')
#     astro = Astronaut(**row, addresses=[Address(**a) for a in addr])
#     result.append(astro)
