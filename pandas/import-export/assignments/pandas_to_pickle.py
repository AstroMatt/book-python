import pandas as pd

DATA = r'https://www.worldspaceflight.com/bios/eva/eva3.php'
FILE = r'/tmp/_temporary.pkl'


data = pd.read_html(DATA, header=0)[1]
data.to_pickle(FILE)
