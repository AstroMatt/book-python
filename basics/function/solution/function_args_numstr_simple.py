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


def translate(number):
    """
    >>> translate(1969)
    'one niner six niner'

    >>> translate(31337)
    'tree one tree tree seven'

    >>> translate(13.37)
    'one tree and tree seven'

    >>> translate(31.337)
    'tree one and tree tree seven'

    >>> translate(-1969)
    'minus one niner six niner'

    >>> translate(-31.337)
    'minus tree one and tree tree seven'

    >>> translate(-49.35)
    'minus fower niner and tree fife'
    """
    return ' '.join(data[c] for c in str(number))
