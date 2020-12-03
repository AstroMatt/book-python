"""
* Assignment: Exception Assert
* Filename: controlflow_exception_assert.py
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Use `assert` keyword
    3. Check if current Python version is greater or equal to `required`
    4. If not, raise exception with message 'Python 3.7+ required'

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj słowa kluczowego `assert`
    3. Sprawdź czy obecna wersja Python jest większa lub równa `required`
    4. Jeżeli nie, podnieś wyjątek z komunikatem 'Python 3.7+ required'

Tests:
    >>> type(sys)
    <class 'module'>
    >>> type(current_version)
    <class 'sys.version_info'>
    >>> type(required)
    <class 'tuple'>
    >>> required
    (3, 7)
"""

# Given
import sys
current_version = sys.version_info
required = (3, 7)

# Solution
assert current_version >= required, 'Python 3.7+ required'
