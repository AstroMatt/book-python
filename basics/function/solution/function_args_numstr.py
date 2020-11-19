"""
>>> pilot_say(1969)
'one niner six niner'
>>> pilot_say(31337)
'tree one tree tree seven'
>>> pilot_say(13.37)
'one tree and tree seven'
>>> pilot_say(31.337)
'tree one and tree tree seven'
>>> pilot_say(-1969)
'minus one niner six niner'
>>> pilot_say(-31.337)
'minus tree one and tree tree seven'
>>> pilot_say(-49.35)
'minus fower niner and tree fife'
"""

DATA = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'tree',
    4: 'fower',
    5: 'fife',
    6: 'six',
    7: 'seven',
    8: 'ait',
    9: 'niner',
}

data = {str(k):v for k,v in DATA.items()}
data['-'] = 'minus'
data['.'] = 'and'


def pilot_say(number):
    return ' '.join(data[x] for x in str(number))
