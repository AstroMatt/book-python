"""

Type Int Sub
------------
* Last update: 2020-11-22
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    3. For calculation use round number -273 (0K = -273°C)
    4. How many Celsius degrees has average temperatures at surface [MSLREMS]_:
        a. Lunar day: 453 K
        b. Lunar night: 93 K
    5. Compare result with "Tests" section (see below)

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    3. W zadaniu przyjmij równe -273°C (0K = -273°C)
    4. Ile stopni Celsiusza wynoszą średnie temperatury powierzchni [MSLREMS]_:
        a. Księżyca w dzień: 453 K
        b. Księżyca w nocy: 93 K
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> moon_day
    180
    >>> moon_night
    -180

"""

# Solution
K = -273

moon_day = 453 + K
moon_night = 93 + K
