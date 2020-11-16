"""
>>> net / PLN
100.0
>>> tax / PLN
23.0
>>> gross / PLN
123.0
"""

PLN = 1
VAT = 23 / 100

net = 100.00 * PLN
tax = net * VAT
gross = net * (1+VAT)
