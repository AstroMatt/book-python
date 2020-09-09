import pandas as pd

DATA = 'https://www.worldspaceflight.com/bios/eva/eva3.php'
FILE = 'astro-eva3.pkl'


data = pd.read_html(DATA, header=0)[1]
data.to_pickle(FILE)
