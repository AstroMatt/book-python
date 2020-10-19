import pandas as pd

DATA = r'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-order.csv'


df = pd.read_csv(DATA)
df['Order'].ffill(inplace=True)
df['Order'] = df['Order'].astype(int)
df = df.sample(frac=1.0)
df.reset_index(drop=True, inplace=True)

df
