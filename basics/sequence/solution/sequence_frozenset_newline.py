"""
>>> assert type(result) is str
>>> assert 'We choose to go to the Moon.' in result
>>> assert 'We choose to go to the Moon in this decade and do the other things.' in result
>>> assert 'Not because they are easy, but because they are hard.' in result
>>> result.count('\\n')
2
"""

DATA = frozenset({
    'We choose to go to the Moon.',
    'We choose to go to the Moon in this decade and do the other things.',
    'Not because they are easy, but because they are hard.'})

result = '\n'.join(DATA)
