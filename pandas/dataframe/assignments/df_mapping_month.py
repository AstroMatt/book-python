import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/phones-en.csv'

MONTHS_EN = ['January', 'February', 'March', 'April',
             'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']

MONTHS = dict(enumerate(MONTHS_EN, start=1))


## Solution 1
phones = pd.read_csv(DATA, parse_dates=['date'], index_col=0)
phones[['year', 'month_name']] = phones['month'].str.split('-', expand=True)
phones['month_name'].replace(MONTHS, inplace=True)
phones


## Solution 2
phones = pd.read_csv(DATA, parse_dates=['date'], index_col=0)
phones[['year', 'month_name']] = phones['month'].str.split('-', expand=True)
phones['month_name'] = phones['month_name'].map(MONTHS)
phones


## Solution 3
phones = pd.read_csv(DATA, parse_dates=['date'], index_col=0)
phones['year'] = phones['month'].str[:4]
phones['month_name'] = phones['month'].str[-2:]
phones['month_name'].replace(MONTHS, inplace=True)
phones
