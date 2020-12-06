from datetime import datetime, timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

MONTH = 30.436875 * DAY
YEAR = 365.2425 * DAY


shift = int(8*YEAR + 3*MONTH + 9*DAY + 49*MINUTE + 15*SECOND)

past = datetime.now() - timedelta(seconds=shift)

birthday = datetime(1970, 1, 1, 0, 0, 0)
duration = past - birthday
# datetime.timedelta(days=14749, seconds=42059, microseconds=810113)


years, seconds = divmod(duration.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(duration.seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)

difference = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}

print(difference)
# {'years': 41, 'months': 2, 'days': 16, 'hours': 4, 'minutes': 12, 'seconds': 5}   # This will change every second
