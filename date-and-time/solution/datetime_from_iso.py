from datetime import datetime


dt = '1969-07-21T02:56:15.123Z'
output = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ')

print(output)
