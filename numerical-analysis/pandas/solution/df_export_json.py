import pandas as pd

DATA = 'https://www.worldspaceflight.com/bios/eva/eva.php'
FILE = '/tmp/astro-eva2.csv'

data = pd.read_html(DATA, header=0)[1]
data.to_json(FILE)

