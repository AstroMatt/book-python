import math

PRECISION = 2

degrees = input('What is the angle [deg]?: ')
radians = math.radians(float(degrees))

result = {
    'sin': round(math.sin(radians), PRECISION),
    'cos': round(math.cos(radians), PRECISION),
    'tg': round(math.tan(radians), PRECISION),
    'ctg': round(math.atan(radians), PRECISION),
    'PI': round(math.pi, PRECISION),
}

print(result)
