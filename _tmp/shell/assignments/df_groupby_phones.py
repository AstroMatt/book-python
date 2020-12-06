import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/phones-pl.csv'


phones = pd.read_csv(DATA, parse_dates=['datetime'])
phones['year'] = phones['datetime'].dt.year
phones['month'] = phones['datetime'].dt.month
calls = phones[phones['item'] == 'call']
result = calls.groupby(['year', 'month'])['duration'].sum()
result
