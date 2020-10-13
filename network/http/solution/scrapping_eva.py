import csv
from datetime import datetime
from pprint import pprint
from bs4 import BeautifulSoup
import requests


URL = 'https://www.worldspaceflight.com/bios/eva/eva.php'
FILE_HTML = r'eva.html'
FILE_CSV = r'eva.csv'


# When you dump page for the first time, you can test parsing on local file
# It saves bandwidth, and speeds you development
# Then comment following ``with`` context manager

with open(FILE_HTML, mode='w', encoding='utf-8') as file:
    response = requests.get(URL)
    file.write(response.text)


# Parser content below

with open(FILE_HTML, mode='r', encoding='utf-8') as file:
    content = file.read()

html = BeautifulSoup(content, 'html.parser')
table = html.find_all('table')[1]


def clean_Date(text):
    try:
        return datetime.strptime(text, '%d %B %Y').date()
    except ValueError:
        return text


def clean_Number(text):
    return int(text)


def clean_ISS(text):
    if text == '\xa0':
        return ''
    return text


def clean_Mission(text):
    return text


def clean_Participants(text):
    return ', '.join(x.string for x in text)


def clean_Duration(text):
    hours, minutes = text.split(':')
    result = ''

    if int(hours) != 0:
        result += f'{hours}h '

    if int(minutes[0]) == 0:
        minutes = minutes[1]

    result += f'{minutes}m'
    return result


def clean_Notes(text):
    if text == '\xa0':
        return ''
    return text


records = []

for row in table.find_all('tr')[1:]:
    td = row.find_all('td')

    records.append({
        'Number': clean_Number(td[0].string),
        'ISS': clean_ISS(td[1].string),
        'Mission': clean_Mission(td[2].string),
        'Participants': clean_Participants(td[3].find_all('a')),
        'Duration': clean_Duration(td[4].string),
        'Date': clean_Date(td[5].string),
        'Notes': clean_Notes(td[6].string),
    })


with open(FILE_CSV, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=records[0].keys(),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in records:
        writer.writerow(row)


pprint(records)
