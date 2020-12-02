"""
* Assignment: Mapping Dict Get
* Filename: mapping_dict_get.py
* Complexity: easy
* Lines of code: 2 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create translator of pilot's alphabet
    3. Each letter has it's phonetic counterpart
    4. Ask user to input letter
    5. User will always put only one capitalized letter or number
    6. Print phonetic letter pronunciation
    7. If user type character not existing in alphabet, print: "Pilots don't say that"
    8. Do not use `if`, `try`, and `except`

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz tłumacza alfabetu pilotów
    3. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
    4. Poproś użytkownika o wprowadzenie litery
    5. Użytkownik zawsze poda tylko jedną dużą literę lub cyfrę
    6. Wypisz fonetyczną wymowę litery
    7. Jeżeli wpisał znak, który nie występuje w alfabecie, wypisz: "Pilots don't say that"
    8. Nie używaj `if`, `try` ani `except`

Tests:
    TODO doctests
"""

# Given
ALPHABET = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whisky',
    'X': 'X-Ray',
    'Z': 'Zulu',
}

# Solution
letter = input('Type letter: ')
result = ALPHABET.get(letter, "Pilots don't say that")
