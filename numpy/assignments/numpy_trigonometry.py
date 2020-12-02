import numpy as np


deg = input('Type angle [deg]: ')
deg = float(deg)

if deg == 180:
    raise ArithmeticError('Cotangent does not exist')

rad = np.deg2rad(deg)
sin = np.sin(rad)
cos = np.cos(rad)
tan = np.tan(rad)
ctg = 1 / tan

print(f'Sinus: {sin}')
print(f'Cosinus: {cos}')
print(f'Tangent: {tan}')
print(f'Cotangent: {ctg}')
