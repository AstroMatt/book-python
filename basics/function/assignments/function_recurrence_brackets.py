"""
* Assignment: Function Recurrence Brackets
* Filename: function_recurrence_brackets.py
* Complexity: medium
* Lines of code: 10 lines
* Time: 21 min

English:
    1. Create function which checks if brackets are balanced
    2. Brackets are balanced, when each opening bracket has closing pair
    3. Use recursion
    4. Types of brackets:
        a. round: `(` i `)`
        b. square: `[` i `]`
        c. curly `{` i `}`
        d. angle `<` i `>`

Polish:
    1. Stwórz funkcję, która sprawdzi czy nawiasy są zbalansowane
    2. Nawiasy są zbalansowane, gdy każdy otwierany nawias ma zamykającą parę
    3. Użyj rekurencji
    4. Typy nawiasów:
        a. okrągłe: `(` i `)`
        b. kwadratowe: `[` i `]`
        c. klamrowe `{` i `}`
        d. trójkątne `<` i `>`

Tests:
    >>> is_bracket_balanced('{}')
    True
    >>> is_bracket_balanced('()')
    True
    >>> is_bracket_balanced('[]')
    True
    >>> is_bracket_balanced('<>')
    True
    >>> is_bracket_balanced('')
    True
    >>> is_bracket_balanced('(')
    False
    >>> is_bracket_balanced('}')
    False
    >>> is_bracket_balanced('(]')
    False
    >>> is_bracket_balanced('([)')
    False
    >>> is_bracket_balanced('[()')
    False
    >>> is_bracket_balanced('{()[]}')
    True
    >>> is_bracket_balanced('() [] () ([]()[])')
    True
    >>> is_bracket_balanced("( (] ([)]")
    False
"""

# Given
BRACKET_OPEN = ('(', '{', '[', '<')
BRACKET_CLOSE = (')', '}', ']', '>')
PAIRS = dict(zip(BRACKET_OPEN, BRACKET_CLOSE))


# Solution
def matches(opened_brackets, bracket):
    if not opened_brackets:
        return False

    opening_brackets = opened_brackets.pop()
    return PAIRS[opening_brackets] == bracket


def is_bracket_balanced(text):
    opened_brackets = []

    for character in text:
        if character in BRACKET_OPEN:
            opened_brackets.append(character)
        elif character in BRACKET_CLOSE:
            if not matches(opened_brackets, character):
                return False
    return not opened_brackets
