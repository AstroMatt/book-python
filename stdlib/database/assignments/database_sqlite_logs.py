import sqlite3
from datetime import datetime, timezone

DATABASE = r'_temporary.sqlite3'
FILE = r'_temporary.csv'

# https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm
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


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        level TEXT,
        message TEXT);"""

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
        logs_datetime_index ON logs (datetime);"""

SQL_INSERT = """
    INSERT INTO logs VALUES (
        NULL,
        :datetime,
        :level,
        :message);"""

SQL_SELECT = 'SELECT * FROM logs ORDER BY datetime DESC'


with open(FILE, mode='w') as file:
    file.write(DATA)


data = []

with open(FILE) as file:
    for line in file:
        date, time, level, message = line.strip().split(', ', maxsplit=3)
        date = datetime.strptime(date, '%Y-%m-%d').date()

        try:
            time = datetime.strptime(time, '%H:%M:%S').time()
        except ValueError:
            time = datetime.strptime(time, '%H:%M').time()

        data.append({
            'datetime': datetime.combine(date, time).replace(tzinfo=timezone.utc),
            'level': level,
            'message': message,
        })


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX)
    db.executemany(SQL_INSERT, data)
    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        print(dict(row))

