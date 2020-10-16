"""
>>> Astronaut('Mark Watney', age=38, height=170)
Astronaut(name='Mark Watney', age=38, height=170)
>>> Astronaut('Mark Watney', age=44, height=170)
Traceback (most recent call last):
    ...
ValueError: Age is not between 28 to 42
>>> Astronaut('Mark Watney', age=38, height=210)
Traceback (most recent call last):
    ...
ValueError: Height is not between 150 to 200
"""

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
            raise ValueError(f'{self.name} is not between {self.min} to {self.max}')
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
