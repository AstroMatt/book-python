CREW_PRIMARY = [
    {'is_astronaut': True, 'name': 'Jan Twardowski'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': True, 'name': 'Melissa Lewis'}]

CREW_BACKUP = [
    {'is_astronaut': True, 'name': 'Melissa Lewis'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': False, 'name': 'Alex Vogel'}]


def check_astronauts(func):
    def wrapper(crew):
        for member in crew:
            if not member['is_astronaut']:
                raise PermissionError(f'{member["name"]} is not an astronaut')
        return func(crew)
    return wrapper


@check_astronauts
def launch(crew):
    crew = ', '.join(astro['name'] for astro in crew)
    print(f'Launching {crew}')


launch(CREW_PRIMARY)
launch(CREW_BACKUP)
