"""
* Assignment: Mapping Dict Define
* Filename: mapping_dict_define.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: dict` representing input data
    3. Non-functional requirements:
        a. Assignmnet verifies creation of `dict()`
        b. Do not parse `DATA`, simply model `result` based on `DATA`
        c. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or any other control-flow statement

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: dict` reprezentujący dane wejściowe
    3. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `dict()`
        b. Nie parsuj `DATA`, po prostu zamodeluj `result` bazując na `DATA`
        c. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej

Tests:
    >>> assert type(result) is dict
    >>> assert 'firstname' in result
    >>> assert 'lastname' in result
    >>> assert 'missions' in result
    >>> assert result['firstname'] == 'Jan'
    >>> assert result['lastname'] == 'Twardowski'
    >>> assert 'Artemis' in result['missions']
    >>> assert 'Ares' in result['missions']
    >>> assert type(result['missions']) is list
"""

# Given
DATA = """
    First Name: Jan
    Last Name: Twardowski
    Missions: Apollo, Artemis
"""

# Solution
result = {
    'firstname': 'Jan',
    'lastname': 'Twardowski',
    'missions': ['Artemis', 'Ares'],
}
