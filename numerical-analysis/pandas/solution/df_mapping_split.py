import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/phones-en.csv'


## Solution 1
phones = pd.read_csv(DATA, parse_dates=['date'])
phones['datetime'] = phones['date']
phones['date'] = phones['datetime'].dt.date
phones['time'] = phones['datetime'].dt.time
phones


## Solution 2
phones = pd.read_csv(DATA, parse_dates=['date'])
phones['datetime'] = phones['date']
phones['date'] = phones['datetime'].map(lambda dt: dt.date())
phones['time'] = phones['datetime'].map(lambda dt: dt.time())
phones


## Solution 3
phones = pd.read_csv(DATA, parse_dates=['date'])
phones['datetime'] = phones['date']
phones[['date', 'time']] = phones['date'].map(str).str.split(expand=True)
phones
