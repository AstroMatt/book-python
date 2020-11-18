"""
>>> import statistics
>>> assert type(mean) is float
>>> assert all(type(x) is float for x in result)
>>> assert statistics.mean(result) == mean
"""

GRADE_SCALE = (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)
result = []

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in GRADE_SCALE:
        result.append(grade)
    else:
        print('Grade is not allowed')

if result:
    mean = sum(result) / len(result)
    print(f'Mean: {mean}')
else:
    print('Empty report card')
