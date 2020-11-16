"""
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


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MIN
DAY = 24 * HOUR

workday = 8 * HOUR
workweek = 5 * workday
workmonth = 22 * workday
