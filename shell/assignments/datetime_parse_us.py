from datetime import datetime


armstrong = '"July 21st, 1969 2:56:15 AM UTC"'

armstrong = datetime.strptime(armstrong, '"%B %dst, %Y %I:%M:%S %p %Z"')
# datetime.datetime(1969, 7, 21, 2, 56, 15)

result = armstrong.strftime('%m/%d/%y %#I:%M %p')  # Windows
result = armstrong.strftime('%m/%d/%y %-I:%M %p')  # *nix
print(result)
# 07/21/69 2:56 AM
