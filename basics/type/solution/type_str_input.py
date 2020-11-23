"""
* Assignment name: Type String Input
* Suggested filename: type_str_input.py
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    1. Ask user to input text
    2. Define ``result`` with number of characters of input text

Polish:
    1. Poproś użytkownika o wprowadzenie tekstu
    2. Zdefiniuj ``result`` z liczbą znaków wprowadzonego tekstu

Tests:
    >>> type(result)
    <class 'int'>
"""

# Solution
text = input('Type text: ')
result = len(text)
