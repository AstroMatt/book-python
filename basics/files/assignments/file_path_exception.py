"""
* Assignment: File Path Exception
* Filename: file_path_exception.py
* Complexity: easy
* Lines of code: 6 lines
* Estimated time: 2 min

English:
    1. Using `input()` ask user for a file path
    3. Handle exception for not existing file
    4. Handle exception for not having sufficient permissions

Polish:
    1. Używając `input()` zapytaj użytkownika o ścieżkę do pliku
    3. Obsłuż wyjątek dla nieistniejącego pliku
    4. Obsłuż wyjątek dla braku wystarczających uprawnień

Tests:
    TODO: Doctests
"""

# Given
filename = input('Type filename: ')

# Solution
try:
    file = open(filename)
except FileNotFoundError:
    print('Sorry, file not found')
except PermissionError:
    print('Sorry, not permitted')
