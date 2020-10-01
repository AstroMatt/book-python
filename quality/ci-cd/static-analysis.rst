********************
Static Code Analysis
********************


``SonarLint``
=============
* https://www.sonarlint.org
* Plugin do IDE


``SonarScanner``
================


``SonarQube``
=============
SonarQube software (previously called Sonar) is an open source quality management platform, dedicated to continuously analyze and measure technical quality, from project portfolio to method.

:More information:
    * https://sonarqube.com
    * http://docs.sonarqube.org/display/SONAR/Documentation
    * https://sonarqube.com/dashboard/index?did=143
    * https://sonarqube.com/governance?id=662857


Przygotowanie środowiska statycznej analizy
===========================================
Uruchomienie:

    .. code-block:: console

        $ cd PROJECT_DIRECTORY
        $ docker run --rm -d --name sonarqube -p 9000:9000 -v $(pwd):/src sonarqube
        $ docker exec -u 0 -it sonarqube bash

            curl -sL https://deb.nodesource.com/setup_8.x -o /opt/node.sh
            bash /opt/node.sh
            apt install -y nodejs
            wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip -O /opt/sonar-scanner.zip
            unzip -d /opt/ /opt/sonar-scanner.zip
            ln -s /opt/sonar-scanner-*/bin/sonar-scanner /usr/bin/sonar-scanner
            VERSION=$(cd /src/ && hg log -l 1 --template '{node}\n')

            apt install -y python-pip pylint python-coverage python-nose
            pip install -r /src/requirements.txt

Konfiguracja:

    #. Quality Profile -> Python
    #. Skopiuj profil "Sonar way" i nazwij nowy jako "PyLint"
    #. Trybik (prawy górny róg) -> Activate more rules
    #. Przefiltruj listę (lewy dolny róg) po "Repository" równym "PyLint"
    #. Bulk Change (góra ekrany) -> Activate in "PyLint" -> zaakceptuj
    #. Ustaw "PyLint jako domyślny"
    #. Uruchom analizę

.. warning:: Po uruchomieniu ``SonarQube`` z obrazu ``Docker`` instalacja pluginów, a następnie restart ``SonarQube`` niszczy możliwość przeprowadzania analizy

#. Administration -> Marketplace

    * Zainstalować plugin HTML

Python
------
.. literalinclude:: src/sonar-python.properties
    :language: properties
    :caption: SonarScanner config for static analysis of Python code

CSS
---
.. literalinclude:: src/sonar-css.properties
    :language: properties
    :caption: SonarScanner config for static analysis of CSS code

JavaScript
----------
.. literalinclude:: src/sonar-javascript.properties
    :language: properties
    :caption: SonarScanner config for static analysis of JavaScript code

Multi-language
--------------
.. literalinclude:: src/sonar-multilanguage.properties
    :language: properties
    :caption: SonarScanner config for static analysis of Multilanguage code




``Coverage``
------------

:About:
    Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

:Install:
    .. code-block:: console

        $ pip install coverage

:Usage:
    .. code-block:: console

        $ coverage run FILE.py
        $ coverage report -m
        $ nosetests --with-coverage --cover-erase --cover-xml --cover-inclusive --with-xunit --xunit-file=xunit.xml --cover-xml-file=coverage.xml

    Use coverage run to run your program and gather data:

    .. code-block:: console

        $ coverage run myprogram.py arg1 arg2
        blah blah ..your program's output.. blah blah

    Use coverage report to report on the results:

    .. code-block:: console

        $ coverage report -m
        Name                      Stmts   Miss  Cover   Missing
        -------------------------------------------------------
        myprogram.py                 20      4    80%   33-35, 39
        mymodule.py                  56      6    89%   17-23
        -------------------------------------------------------
        TOTAL                        76     10    87%

    For a nicer presentation, use ``coverage html`` to get annotated HTML listings detailing missed lines:

    .. code-block:: console

        $ coverage html


:More information:
    * https://pypi.python.org/pypi/coverage
    * https://coverage.readthedocs.io/


``pylama``
----------
.. code-block:: console

    $ pylama --linters pylint --skip='*/migrations/*' --abspath /src

.. literalinclude:: src/pylama.ini
    :language: ini
    :caption: setup.cfg

``bandit``
----------
* Sprawdzanie kodu pod kątem podatności bezpieczeństwa

.. code-block:: console

    $ pip install bandit
    $ bandit --recursive /src/

``pycodestyle``
---------------
.. code-block:: console

    $ pip install pycodestyle
    $ pycodestyle --max-line-length=79 --exclude=*/migrations/* .

``safety``
----------
.. code-block:: console

    $ pip install safety
    $ safety check -r /src/requirements.txt


