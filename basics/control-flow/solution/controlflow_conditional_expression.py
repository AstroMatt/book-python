"""
>>> assert type(systolic) is int
>>> assert type(diastolic) is int
"""


blood_pressure = input('What is your Blood Pressure?: ')
systolic, diastolic = blood_pressure.strip().split('/')
systolic = int(systolic)
diastolic = int(diastolic)


if systolic >= 180 or diastolic >= 120:
    print('Hypertensive Crisis')

if systolic >= 140 or diastolic >= 90:
    print('Hypertension stage 2')
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    print('Hypertension stage 1')
elif 120 <= systolic < 129 and diastolic < 80:
    print('Elevated')
elif systolic < 120 and diastolic < 80:
    print('Normal')


## Alternative solution
# STATUS_NORMAL = 'Normal'
# STATUS_ELEVATED = 'Elevated'
# STATUS_HYPERTENSION_STAGE_1 = 'Hypertension stage 1'
# STATUS_HYPERTENSION_STAGE_2 = 'Hypertension stage 2'
# STATUS_HYPERTENSIVE_CRISIS = 'Hypertensive Crisis'
#
# status = []
#
# if 180 <= systolic or 120 <= diastolic:
#     status.append(STATUS_HYPERTENSIVE_CRISIS)
#
# if 140 <= systolic or 90 <= diastolic:
#     status.append(STATUS_HYPERTENSION_STAGE_2)
#
# elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
#     status.append(STATUS_HYPERTENSION_STAGE_1)
#
# elif 120 <= systolic <= 129 and diastolic < 80:
#     status.append(STATUS_ELEVATED)
#
# elif systolic < 120 and diastolic < 80:
#     status.append(STATUS_NORMAL)
#
# print(status)
