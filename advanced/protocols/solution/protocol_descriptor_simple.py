"""
* Assignment: Protocol Descriptor Simple
* Filename: protocol_descriptor_simple.py
* Complexity: easy
* Lines of code: 9 lines
* Estimated time: 13 min

English:
    1. Define class `Temperature`
    2. Class stores values in Kelvins using descriptor
    3. Temperature must always be positive
    4. Use descriptors to check boundaries at each value modification
    5. All tests must pass
    6. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę `Temperature`
    2. Klasa przetrzymuje wartości jako Kelwiny używając deskryptora
    3. Temperatura musi być zawsze być dodatnia
    4. Użyj deskryptorów do sprawdzania wartości granicznych przy każdej modyfikacji
    5. Wszystkie testy muszą przejść
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> class Temperature:
    ...     kelvin = Kelvin()

    >>> t = Temperature()
    >>> t.kelvin = 1
    >>> t.kelvin
    1
    >>> t.kelvin = -1
    Traceback (most recent call last):
    ValueError: Negative temperature
"""


# Solution
class Kelvin:
    def __get__(self, parent, parent_type):
        return parent._value

    def __set__(self, parent, new_value):
        if new_value < 0:
            raise ValueError('Negative temperature')
        else:
            parent._value = new_value


