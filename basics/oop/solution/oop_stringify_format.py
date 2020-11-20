"""
>>> result = Distance(meters=1337)
>>> format(result, 'km')
'1.337'
>>> format(result, 'cm')
'133700'
>>> format(result, 'm')
'1337'
"""

class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __format__(self, unit):
        if unit in ('cm', 'centimeter', 'centimeters'):
            result = self.meters * 100
        elif unit in ('m', 'meter', 'meters'):
            result = self.meters
        elif unit in ('km', 'kilometer', 'kilometers'):
            result = self.meters / 1000
        return str(result)
