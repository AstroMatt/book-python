"""
>>> assert type(result) is str
>>> result
'zazolc gesla jazn'
"""

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

result = []

for letter in DATA:
    letter = PL.get(letter, letter)
    result.append(letter)

result = ''.join(result)

