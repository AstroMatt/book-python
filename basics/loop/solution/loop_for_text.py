"""
* Assignment: Loop For Text
* Filename: loop_for_text.py
* Complexity: medium
* Lines of code to write: 14 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Given is text of the "Moon Speech" by John F. Kennedy's [1]
    3. Sentences are separated by period (`.`)
    4. Clean each sentence from whitespaces at the beginning and at the end
    5. Words are separated by spaces
    6. Print the total number in whole text:
        a. adverbs (words ending with "ly")
        b. sentences
        c. words
        d. letters
        e. characters (including spaces inside sentences, but without comas `,`)
        f. comas (`,`)
    7. Compare results with "Output" section below

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dany jest tekst przemówienia "Moon Speech" wygłoszonej przez John F. Kennedy'ego [1]
    3. Zdania oddzielone są kropkami (`.`)
    4. Każde zdanie oczyść z białych znaków na początku i końcu
    5. Słowa oddzielone są spacjami
    6. Wypisz także ile jest łącznie w całym tekście:
        a. przysłówków (słów zakończonych na "ly")
        b. zdań
        c. słów
        d. liter
        e. znaków (łącznie ze spacjami wewnątrz zdań, ale bez przecinków `,`)
        f. przecinków (`,`)
    7. Porównaj wynik z sekcją "Output" poniżej

References:
    [1] Kennedy, J.F. Moon Speech - Rice Stadium. 1962. URL: http://er.jsc.nasa.gov/seh/ricetalk.htm

Tests:
    >>> type(result)
    <class 'dict'>
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    {'sentences': 7,
    'words': 71,
    'characters': 347,
    'letters': 283,
    'commas': 1,
    'adverbs': 0}
"""

# Given
TEXT = """
    We choose to go to the Moon.
    We choose to go to the Moon in this decade and do the other things.
    Not because they are easy, but because they are hard.
    Because that goal will serve to organize and measure the best of our energies and skills.
    Because that challenge is one that we are willing to accept.
    One we are unwilling to postpone.
    And one we intend to win
"""

result: dict = {
    'sentences': 0,
    'words': 0,
    'characters': 0,
    'letters': 0,
    'commas': 0,
    'adverbs': 0,
}

# Solution
for sentence in TEXT.split('.'):
    sentence = sentence.strip()
    words = sentence.split()
    letters = sentence.replace(',', '').replace(' ', '')
    characters = sentence.replace(',', '')
    comas = sentence.count(',')

    result['sentences'] += 1
    result['words'] += len(words)
    result['letters'] += len(letters)
    result['characters'] += len(characters)
    result['commas'] += comas

    for word in words:
        if word.endswith('ly'):
            result['adverbs'] += 1


