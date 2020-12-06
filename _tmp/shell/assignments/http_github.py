#!/usr/bin/env python3

import re
import json
from http.client import HTTPSConnection
from http import HTTPStatus
from base64 import b64encode
from datetime import datetime
import logging


USERNAME = 'your username'
TOKEN = 'your password'


auth = bytes(f'{USERNAME}:{TOKEN}', 'utf-8')
auth = b64encode(auth).decode('ascii')

headers = {
    'Authorization': f'Basic {auth}',
    'User-Agent': 'Python http.client',
    'Accept': 'application/json'
}

conn = HTTPSConnection(host="api.github.com", port=443)


def GET(url):
    logging.warning(f'URL: {url}')
    conn.request('GET', url, headers=headers)
    response = conn.getresponse()

    if response.status == HTTPStatus.OK:
        body = response.read().decode()
        return json.loads(body)
    else:
        raise ConnectionError(response.reason)


for repository in GET('/orgs/django/repos'):
    if repository['fullname'] == 'django/django':
        break


url = repository['commits_url']
url = url.replace('{/sha}', '')
url = url.replace('https://api.github.com', '')

commits = GET(url)
date = commits[0]['commit']['author']['date']
name = commits[0]['commit']['author']['name']
messages = [commit['commit']['message'] for commit in commits]
date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')

issues = set()

for msg in messages:
    tickets = re.findall(r'#([0-9]+)', msg, flags=re.MULTILINE)
    issues.update(tickets)

print(f'Last commit: {date} by {name}')
print(f'Issues: {issues}')

conn.close()
