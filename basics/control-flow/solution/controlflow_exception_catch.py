temperature = input('Type temperature: ')

try:
    float(temperature)
except ValueError:
    print('Invalid temperature')
    exit(1)
else:
    print(temperature)
