"""
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
'''My name... "José Jiménez".
\tI'm an \"\"\"astronaut!\"\"\"'''
"""

name = input('What is your name?: ')
result = f"""'''My name... "{name}".\n\tI\'m an \"\"\"astronaut!\"\"\"'''"""
