from datetime import datetime


gagarin = 'April 12, 1961 6:07 local time'


dt = datetime.strptime(gagarin, '%B %d, %Y %H:%M local time')
formatted = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

print(formatted)

