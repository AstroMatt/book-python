import re
from datetime import datetime, timezone
import requests


USERNAME = '...'
TOKEN = '...'

AUTH = (USERNAME, TOKEN)
commits = list()
issues = set()


url = 'https://api.github.com/orgs/django/repos'

for repository in requests.get(url, auth=AUTH).json():
    if repository['name'] == 'django':
        url = repository['commits_url']
        url = url.replace('{/sha}', '')
        break

for commit in requests.get(url, auth=AUTH).json():
    date = commit['author']['date']
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)

    commits.append({
        'hash': commit['sha'],
        'author': commit['author']['name'],
        'email': commit['author']['email'],
        'date': date,
        'message': commit['message'],
    })

for commit in commits:
    issue = re.findall(r'#([0-9]+)', commit['message'], flags=re.MULTILINE)

    if issue:
        issues.add(issue)

print(issues)
