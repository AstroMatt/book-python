import pandas as pd


URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/martian-pl.csv'

df = pd.read_csv(URL, parse_dates=['Mission Date'])

print(df)
