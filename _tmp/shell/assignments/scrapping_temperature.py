HTML = '''<table border="2" cellspacing="0" cellpadding="4" rules="all" style="border-collapse:collapse; empty-cells:show; margin: 2ex 2em; border: solid 1px #aaaaaa; font-size: 95%; text-align: right"><caption></caption><tbody><tr align="center"><th>x</th><th>10&nbsp;°C</th><th>5&nbsp;°C</th><th>0&nbsp;°C</th><th>−5&nbsp;°C</th><th>−10&nbsp;°C</th><th>−15&nbsp;°C</th><th>−20&nbsp;°C</th><th>−25&nbsp;°C</th><th>−30&nbsp;°C</th><th>−35&nbsp;°C</th><th>−40&nbsp;°C</th><th>−45&nbsp;°C</th><th>−50&nbsp;°C</th></tr><tr><td><b>10 km/h</b></td><td>8,6</td><td>2,7</td><td>−3,3</td><td>−9,3</td><td>−15,3</td><td>−21,1</td><td>−27,2</td><td>−33,2</td><td>−39,2</td><td>−45,1</td><td>−51,1</td><td>−57,1</td><td>−63,0</td></tr><tr><td><b>15 km/h</b></td><td>7,9</td><td>1,7</td><td>−4,4</td><td>−10,6</td><td>−16,7</td><td>−22,9</td><td>−29,1</td><td>−35,2</td><td>−41,4</td><td>−47,6</td><td>−53,74</td><td>−59,9</td><td>−66,1</td></tr><tr><td><b>20 km/h</b></td><td>7,4</td><td>1,1</td><td>−5,2</td><td>−11,6</td><td>−17,9</td><td>−24,2</td><td>−30,5</td><td>−36,8</td><td>−43,1</td><td>−49,4</td><td>−55,7</td><td>−62,0</td><td>−69,3</td></tr><tr><td><b>25 km/h</b></td><td>6,9</td><td>0,5</td><td>-5,9</td><td>−12,3</td><td>−18,8</td><td>−25,2</td><td>−31,6</td><td>−38,0</td><td>−44,5</td><td>−50,9</td><td>−57,3</td><td>−63,7</td><td>−70,2</td></tr><tr><td><b>30 km/h</b></td><td>6,6</td><td>0,1</td><td>−6,5</td><td>−13,0</td><td>−19,5</td><td>−26,0</td><td>−32,6</td><td>−39,1</td><td>−45,6</td><td>−52,1</td><td>−58,7</td><td>−65,2</td><td>−71,7</td></tr><tr><td><b>35 km/h</b></td><td>6,3</td><td>−0,4</td><td>−7,0</td><td>−13,6</td><td>−20,2</td><td>−26,8</td><td>−33,4</td><td>−40,0</td><td>−46,6</td><td>−53,2</td><td>−59,8</td><td>−66,4</td><td>−73,1</td></tr><tr><td><b>40 km/h</b></td><td>6,0</td><td>−0,7</td><td>−7,4</td><td>−14,1</td><td>−20,8</td><td>−27,4</td><td>−34,1</td><td>−40,8</td><td>−47,5</td><td>−54,2</td><td>−60,9</td><td>−67,6</td><td>−74,2</td></tr><tr><td><b>45 km/h</b></td><td>5,7</td><td>−1,0</td><td>−7,8</td><td>−14,5</td><td>−21,3</td><td>−28,0</td><td>−34,8</td><td>−41,5</td><td>−48,3</td><td>−55,1</td><td>−61,8</td><td>−68,6</td><td>−75,3</td></tr><tr><td><b>50 km/h</b></td><td>5,5</td><td>−1,3</td><td>−8,1</td><td>−15,0</td><td>−21,8</td><td>−28,6</td><td>−35,4</td><td>−42,2</td><td>−49,0</td><td>−55,8</td><td>−62,7</td><td>−69,5</td><td>−76,3</td></tr><tr><td><b>55 km/h</b></td><td>5,3</td><td>−1,6</td><td>−8,5</td><td>−15,3</td><td>−22,2</td><td>−29,1</td><td>−36,0</td><td>−42,8</td><td>−49,7</td><td>−56,6</td><td>−63,4</td><td>−70,3</td><td>−77,2</td></tr><tr><td><b>60 km/h</b></td><td>5,1</td><td>−1,8</td><td>−8,8</td><td>−15,7</td><td>−22,6</td><td>−29,5</td><td>−36,5</td><td>−43,4</td><td>−50,3</td><td>−57,2</td><td>−64,2</td><td>−71,1</td><td>−78,0</td></tr><tr style="text-align: left"><td bgcolor="#FFEBAD" colspan="14">Table 1: Example values of the temperature according to model 1</td></tr></tbody></table>'''


from pprint import pprint
from bs4 import BeautifulSoup
import requests


def clean_table_header(text):
    text = text.replace('\xa0', ' ')
    text = text.strip()
    return text


def clean_value(text):
    text = text.strip()
    text = text.replace(',', '.')
    text = text.replace('−', '-')
    return float(text)


URL = 'https://pl.wikipedia.org/wiki/Temperatura_odczuwalna'
result = list()

response = requests.get(URL)
html = BeautifulSoup(response.text, 'html.parser')
table = html.find_all('table')[0]

table_rows = table.find_all('tr')
table_header = table_rows[0].find_all('th')
table_header = [clean_table_header(th.text) for th in table_header]
table_header[0] = 'wind speed'
table_rows = table_rows[1:-1]


for tr in table_rows:
    row_cells = tr.find_all('td')
    row_header = row_cells[0].text
    row_cells = [clean_value(td.text) for td in row_cells[1:]]
    row_cells = [row_header] + row_cells
    row_dict = dict()

    for i, _ in enumerate(table_header):
        key = table_header[i]
        value = row_cells[i]
        row_dict[key] = value

    result.append(row_dict)


pprint(result)


import pandas as pd

df = pd.DataFrame(result)
df.set_index('wind speed', inplace=True)

