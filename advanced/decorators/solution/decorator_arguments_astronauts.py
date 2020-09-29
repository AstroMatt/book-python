"""
>>> launch(CREW_PRIMARY)
'Launching: Jan Twardowski, Mark Watney, Melissa Lewis'

>>> launch(CREW_BACKUP)
Traceback (most recent call last):
    ...
PermissionError: Alex Vogel is not an astronaut
"""

CREW_PRIMARY = [
    {'is_astronaut': True, 'name': 'Jan Twardowski'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': True, 'name': 'Melissa Lewis'}]

CREW_BACKUP = [
    {'is_astronaut': True, 'name': 'Melissa Lewis'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': False, 'name': 'Alex Vogel'}]


def check(field, value):
    def decorator(func):
        def wrapper(crew):
            for member in crew:
                if member.get(field) != value:
                    name = member['name']
                    raise PermissionError(f'{name} is not an astronaut')
            return func(crew)
        return wrapper
    return decorator


@check(field='is_astronaut', value=True)
def launch(crew):
    crew = ', '.join(astro['name'] for astro in crew)
    return f'Launching: {crew}'
