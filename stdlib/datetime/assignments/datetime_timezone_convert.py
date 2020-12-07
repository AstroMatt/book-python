"""
* Assignment: Datetime Timezone Convert
* Filename: :download:`assignments/datetime_timezone_convert.py`
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Convert given date to `datetime` objects
    3. What was the time in:
        a. London, United Kingdom
        b. Moscow, Russian Federation
        c. Warsaw, Poland
        d. Tokyo, Japan
        e. Sydney, Australia
        f. Auckland, New Zealand

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj podaną datę do obiektu `datetime`
    3. Wyświetl datę jaka była w:
        a. London, Wielka Brytania
        b. Moscow, Rosja
        c. Warsaw, Polska
        d. Tokyo, Japan
        e. Sydney, Australia
        f. Auckland, Nowa Zelandia

Extra Task:
    1. Kosmodrom Bajkonur, Kazachstan
    2. Cape Canaveral, FL, USA
    3. Houston, TX, USA
    4. New York, USA
    5. South Pole
    6. North Pole

Tests:
    TODO: Doctests
    TODO: Make solution to the new assignment description
"""

# Given
from datetime import datetime
from pytz import timezone


DATA = '1969-07-21 02:56:15 UTC'


# Solution
UTC = timezone('UTC')
WAW = timezone('Europe/Warsaw')
BAIKONUR = timezone('Asia/Almaty')


gagarin = 'April 12, 1961 2:07 local time'
gagarin = datetime.strptime(gagarin, '%B %d, %Y %H:%M local time')
gagarin = BAIKONUR.localize(gagarin)

print('Gagarin [UTC]', gagarin.astimezone(UTC))
print('Gagarin [WAW]', gagarin.astimezone(WAW))


armstrong = '"07/21/69 2:56:15 AM UTC"'
armstrong = datetime.strptime(armstrong, '"%m/%d/%y %I:%M:%S %p %Z"')
armstrong = UTC.localize(armstrong)

print('Armstrong [UTC]', armstrong)
print('Armstrong [WAW]', armstrong.astimezone(WAW))
