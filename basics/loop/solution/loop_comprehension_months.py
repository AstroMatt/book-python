MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

result = {f'{k:02}':v for k,v in enumerate(MONTHS, start=1)}

print(result)
