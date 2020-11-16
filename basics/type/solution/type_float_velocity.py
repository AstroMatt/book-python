"""
>>> round(result / KPH, 2)
120.7
"""

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

M = 1
KM = 1000 * M
MI = 1609.344 * M

KPH = KM / HOUR
MPH = MI / HOUR

result = 75 * MPH
