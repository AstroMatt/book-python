import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-dates.csv'

MONTHS_PLEN = {'styczeń': 'January',
               'luty': 'February',
               'marzec': 'March',
               'kwiecień': 'April',
               'maj': 'May',
               'czerwiec': 'June',
               'lipiec': 'July',
               'sierpień': 'August',
               'wrzesień': 'September',
               'październik': 'October',
               'listopad': 'November',
               'grudzień': 'December'}


## Solution 1
astro = pd.read_csv(DATA)

astro['Mission Date'] = astro['Mission Date'] \
     .replace(MONTHS_PLEN, regex=True) \
     .apply(pd.Timestamp)

astro


## Solution 2
def substitute(original):
    for pl, en in MONTHS_PLEN.items():
        translated = original.replace(pl, en)
        if original != translated:
            return translated


astro = pd.read_csv(DATA)
astro['Mission Date'] = astro['Mission Date']\
                             .apply(substitute)\
                             .apply(pd.Timestamp)
astro
