degrees = input('Type angle [deg]: ')


class CotangentError(Exception):
    pass


if int(degrees) == 180:
    raise CotangentError('Cotangent for 180 degrees is infinite')
