"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
{0: 'setosa',
 1: 'versicolor',
 2: 'virginica'}
"""

DATA = ['setosa', 'versicolor', 'virginica']

result = dict(enumerate(DATA))
