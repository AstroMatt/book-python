"""
>>> assert type(result) is dict
>>> result  # doctest: +NORMALIZE_WHITESPACE
{1: 'January',
 2: 'February',
 3: 'March',
 4: 'April',
 5: 'May',
 6: 'June',
 7: 'July',
 8: 'August',
 9: 'September',
 10: 'October',
 11: 'November',
 12: 'December'}
"""


MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

result = {}
i = 1

for month in MONTHS:
    result[i] = month
    i += 1
