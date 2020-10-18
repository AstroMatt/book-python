import pandas as pd

LETTERS_PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                'ł': 'l', 'ń': 'n', 'ó': 'o',
                'ś': 's', 'ż': 'z', 'ź': 'z'}

LETTERS_PLEN.update({k.upper():v.upper()
                     for k,v in LETTERS_PLEN.items()})


def substitute(text):
    return ''.join(LETTERS_PLEN.get(x,x) for x in text)


trl = pd.read_excel(io='../_data/trl.xlsx',
                    sheet_name='Polish',
                    header=1,
                    index_col=0)

trl = trl.applymap(substitute)
trl.columns = trl.columns.map(substitute)

trl
