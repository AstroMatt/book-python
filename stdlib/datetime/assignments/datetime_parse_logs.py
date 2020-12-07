"""
* Assignment: Datetime Parse Logs
* Filename: datetime_parse_logs.py
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Save input data to file `apollo11-timeline.log`
    3. Extract `datetime` object, level name and message from each line
    4. Collect data to `result: list[dict]`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz dane wejściowe do pliku `apollo11-timeline.log`
    3. Wyciągnij obiekt `datetime`, poziom logowania oraz wiadomość z każdej linii
    4. Zbierz dane do `result: list[dict]`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

References:
    * Apollo 11 timeline https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'date': datetime.datetime(1969, 7, 14, 21, 0), 'level': 'INFO', 'message': 'Terminal countdown started'},
     {'date': datetime.datetime(1969, 7, 16, 13, 31, 53), 'level': 'WARNING', 'message': 'S-IC engine ignition (#5)'},
     {'date': datetime.datetime(1969, 7, 16, 13, 33, 23), 'level': 'DEBUG', 'message': 'Maximum dynamic pressure (735.17 lb/ft^2)'},
     {'date': datetime.datetime(1969, 7, 16, 13, 34, 44), 'level': 'WARNING', 'message': 'S-II ignition'},
     {'date': datetime.datetime(1969, 7, 16, 13, 35, 17), 'level': 'DEBUG', 'message': 'Launch escape tower jettisoned'},
     {'date': datetime.datetime(1969, 7, 16, 13, 39, 40), 'level': 'DEBUG', 'message': 'S-II center engine cutoff'},
     {'date': datetime.datetime(1969, 7, 16, 16, 22, 13), 'level': 'INFO', 'message': 'Translunar injection'},
     {'date': datetime.datetime(1969, 7, 16, 16, 56, 3), 'level': 'INFO', 'message': 'CSM docked with LM/S-IVB'},
     {'date': datetime.datetime(1969, 7, 16, 17, 21, 50), 'level': 'INFO', 'message': 'Lunar orbit insertion ignition'},
     {'date': datetime.datetime(1969, 7, 16, 21, 43, 36), 'level': 'INFO', 'message': 'Lunar orbit circularization ignition'},
     {'date': datetime.datetime(1969, 7, 20, 17, 44), 'level': 'INFO', 'message': 'CSM/LM undocked'},
     {'date': datetime.datetime(1969, 7, 20, 20, 5, 5), 'level': 'WARNING', 'message': 'LM powered descent engine ignition'},
     {'date': datetime.datetime(1969, 7, 20, 20, 10, 22), 'level': 'ERROR', 'message': 'LM 1202 alarm'},
     {'date': datetime.datetime(1969, 7, 20, 20, 14, 18), 'level': 'ERROR', 'message': 'LM 1201 alarm'},
     {'date': datetime.datetime(1969, 7, 20, 20, 17, 39), 'level': 'WARNING', 'message': 'LM lunar landing'},
     {'date': datetime.datetime(1969, 7, 21, 2, 39, 33), 'level': 'DEBUG', 'message': 'EVA started (hatch open)'},
     {'date': datetime.datetime(1969, 7, 21, 2, 56, 15), 'level': 'WARNING', 'message': '1st step taken lunar surface (CDR)'},
     {'date': datetime.datetime(1969, 7, 21, 2, 56, 15), 'level': 'WARNING', 'message': "That's one small step for [a] man... one giant leap for mankind"},
     {'date': datetime.datetime(1969, 7, 21, 3, 5, 58), 'level': 'DEBUG', 'message': 'Contingency sample collection started (CDR)'},
     {'date': datetime.datetime(1969, 7, 21, 3, 15, 16), 'level': 'INFO', 'message': 'LMP on lunar surface'},
     {'date': datetime.datetime(1969, 7, 21, 5, 11, 13), 'level': 'DEBUG', 'message': 'EVA ended (hatch closed)'},
     {'date': datetime.datetime(1969, 7, 21, 17, 54), 'level': 'WARNING', 'message': 'LM lunar liftoff ignition (LM APS)'},
     {'date': datetime.datetime(1969, 7, 21, 21, 35), 'level': 'INFO', 'message': 'CSM/LM docked'},
     {'date': datetime.datetime(1969, 7, 22, 4, 55, 42), 'level': 'WARNING', 'message': 'Transearth injection ignition (SPS)'},
     {'date': datetime.datetime(1969, 7, 24, 16, 21, 12), 'level': 'INFO', 'message': 'CM/SM separation'},
     {'date': datetime.datetime(1969, 7, 24, 16, 35, 5), 'level': 'WARNING', 'message': 'Entry'},
     {'date': datetime.datetime(1969, 7, 24, 16, 50, 35), 'level': 'WARNING', 'message': 'Splashdown (went to apex-down)'},
     {'date': datetime.datetime(1969, 7, 24, 17, 29), 'level': 'INFO', 'message': 'Crew egress'}]
"""


# Given
from datetime import datetime


DATA = """1969-07-14, 21:00:00, INFO, Terminal countdown started
1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)
1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
1969-07-16, 13:34:44, WARNING, S-II ignition
1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned
1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff
1969-07-16, 16:22:13, INFO, Translunar injection
1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB
1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition
1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition
1969-07-20, 17:44:00, INFO, CSM/LM undocked
1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition
1969-07-20, 20:10:22, ERROR, LM 1202 alarm
1969-07-20, 20:14:18, ERROR, LM 1201 alarm
1969-07-20, 20:17:39, WARNING, LM lunar landing
1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)
1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)
1969-07-21, 02:56:15, WARNING, That's one small step for [a] man... one giant leap for mankind
1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)
1969-07-21, 03:15:16, INFO, LMP on lunar surface
1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)
1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)
1969-07-21, 21:35:00, INFO, CSM/LM docked
1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)
1969-07-24, 16:21:12, INFO, CM/SM separation
1969-07-24, 16:35:05, WARNING, Entry
1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)
1969-07-24, 17:29, INFO, Crew egress"""

result = []

# Solution
for line in DATA.splitlines():
    date, time, level, message = line.split(', ', maxsplit=3)
    date = datetime.strptime(date, '%Y-%m-%d')

    try:
        time = datetime.strptime(time, '%H:%M:%S').time()
    except ValueError:
        time = datetime.strptime(time, '%H:%M').time()

    result.append({
        'date': datetime.combine(date, time),
        'level': level,
        'message': message,
    })
