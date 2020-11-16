"""
>>> round(result/m, 2)
7088.63
"""

m = 1
Pa = 1
hPa = 100 * Pa
ATA = 1013.25 * hPa

o2 = 20.946/100 * ATA
gradient = 11.3 * Pa / m
result = (ATA - o2) / gradient
