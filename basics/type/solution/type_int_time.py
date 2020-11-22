"""

Type Int Time
-------------
* Last update: 2020-11-22
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 8 min

English:
    1. Calculate how many seconds is one day
    2. Calculate how many minutes is one day
    3. Calculate how many seconds is work day (8 hours)
    4. Calculate how many minutes is work week (5 work days)
    5. Calculate how many hours is work month (22 work days)
    6. In Calculations use truediv (``//``)
    7. Compare result with "Tests" section (see below)

Polish:
    1. Oblicz ile sekund to jedna doba
    2. Oblicz ile minut to je jedna doba
    3. Oblicz ile sekund to dzień pracy (8 godzin)
    4. Oblicz ile minut to tydzień pracy (5 dni pracy)
    5. Oblicz ile godzin to miesiąc pracy (22 dni pracy)
    6. W obliczeniach użyj truediv (``//``)
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 h = 60 min
    * 1 min = 60 s

Tests:
    >>> DAY // SECOND
    86400
    >>> DAY // MINUTE
    1440
    >>> workday // SECOND
    28800
    >>> workweek // MINUTE
    2400
    >>> workmonth // HOUR
    176

"""

# Solution
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MIN
DAY = 24 * HOUR

workday = 8 * HOUR
workweek = 5 * workday
workmonth = 22 * workday
