"""
* Assignment: Function Arguments Sequence
* Filename: function_args_sequence.py
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 3 min

English:
    1. Define function which takes sequence of integers as an argument
    2. Sum only even numbers
    3. Print returned value

Polish:
    1. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    2. Zsumuj tylko parzyste liczby
    3. Wypisz zwróconą wartość

Tests:
    TODO: Doctests
"""


# Solution
def total(sequence):
    return sum(x for x in sequence if x % 2 == 0)


print(total([1, 2, 3, 4]))
# 6

print(total([1, 1, 2]))
# 2

print(total([0, 2, 4, 9]))
# 6
