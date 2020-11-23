"""
* Assignment: Type Float Tax
* Filename: type_float_tax.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min

English:
    1. Cost of the service is 100.00 PLN net
    2. Service has value added tax (VAT) rate of 23%
    3. Calculate tax and gross values
    4. To calculate tax, multiply net times VAT
    5. To calculate gross multiply net times VAT plus 1
    6. Mind the operator precedence
    7. Compare result with "Tests" section (see below)

Polish:
    1. Cena usługi wynosi 100.00 PLN netto
    2. Usługa objęta jest 23% stawką VAT
    3. Oblicz wartości podatku oraz cenę brutto
    4. Aby obliczyć podatek, pomnóż cenę netto razy stawkę VAT
    5. Aby obliczyć cenę brutto pomnóż cenę netto razy stawka VAT plus 1
    6. Zwróć uwagę na kolejność wykonywania działań
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(net)
    <class 'float'>
    >>> type(tax)
    <class 'float'>
    >>> type(gross)
    <class 'float'>
    >>> net / PLN
    100.0
    >>> tax / PLN
    23.0
    >>> gross / PLN
    123.0
"""

# Given
PLN = 1
VAT = 23 / 100

# Solution
net = 100.00 * PLN
tax = net * VAT
gross = net * (1+VAT)
