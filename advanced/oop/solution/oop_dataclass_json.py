"""
* Assignment: OOP Dataclass JSON
* Filename: oop_dataclass_json.py
* Complexity: easy
* Lines of code: 30 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. You received input data in JSON format from the API
    3. Using `dataclass` Model data as class `User`
    4. Parse fields with dates and store as `datetime` objects
    5. Parse fields with `true` and `false` values and store as `bool` objects
    6. Iterate over records and create instances of this class
    7. Collect all instances to one list
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Otrzymałeś z API dane wejściowe w formacie JSON
    3. Wykorzystując `dataclass` zamodeluj dane za pomocą klasy `User`
    4. Sparsuj pola zwierające daty i zapisz je jako obiekty `datetime`
    5. Sparsuj pola zawierające `true` lub `false` i zapamiętaj ich wartości jako obiekty `bool`
    6. Iterując po rekordach twórz instancje tej klasy
    7. Zbierz wszystkie instancje do jednej listy
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(username='commander', password='pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=', firstname='Иван', lastname='Иванович', email='', date_joined=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), last_login=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), is_superuser=False, is_staff=True, is_active=True, groups=[1], user_permissions=[{'eclss': ['add', 'modify', 'view']}, {'communication': ['add', 'modify', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(username='executive-officer', password='pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=', firstname='José', lastname='Jiménez', email='', date_joined=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), last_login=None, is_superuser=False, is_staff=True, is_active=True, groups=[1], user_permissions=[{'eclss': ['add', 'modify', 'view']}, {'communication': ['add', 'modify', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(username='crew-medical-officer', password='pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=', firstname='Melissa', lastname='Lewis', email='', date_joined=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), last_login=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), is_superuser=False, is_staff=True, is_active=True, groups=[1], user_permissions=[{'communication': ['add', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(username='science-data-officer', password='pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=', firstname='Mark', lastname='Watney', email='', date_joined=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), last_login=None, is_superuser=False, is_staff=True, is_active=True, groups=[1], user_permissions=[{'communication': ['add', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(username='communication-officer', password='pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=', firstname='Jan', lastname='Twardowski', email='', date_joined=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), last_login=None, is_superuser=False, is_staff=True, is_active=True, groups=[1], user_permissions=[{'communication': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(username='eclss-officer', password='pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=', firstname='Harry', lastname='Stamper', email='', date_joined=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), last_login=None, is_superuser=False, is_staff=True, is_active=True, groups=[1], user_permissions=[{'communication': ['add', 'view']}, {'eclss': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}])]
"""


# Given
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


DATA = '[{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","firstname":"Иван","lastname":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","firstname":"José","lastname":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","firstname":"Melissa","lastname":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","firstname":"Mark","lastname":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","firstname":"Jan","lastname":"Twardowski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","firstname":"Harry","lastname":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]'  # noqa


def _clean_time(text: Optional[datetime]) -> Optional[datetime]:
    try:
        return datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
    except TypeError:
        return None


# Solution
@dataclass
class Permission:
    name: str
    level: list[str]


@dataclass
class User:
    username: str
    password: str
    firstname: str
    lastname: str
    email: str
    date_joined: datetime
    last_login: Optional[datetime]
    is_superuser: bool
    is_staff: bool
    is_active: bool
    groups: list[int]
    user_permissions: list[Permission]

    def __post_init__(self):
        self.date_joined = _clean_time(self.date_joined)
        self.last_login = _clean_time(self.last_login)


result = [User(**u['fields'])
         for u in json.loads(DATA)]

