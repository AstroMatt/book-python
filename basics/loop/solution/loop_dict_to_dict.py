"""
>>> assert type(result) is dict
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': '6',
 'Prof-school': '6',
 'Masters': '5',
 'Bachelor': '5',
 'Engineer': '5',
 'HS-grad': '4',
 'Junior High': '3',
 'Primary School': '2',
 'Kindergarten': '1'}
"""


DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

result = {}

for idx, titles in DATA.items():
    for title in titles:
        result[title] = str(idx)
