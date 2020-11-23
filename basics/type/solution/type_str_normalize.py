"""
* Assignment name: Type String Normalize
* Suggested filename: type_str_normalize.py
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use ``str`` methods to clean ``DATA``
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wykorzystaj metody ``str`` do oczyszczenia ``DATA``
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result
    'Jana Twardowskiego III'
"""

# Given
DATA = 'UL. jana \tTWArdoWskIEGO 3'

# Solution
result = (
    DATA.upper()                # Convert to common format
        .replace('\t', '')      # Remove unwanted whitespaces
        .replace('.', '')       # Remove unwanted special characters
        .replace('UL', '')      # Remove unwanted text
        .replace('3', 'III')    # Substitute text
        .title()                # Formatting
        .replace('Iii', 'III')  # Clean-up
        .strip()
)
