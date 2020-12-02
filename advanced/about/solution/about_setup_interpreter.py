"""
* Assignment: About Setup Interpreter
* Filename: about_setup_interpreter.py
* Complexity: easy
* Lines of code: 0 lines
* Estimated time: 3 min

English:
    1. In your directory create file `about_interpreter.py`
    2. If question about adding file to GIT repository pops-up, mark checkbox "Always add" and click "Yes"
    3. Use code from "Given" section (see below)
    4. Run code in your IDE (right click on code -> "Run File in Python Console")
    5. What Python version is installed?
    6. Compare result with "Tests" section (see below)
    7. Write result (version number) in shared spreadsheet
    8. Write `100%` in shared spreadsheet at assignment row

Polish:
    1. W swoim katalogu stwórz plik `about_interpreter.py`
    2. Jeżeli wyskoczy pytanie czy dodać plik do repozytorium GIT, zaznacz checkbox "Always add" i wybierz "Yes"
    3. Użyj kodu z sekcji "Given" (patrz poniżej)
    4. Uruchom kod swoim IDE (prawy klawisz myszy na kodzie -> "Run File in Python Console")
    5. Jaka wersja Python jest zainstalowana?
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    7. Zapisz rezultat (numer wersji) we współdzielonym arkuszu kalkulacyjnym
    8. Zapisz `100%` we współdzielonym arkuszu kalkulacyjnym w wierszu zadania

Tests:
    >>> import sys
    >>> sys.version_info > (3, 7, 0)
    True
"""

# Given
import sys
print(sys.version[:6])


# Solution
import sys
print(sys.version[:6])
