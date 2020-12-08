"""
* Assignment: Serialization JSON HTTP
* Filename: :download:`assignments/serialization_json_http.py`
* Complexity: hard
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    1. Use `requests` library (requires installation)
    2. Download data from https://api.github.com/users
    3. Model data as class `User`
    4. Iterate over records and create instances of this class
    5. Collect all instances to one list
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    1. Użyj biblioteki `requests` (wymagana instalacja)
    2. Pobierz dane z https://api.github.com/users
    3. Zamodeluj dane za pomocą klasy `User`
    4. Iterując po rekordach twórz instancje tej klasy
    5. Zbierz wszystkie instancje do jednej listy
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'list'>
    >>> result[0]  # doctest: +NORMALIZE_WHITESPACE
    User(login='mojombo',
         id=1, url='https://api.github.com/users/mojombo',
         node_id='MDQ6VXNlcjE=',
         avatar_url='https://avatars0.githubusercontent.com/u/1?v=4',
         gravatar_id='',
         html_url='https://github.com/mojombo',
         followers_url='https://api.github.com/users/mojombo/followers',
         following_url='https://api.github.com/users/mojombo/following{/other_user}',
         gists_url='https://api.github.com/users/mojombo/gists{/gist_id}',
         starred_url='https://api.github.com/users/mojombo/starred{/owner}{/repo}',
         subscriptions_url='https://api.github.com/users/mojombo/subscriptions',
         organizations_url='https://api.github.com/users/mojombo/orgs',
         repos_url='https://api.github.com/users/mojombo/repos',
         events_url='https://api.github.com/users/mojombo/events{/privacy}',
         received_events_url='https://api.github.com/users/mojombo/received_events',
         type='User',
         site_admin=False)
"""

# Given
from dataclasses import dataclass
import requests


# Solution
@dataclass
class User:
    login: str
    id: int
    url: str
    node_id: str
    avatar_url: str
    gravatar_id: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


data = requests.get('https://api.github.com/users').json()
result = [User(**user) for user in data]

