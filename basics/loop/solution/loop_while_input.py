"""
>>> import statistics
>>> assert type(mean) is float
>>> assert all(type(x) is float for x in result)
>>> assert statistics.mean(result) == mean
"""

GRADE_SCALE = (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)
report_card = []

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in GRADE_SCALE:
        report_card.append(grade)
    else:
        print('Grade is not allowed')

if report_card:
    mean = sum(report_card) / len(report_card)
    print(f'Mean: {mean}')
else:
    print('Empty report card')
