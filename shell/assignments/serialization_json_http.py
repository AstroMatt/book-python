from dataclasses import dataclass
import requests


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


for user in requests.get('https://api.github.com/users').json():
    u = User(**user)
    print(u)

