
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional
from unittest import TestCase


@dataclass
class User:
    firstname: str
    lastname: str
    date_of_birth: Optional[datetime] = None
    permission: list = ()

    def __post_init__(self):
        self.permission = list(self.permission)

        if self.date_of_birth and self.date_of_birth.tzinfo != timezone.utc:
            raise ValueError

    def add_permission(self, permission):
        self.permission.append(permission)

    def remove_permission(self, permission):
        self.permission.remove(permission)

    def __str__(self):
        return f'User(firstname="{self.firstname}", lastname="{self.lastname}")'


class UserTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        now = datetime.now(tz=timezone.utc)
        self.user = User(firstname='Jan', lastname='Twardowski', date_of_birth=now)

    def tearDown(self) -> None:
        pass

    def test_create_user(self):
        user = User(firstname='Jan', lastname='Twardowski')
        self.assertEqual(user.firstname, 'Jan')
        self.assertEqual(user.lastname, 'Twardowski')

    def test_permission_add(self):
        self.user.add_permission('read')
        self.assertIn('read', self.user.permission)

    def test_permission_remove(self):
        self.user.add_permission('read')
        self.user.remove_permission('read')
        self.assertNotIn('read', self.user.permission)

    def test_date_of_birth_in_utc(self):
        self.assertEqual(self.user.date_of_birth.tzinfo, timezone.utc)

    def test_date_of_birth_not_in_utc(self):
        with self.assertRaises(ValueError):
            now = datetime.now()
            user = User(firstname='Jan', lastname='Twardowski', date_of_birth=now)
            self.assertEqual(user.date_of_birth.tzinfo, timezone.utc)

    def test_str(self):
        self.assertEqual(str(self.user), 'User(firstname="Jan", lastname="Twardowski")')
