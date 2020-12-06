"""
* Assignment: File Path Abspath
* Filename: file_path_abspath.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Using `input()` ask user for a file path
    2. Convert path to absolute
    3. Print if path exists and leads to file or directory
    4. Compare result with "Tests" section (see below)

Polish:
    1. Używając `input()` zapytaj użytkownika o ścieżkę do pliku
    2. Przekonwertuj ścieżkę do bezwzględnej
    3. Wypisz czy ścieżka istnieje i czy prowadzi do pliku czy katalogu
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> isinstance(result, Path)
    True
    >>> current_directory = Path.cwd()
    >>> str(current_directory) in str(result)
    True
"""

# Given
filename = input('Type filename: ')

# Solution
from pathlib import Path
result = Path(Path.cwd(), filename)
