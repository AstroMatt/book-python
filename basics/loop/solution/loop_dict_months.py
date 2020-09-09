MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

result = {}

for i, month in enumerate(MONTHS, start=1):
    key = f'{i:02d}'
    result[key] = month

print(result)
# {'01': 'January',
#  '02': 'February',
#  '03': 'March',
#  '04': 'April',
#  '05': 'May',
#  '06': 'June',
#  '07': 'July',
#  '08': 'August',
#  '09': 'September',
#  '10': 'October',
#  '11': 'November',
#  '12': 'December'}
