"""
* Assignment: Protocol Descriptor ValueRange
* Filename: protocol_descriptor_valuerange.py
* Complexity: easy
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Define descriptor class `ValueRange` with attributes:
        a. `name: str`
        b. `min: float`
        c. `max: float`
        d. `value: float`
    2. Define class `Astronaut` with attributes:
        a. `age = ValueRange('Age', min=28, max=42)`
        b. `height = ValueRange('Height', min=150, max=200)`
    3. Setting `Astronaut` attribute should invoke boundary check of `ValueRange`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę-deskryptor `ValueRange` z atrybutami:
        a. `name: str`
        b. `min: float`
        c. `max: float`
        d. `value: float`
    2. Zdefiniuj klasę `Astronaut` z atrybutami:
        a. `age = ValueRange('Age', min=28, max=42)`
        b. `height = ValueRange('Height', min=150, max=200)`
    3. Ustawianie atrybutu `Astronaut` powinno wywołać sprawdzanie zakresu z `ValueRange`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> mark = Astronaut('Mark Watney', 36, 170)

    >>> melissa = Astronaut('Melissa Lewis', 44, 170)
    Traceback (most recent call last):
    ValueError: Age is not between 28 and 42

    >>> alex = Astronaut('Alex Vogel', 40, 201)
    Traceback (most recent call last):
    ValueError: Height is not between 150 and 200
"""

# Given
class ValueRange:
    name: str
    min: float
    max: float
    value: float

    def __init__(self, name, min, max):
        pass


class Astronaut:
    age = ValueRange('Age', min=28, max=42)
    height = ValueRange('Height', min=150, max=200)


# Solution
class ValueRange:
    name: str
    min: float
    max: float
    value: float

    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

    def __set__(self, parent, value):
        if value not in range(self.min, self.max):
            raise ValueError(f'{self.name} is not between {self.min} and {self.max}')
        self.value = value


class Astronaut:
    age = ValueRange('Age', min=28, max=42)
    height = ValueRange('Height', min=150, max=200)

    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def __repr__(self):
        name = self.name
        age = self.age.value
        height = self.height.value
        return f'Astronaut({name=}, {age=}, {height=})'
