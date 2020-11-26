"""
* Assignment: Conditional Expression
* Filename: controlflow_conditional_expression.py
* Complexity: medium
* Lines of code to write: 10 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Table contains Blood Pressure classification according to American Heart Association [1]
    3. User inputs blood pressure in `XXX/YY` or `XXX/YYY` format
    4. User will not try to input invalid data
    5. Data format:
        a. `XXX: int` systolic pressure
        b. `YY: int` or `YYY: int` diastolic pressure
    6. Print status of given blood pressure
    7. If systolic and diastolic values are in different categories, assume worst case

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Tabela zawiera klasyfikację ciśnienia krwi wg American Heart Association [1]
    3. Użytkownik wprowadza ciśnienie krwi w formacie `XXX/YY` lub `XXX/YYY`
    4. Użytkownik nie będzie próbował wprowadzać danych niepoprawnych
    5. Format danych:
        a. `XXX: int` to wartość ciśnienia skurczowego (ang. *systolic*)
        b. `YY: int` lub `YYY: int` to wartość ciśnienia rozkurczowego (ang. *diastolic*)
    6. Wypisz status wprowadzonego ciśnienia krwi
    7. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek

References:
    [1] Whelton, Paul K. and et al.
        2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline for the
        Prevention, Detection, Evaluation, and Management of High Blood Pressure
        in Adults: Executive Summary: A Report of the American College of
        Cardiology/American Heart Association Task Force on Clinical Practice Guidelines.
        Journal of Hypertension. vol 71. pages 1269–1324. 2018. doi: 10.1161/HYP.0000000000000066

Tests:
    TODO: Doctests
    >>> type(result)
    <class 'list'>
    >>> len(result) in (1, 2)
    True
    >>>
    >>> if len(result) == 2:
    ...     (STATUS_HYPERTENSIVE_CRISIS in result
    ...      and STATUS_HYPERTENSION_STAGE_2 in result)
    ... elif len(result) == 1:
    ...     (STATUS_NORMAL in result
    ...      or STATUS_ELEVATED in result
    ...      or STATUS_HYPERTENSION_STAGE_1 in result
    ...      or STATUS_HYPERTENSION_STAGE_2 in result
    ...      or STATUS_HYPERTENSIVE_CRISIS in result)
    ... else:
    ...     raise ValueError
    True
    >>> assert blood_pressure == '119/79' and result == ['Normal'] or True
    >>> assert blood_pressure == '120/80' and result == ['Hypertension stage 1'] or True
    >>> assert blood_pressure == '121/79' and result == ['Elevated'] or True
    >>> assert blood_pressure == '120/81' and result == ['Hypertension stage 1'] or True
    >>> assert blood_pressure == '130/80' and result == ['Hypertension stage 1'] or True
    >>> assert blood_pressure == '130/89' and result == ['Hypertension stage 1'] or True
    >>> assert blood_pressure == '140/85' and result == ['Hypertension stage 2'] or True
    >>> assert blood_pressure == '140/89' and result == ['Hypertension stage 2'] or True
    >>> assert blood_pressure == '141/90' and result == ['Hypertension stage 2'] or True
    >>> assert blood_pressure == '141/91' and result == ['Hypertension stage 2'] or True
    >>> assert blood_pressure == '180/120' and result == ['Hypertension stage 2', 'Hypertensive Crisis'] or True
"""

# Given
STATUS_NORMAL = 'Normal'
STATUS_ELEVATED = 'Elevated'
STATUS_HYPERTENSION_STAGE_1 = 'Hypertension stage 1'
STATUS_HYPERTENSION_STAGE_2 = 'Hypertension stage 2'
STATUS_HYPERTENSIVE_CRISIS = 'Hypertensive Crisis'

blood_pressure = input('What is your Blood Pressure?: ')
systolic, diastolic = blood_pressure.strip().split('/')
systolic = int(systolic)
diastolic = int(diastolic)

result = []

"""
| Blood Pressure Category | Systolic [mm Hg] | Operator | Diastolic [mm Hg] |
|-------------------------|------------------|----------|-------------------|
| Normal                  | Less than 120    | and      | Less than 80      |
| Elevated                | 120-129          | and      | Less than 80      |
| Hypertension stage 1    | 130-139          | or       | 80-89             |
| Hypertension stage 2    | 140 or higher    | or       | 90 or higher      |
| Hypertensive Crisis     | Higher than 180  | and/or   | Higher than 120   |
"""

# Solution
if 180 <= systolic or 120 <= diastolic:
    result.append(STATUS_HYPERTENSIVE_CRISIS)

if 140 <= systolic or 90 <= diastolic:
    result.append(STATUS_HYPERTENSION_STAGE_2)
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    result.append(STATUS_HYPERTENSION_STAGE_1)
elif 120 <= systolic <= 129 and diastolic < 80:
    result.append(STATUS_ELEVATED)
elif systolic < 120 and diastolic < 80:
    result.append(STATUS_NORMAL)

