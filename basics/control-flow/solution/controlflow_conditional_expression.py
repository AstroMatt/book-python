"""
* Assignment: Conditional Expression
* Filename: controlflow_conditional_expression.py
* Complexity: medium
* Lines of code to write: 10 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Table contains Blood Pressure classification according to American Heart Association :cite:`Whelton2018`
    3. User inputs blood pressure in `XXX/YY` or `XXX/YYY` format
    4. User will not try to input invalid data
    5. Data format:
        a. `XXX: int` systolic pressure
        b. `YY: int` or `YYY: int` diastolic pressure
    6. Print status of given blood pressure
    7. If systolic and diastolic values are in different categories, assume worst case

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Tabela zawiera klasyfikację ciśnienia krwi wg American Heart Association :cite:`Whelton2018`
    3. Użytkownik wprowadza ciśnienie krwi w formacie `XXX/YY` lub `XXX/YYY`
    4. Użytkownik nie będzie próbował wprowadzać danych niepoprawnych
    5. Format danych:
        a. `XXX: int` to wartość ciśnienia skurczowego (ang. *systolic*)
        b. `YY: int` lub `YYY: int` to wartość ciśnienia rozkurczowego (ang. *diastolic*)
    6. Wypisz status wprowadzonego ciśnienia krwi
    7. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek

Given:
    | Blood Pressure Category | Systolic [mm Hg] | Operator | Diastolic [mm Hg] |
    |-------------------------|------------------|----------|-------------------|
    | Normal                  | Less than 120    | and      | Less than 80      |
    | Elevated                | 120-129          | and      | Less than 80      |
    | Hypertension stage 1    | 130-139          | or       | 80-89             |
    | Hypertension stage 2    | 140 or higher    | or       | 90 or higher      |
    | Hypertensive Crisis     | Higher than 180  | and/or   | Higher than 120   |

Tests:
    TODO: Doctests
    '119/79': 'Normal',
    '120/80': 'Hypertension stage 1',
    '121/79': 'Elevated',
    '120/81': 'Hypertension stage 1',
    '130/80': 'Hypertension stage 1',
    '130/89': 'Hypertension stage 1',
    '140/85': 'Hypertension stage 2',
    '140/89': 'Hypertension stage 2',
    '141/90': 'Hypertension stage 2',
    '141/91': 'Hypertension stage 2',
    '180/120': ('Hypertension stage 2', 'Hypertensive Crisis')
"""

# Given
blood_pressure = input('What is your Blood Pressure?: ')
systolic, diastolic = blood_pressure.strip().split('/')
systolic = int(systolic)
diastolic = int(diastolic)

# Solution
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
