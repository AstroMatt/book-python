import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'


## Solution 1
df = pd.read_csv(DATA, encoding='utf-8')
df = df[df['Petal length'] > 2.0]
df.head(5)


## Solution 2
df = pd.read_csv(DATA, encoding='utf-8')
df.where(df['Petal length'] > 2.0, inplace=True)
df.head(5)


