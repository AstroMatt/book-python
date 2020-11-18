"""
>>> assert type(result) is str
>>> result.count('\\n')
3
>>> result
'We choose to go to the Moon.\\nWe choose to go to the Moon in this decade and do the other things.\\nNot because they are easy, but because they are hard.\\n'
"""

DATA = [
    'We choose to go to the Moon.',
    'We choose to go to the Moon in this decade and do the other things.',
    'Not because they are easy, but because they are hard.']

result = ''

for line in DATA:
    result += line + '\n'
