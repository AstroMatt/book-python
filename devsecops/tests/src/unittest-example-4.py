from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Optional
from unittest import TestCase


@dataclass
class Astronaut:
    name: str
    agency: str = 'NASA'
    date_of_birth: Optional[date] = None
    first_step: Optional[datetime] = None

    def __str__(self):
        return f'My name... {self.name}'

    def __post_init__(self):
        if self.first_step and self.first_step.tzinfo != timezone.utc:
            raise ValueError('Timezone must by UTC')


class AstronautTest(TestCase):
    def setUp(self):
        self.astro = Astronaut(name='José Jiménez', agency='NASA')

    def test_recruiting_new_astronaut(self):
        jose = Astronaut(name='José Jiménez')
        self.assertEqual(jose.name, 'José Jiménez')

    def test_default_agency(self):
        jose = Astronaut(name='José Jiménez')
        self.assertEqual(jose.agency, 'NASA')

    def test_date_of_birth(self):
        jose = Astronaut(name='José Jiménez', date_of_birth=date(1961, 4, 12))
        self.assertEqual(jose.date_of_birth, date(1961, 4, 12))

    def test_first_step_in_utc(self):
        step = datetime(1969, 7, 21, 14, tzinfo=timezone.utc)
        jose = Astronaut(name='José Jiménez', first_step=step)
        self.assertEqual(jose.first_step.tzinfo, timezone.utc)

    def test_first_step_not_in_utc(self):
        step = datetime(1969, 7, 21, 14)

        with self.assertRaises(ValueError):
            Astronaut(name='José Jiménez', first_step=step)

    def test_hello(self):
        self.assertEqual(str(self.astro), 'My name... José Jiménez')
