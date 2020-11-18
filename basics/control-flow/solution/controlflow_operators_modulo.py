"""
>>> '5' % 2
Traceback (most recent call last):
    ...
TypeError: not all arguments converted during string formatting

>>> '5%s' % 2
'52'

>>> 5 % 2
1
"""


number = input('What is your number?: ')
result = float(number) % 2 == 0

print(result)
