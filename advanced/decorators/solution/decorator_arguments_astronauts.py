"""
* Assignment: Decorator Arguments Astronauts
* Filename: decorator_arguments_astronauts.py
* Complexity: easy
* Lines of code to write: 4 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator `check_astronauts`
    3. To answer if person is an astronaut check field:
       `is_astronaut` in `crew: list[dict]`
    4. Decorator will call decorated function, only if all crew members has
       field with specified value
    5. Both field name and value are given as keyword arguments to decorator
    6. If any member is not an astronaut raise `PermissionError` and print
       his first name and last name
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator `check_astronauts`
    3. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole:
       `is_astronaut` in `crew: list[dict]`
    4. Dekorator wywoła dekorowaną funkcję tylko wtedy, gdy każdy członek
       załogi ma pole o podanej wartości
    5. Zarówno nazwa pola jak i wartość są podawane jako argumenty nazwane do dekoratora
    6. Jeżeli, jakikolwiek członek nie jest astronautą, podnieś wyjątek
       `PermissionError` i wypisz jego imię i nazwisko
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> CREW_PRIMARY = [
    ...    {'is_astronaut': True, 'name': 'Jan Twardowski'},
    ...    {'is_astronaut': True, 'name': 'Mark Watney'},
    ...    {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    >>> CREW_BACKUP = [
    ...    {'is_astronaut': True, 'name': 'Melissa Lewis'},
    ...    {'is_astronaut': True, 'name': 'Mark Watney'},
    ...    {'is_astronaut': False, 'name': 'Alex Vogel'}]

    >>> @check_astronauts(field='is_astronaut', value=True)
    ... def launch(crew):
    ...    crew = ', '.join(astro['name'] for astro in crew)
    ...    return f'Launching: {crew}'

    >>> launch(CREW_PRIMARY)
    'Launching: Jan Twardowski, Mark Watney, Melissa Lewis'

    >>> launch(CREW_BACKUP)
    Traceback (most recent call last):
    PermissionError: Alex Vogel is not an astronaut

    >>> @check_astronauts(field='name', value='Melissa Lewis')
    ... def launch(crew):
    ...    crew = ', '.join(astro['name'] for astro in crew)
    ...    return f'Launching: {crew}'

    >>> launch(CREW_PRIMARY)
    Traceback (most recent call last):
    PermissionError: Jan Twardowski is not an astronaut

    >>> launch(CREW_BACKUP)
    Traceback (most recent call last):
    PermissionError: Mark Watney is not an astronaut
"""


# Given
def check_astronauts(field, value):
    def decorator(func):
        def wrapper(crew):
            return func(crew)
        return wrapper
    return decorator


# Solution
def check_astronauts(field, value):
    def decorator(func):
        def wrapper(crew):
            for member in crew:
                if member.get(field) != value:
                    name = member['name']
                    raise PermissionError(f'{name} is not an astronaut')
            return func(crew)
        return wrapper
    return decorator
