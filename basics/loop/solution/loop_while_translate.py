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
i = 0

while i < len(DATA):
    letter = DATA[i]
    letter = PL.get(letter, letter)
    result.append(letter)
    i += 1

result = ''.join(result)
