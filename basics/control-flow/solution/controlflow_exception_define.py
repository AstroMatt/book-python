temperature = input('Type temperature: ')


class NegativeKelvinError(Exception):
    pass


if float(temperature) < 0:
    raise NegativeKelvinError
