ADULT_AGE = 18
age = input('Type age: ')
age = float(age)

if age < ADULT_AGE:
    raise PermissionError('Adults only')
