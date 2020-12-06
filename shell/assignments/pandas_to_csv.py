import pandas as pd

DATA = r'https://www.worldspaceflight.com/bios/eva/eva.php'
FILE = r'_temporary.csv'

data = pd.read_html(DATA, header=0)[1]
data.to_csv(FILE)

