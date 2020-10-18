import pandas as pd

URL = r'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-flights.csv'


df = pd.read_csv(URL)
df['Order'] = df['Order'].astype(int)
df['Order'].ffill(inplace=True)
df = df.sample(frac=1.0)
df.reset_index(drop=True, inplace=True)
