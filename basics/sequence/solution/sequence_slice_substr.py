"""
>>> assert type(result) is str
>>> result
'We choose the Moon!'
"""

TEXT = 'We choose to go to the Moon!'
REMOVE = 'to go to '

a = TEXT.find(REMOVE)   # 10
b = a + len(REMOVE)     # 19

first_part = TEXT[:a]   # 'We choose '
second_part = TEXT[b:]  # 'the Moon!'

result = first_part + second_part

