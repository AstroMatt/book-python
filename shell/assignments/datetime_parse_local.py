from datetime import datetime


DATA = 'April 12, 1961 6:07 local time'

format = '%B %d, %Y %H:%M local time'
dt = datetime.strptime(DATA, format)

result = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(result)
