"""
>>> assert type(result) is dict
>>> assert '00' not in result
>>> assert '13' not in result
>>> assert result['01'] == 'January'
>>> assert all(type(x) is str for x in result.keys())
>>> assert all(type(x) is str for x in result.values())
>>> assert all(len(x) == 2 for x in result.keys())
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'01': 'January',
 '02': 'February',
 '03': 'March',
 '04': 'April',
 '05': 'May',
 '06': 'June',
 '07': 'July',
 '08': 'August',
 '09': 'September',
 '10': 'October',
 '11': 'November',
 '12': 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

result = {f'{k:02}':v for k,v in enumerate(MONTHS, start=1)}
