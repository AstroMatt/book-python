"""
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
"""

from dataclasses import dataclass
from typing import Union


class CSVMixin:
    def to_csv(self) -> str:
        return ','.join(str(x) for x in self.__dict__.values()) + '\n'

    @classmethod
    def from_csv(cls, text: str) -> Union['Astronaut', 'Cosmonaut']:
        data = text.strip().split(',')
        return cls(*data)


@dataclass
class Human:
    firstname: str
    lastname: str


class Astronaut(Human, CSVMixin):
    pass


class Cosmonaut(Human, CSVMixin):
    pass
