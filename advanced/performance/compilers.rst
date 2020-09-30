**************************
Compilers and Interpreters
**************************


Sam Python jest tak naprawdę tylko specyfikacją składni oraz wyglądu biblioteki standardowej. Python ma obecnie kilka interpreterów z których najbardziej popularny jest cPython, który jest wydawany razem z nową wersją specyfikacji języka.


Interpreters
============

cPython
-------
Domyślną wersją Pythona jest cPython. Jest to tzw. implementacja wzorcowa i to jej kompilator jest wydawany wraz ze specyfikacją nowych funkcjonalności przy każdym wydaniu Python. Sam kompilator jest rozwijany w języku C. cPython jest najbardziej popularną dystrybucją z wszystkich wydań. W poniższych materiałach to właśnie z tej wersji będziemy korzystać.

Cython
------
* Cython is a compiled language that generates CPython extension modules
* Cython is a superset of the Python programming language
* Designed to give C-like performance with code that is written mostly in Python
* These extension modules can then be loaded and used by regular Python code using the import statement

PyPy
----
Bardzo ciekawy projekt napisania interpretera Pythona w... Pythonie. Kompilator dokonuje bardzo wielu niskopoziomowych optymalizacji dlatego ta wersja języka jest wyjątkowo szybka. Niestety nie wszystkie biblioteki zewnętrzne są z nią kompatybilne. Nie mniej projekt jest wciąż aktywnie rozwijany przez bardzo pomysłowych programistów i stanowi solidną alternatywę dla cPythona. Niektóre programy przy wykorzystaniu PyPy potrafią przyspieszyć kilkuset do kilkutysiąc krotnie.

IronPython
----------
Próba implementacji języka Python wykorzystując platformę .NET firmy Microsoft. Dzięki temu język bardzo dobrze integruje się z całym środowiskiem.

Jython
------
Próba implementacji języka Python wykorzystując platformę wirtualnej maszyny JAVA (JVM). Projekt bardzo obiecujący lecz niestety ostatnio słabo rozwijany. JVM stanowi bardzo dobrą platformę dobrze "wygrzaną" oraz poznaną pod względem wydajnościowym jak i środowiska developerskiego.

Micropython
-----------
* IoT

Inne
----
W internecie jest dostępnych jeszcze więcej implementacji języka. Niektóre projekty są jeszcze rozwijane, niektóre (Stackless Python) weszły w skład lub transformowały się w wyżej wymienionych lub zostały zarzucone (Unleaden Swallow).


Compiling
=========
* https://py2app.readthedocs.io/
* http://www.py2exe.org/
* http://www.pyinstaller.org/

Assignments
===========
.. todo:: Create assignments
