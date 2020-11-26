"""
* Assignment: Decorator Function Astronauts
* Filename: decorator_func_astronauts.py
* Complexity: easy
* Lines of code to write: 7 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator `check_astronauts`
    3. To answer if person is an astronaut check field `is_astronaut` in `crew: list[dict]`
    4. Decorator will call decorated function, only if all crew members are astronauts
    5. If any member is not an astronaut raise `PermissionError` and print his first name and last name
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Stwórz dekorator `check_astronauts`
    3. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole `is_astronaut` in `crew: list[dict]`
    4. Dekorator wywoła dekorowaną funkcję, tylko gdy wszyscy członkowie załogi są astronautami
    5. Jeżeli, jakikolwiek członek nie jest astronautą, podnieś wyjątek `PermissionError` i wypisz jego imię i nazwisko
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> assert isfunction(check_astronauts)
    >>> assert isfunction(check_astronauts(lambda: None))

    >>> @check_astronauts
    ... def launch(crew):
    ...     crew = ', '.join(astro['name'] for astro in crew)
    ...     return f'Launching: {crew}'

    >>> launch(CREW_PRIMARY)
    'Launching: Jan Twardowski, Mark Watney, Melissa Lewis'

    >>> launch(CREW_BACKUP)
    Traceback (most recent call last):
        ...
    PermissionError: Alex Vogel is not an astronaut
"""

# Given
CREW_PRIMARY = [
    {'is_astronaut': True, 'name': 'Jan Twardowski'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': True, 'name': 'Melissa Lewis'}]

CREW_BACKUP = [
    {'is_astronaut': True, 'name': 'Melissa Lewis'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': False, 'name': 'Alex Vogel'}]


# Solution
def check_astronauts(func):
    def wrapper(crew):
        for member in crew:
            if not member['is_astronaut']:
                raise PermissionError(f'{member["name"]} is not an astronaut')
        return func(crew)
    return wrapper
