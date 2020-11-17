"""
>>> assert type(result) is str
>>> result
'We choose the Moon!'
"""

TEXT = 'We choose to go to the Moon!'
REMOVE = 'to go to '

a = TEXT.find(REMOVE)   # 10
b = a + len(REMOVE)     # 19

result = TEXT[:a] + TEXT[b:]
