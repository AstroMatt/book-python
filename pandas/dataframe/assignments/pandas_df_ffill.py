"""
* Assignment: DataFrame Sample
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    TODO: English Translation

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    3. W danych kolumna "Order":
        a. określa kolejność astronauty/kosmonauty w kosmosie
        b. Czasami kilka osób leciało tym samym statkiem i ich numery powinny być takie same, a w danych jest `NaN`.
        c. Wypełnij brakujące indeksy stosując `df.ffill()`
    4. Ustaw wszystkie wiersze w losowej kolejności
    5. Zresetuj index nie pozostawiając kopii zapasowej starego
    6. Wypisz
        a. Pierwsze trzy wiersze
        b. Ostatnie 10% wierszy

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
         Order            Astronaut     Type              Date   Spacecraft
    0      244     Donald McMonagle  Orbital     28 April 1991       STS-39
    1       93        Georgi Ivanov  Orbital     10 April 1979     Soyuz 33
    2      387         Rick Husband  Orbital       27 May 1999       STS-96
    3      185       William Pailes  Orbital    3 October 1985         51-J
    4      390        Jeffrey Ashby  Orbital      23 July 1999       STS-93
    ..     ...                  ...      ...               ...          ...
    578    277       Franco Malerba  Orbital      31 July 1992       STS-46
    579     10         Leroy Cooper  Orbital       15 May 1963      Faith 7
    580    359       Carlos Noriega  Orbital       15 May 1997       STS-84
    581    192    Rodolfo Neri Vela  Orbital  27 November 1985         61-B
    582    559  David Saint-Jacques  Orbital   3 December 2018  Soyuz MS-11
    <BLANKLINE>
    [583 rows x 5 columns]
"""


# Given
import pandas as pd
import numpy as np
np.random.seed(0)


DATA = r'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-order.csv'

result = ...


# Solution
df = pd.read_csv(DATA)
df['Order'].ffill(inplace=True)
df['Order'] = df['Order'].astype(int)
df = df.sample(frac=1.0)
df.reset_index(drop=True, inplace=True)

result = df
