"""
* Assignment: About Setup Doctest
* Filename: about_setup_doctest.py
* Complexity: easy
* Lines of code to write: 0 lines
* Estimated time: 5 min

English:
    1. Run doctests from this file
        a. Top menu -> Run -> Run... -> Doctest in about_setup_doctest
        b. Right mouse click -> Run 'Doctests in about_setup_doctest'
    2. All tests must pass
    3. Note the line with comment `# doctest: +NORMALIZE_WHITESPACE`
        a. This is the doctest flag
        b. It allows to ignore whitesapces and newlines in lists, tuples, dicts, etc.
        c. Try to remove it (without chaning the result) and check if tests still passes
    4. Write `100%` in shared spreadsheet at assignment row

Polish:
    1. Uruchom doctesty z tego pliku
        a. Górne menu -> Run -> Run... -> Doctest in about_setup_doctest
        b. Prawy przycisk myszy -> Run 'Doctests in about_setup_doctest'
    2. Wszystkie testy muszą przechodzić
    3. Zwróć uwagę na linijkę z komentarzem `# doctest: +NORMALIZE_WHITESPACE`
        a. To jest tzw. flaga sterująca doctest
        b. Pozwala na zignorowanie łamań linii i spacji w listach, tuplach, dictach, itp
        c. Spróbuj usunąć ten zapis (nie modyfikuj wyniku) i zobacz czy testy nadal przechodzą
    4. Zapisz `100%` we współdzielonym arkuszu kalkulacyjnym w wierszu zadania

Tests:
    >>> type(firstname)
    <class 'str'>
    >>> type(lastname)
    <class 'str'>
    >>> f'{firstname} {lastname}'
    'Mark Watney'
    >>> firstname + lastname
    'MarkWatney'
    >>> firstname + ' ' + lastname
    'Mark Watney'
    >>> [firstname] + [lastname]
    ['Mark', 'Watney']
    >>> [firstname] + [lastname] # doctest: +NORMALIZE_WHITESPACE
    ['Mark',
     'Watney']
"""

# Given
firstname = 'Mark'
lastname = 'Watney'


# Solution
firstname = 'Mark'
lastname = 'Watney'
