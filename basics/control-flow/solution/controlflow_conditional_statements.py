AGE_ADULT = 18


age = input('What is your age?: ')
age = int(age.strip())

if age >= AGE_ADULT:
    result = 'Adult'
else:
    result = 'Young'

print(result)
