"""
* Assignment: Datetime Timedelta Period
* Filename: assignments/datetime_timedelta_period.py
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Given period is the time between Gagarin launch and Armstrong first step on the Moon
    3. Assume:
        a. year = 365.2425 days
        * month = 30.436875 days
    4. From current date subtract this period
    5. Print calculated date
    6. How old were you at the given moment?

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Podany jest czas, który upłynął między startem Gagarina a pierwszym krokiem Armstronga na Księżycu
    3. Uwzględnij założenie:
        a. rok = 365.2425 dni
        * miesiąc = 30.436875 dni
    4. Od obecnej chwili odejmij ten czas
    5. Wyświetl wyliczoną datę
    6. Ile miałeś wtedy lat?

Given:
    * 8 years
    * 3 months
    * 8 days
    * 20 hours
    * 49 minutes
    * 15 seconds

Tests:
    # This will change every second
    >>> result
    {'years': 42,
     'months': 7,
     'days': 28,
     'hours': 7,
     'minutes': 54,
     'seconds': 46}
"""


# Given
from datetime import datetime, timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

MONTH = 30.436875 * DAY
YEAR = 365.2425 * DAY


shift = int(8*YEAR + 3*MONTH + 9*DAY + 49*MINUTE + 15*SECOND)
birthday = datetime(1970, 1, 1, 0, 0, 0)

# Solution
past = datetime.now() - timedelta(seconds=shift)
duration = past - birthday

years, seconds = divmod(duration.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(duration.seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)

result = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}
