import pandas as pd

URL = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'

tables = pd.read_html(URL)
df = tables[3]

print(df)

