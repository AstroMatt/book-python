import sqlite3
import pandas as pd

DATA = r'https://www.worldspaceflight.com/bios/eva/eva4.php'
FILE = r'_temporary.sqlite3'


with sqlite3.connect(FILE) as db:
    data = pd.read_html(DATA, header=0)[1]
    data.to_sql('astro_eva', db)
