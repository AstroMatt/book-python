"""
>>> assert type(result) is str
>>> assert '\U0001F642' in result
>>> assert name in result
"""

name = input('What is your name?: ')
result = f'Hello {name} \U0001F642'
