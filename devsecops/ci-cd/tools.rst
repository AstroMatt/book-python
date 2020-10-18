.. _cicd-tools:

***********
CI/CD Tools
***********

* https://pre-commit.com/

Static Analysis
===============
.. csv-table:: Static Analysis
    :header: "Tool", "Description"

    "``pylama``", ""
    "``pylint``", ""
    "``pyflakes``", ""
    "``flake8``", ""
    "``SonarQube``", ""
    "``SonarScanner``", ""
    "``SonarLint``", ""


Security
========
.. csv-table:: Security
    :header: "Tool", "Description"

    "``safety``", ""
    "``bandit``", ""


Distributing and Packaging
==========================
.. csv-table:: Distributing and Packaging
    :header: "Tool", "Description"

    "``pipenv``", "Frozen env"
    "``venv``", ""


Code Style and Practices
========================
.. csv-table:: Code Style and Practices
    :header: "Tool", "Description"

    "``pycodestyle``", ""
    "``pydocestyle``", ""
    "``eradicate``", "Remove commented code"
    "``isort``", ""
    "``cloc``", "Count Lines of Code"


Code complexity and Coverage
============================
.. csv-table:: Code complexity and Coverage
    :header: "Tool", "Description"

    "``mccabe``", ""
    "``radon``", ""
    "``coverage``", ""


Testing
=======
.. csv-table:: Testing
    :header: "Tool", "Description"

    "``doctest``", ""
    "``unittest``", ""
    "``selenium``", ""
    "``behave``", ""
    "``mutpy``", ""
    "``tox``", ""
    "``pytest``", ""


Type Checking
=============
.. csv-table:: Type Checking
    :header: "Tool", "Description"

    "``mypy``", ""
    "``pyre-check``", ""
    "``pytype``", ""
    "``monkeytype``", ""
    "``pyannotate``", ""


Database Schema Migration
=========================
.. csv-table:: Database Schema Migration
    :header: "Tool", "Description"

    "``SQLAlchemy``", ""
    "``django.migrations``", ""
    "``Liquibase``", ""
    "``FlywayDB``", ""


Running
=======
.. code-block:: python

    import os
    import subprocess
    import logging
    from config import APPS, STDOUT_DIRECTORY, PROJECT_DIRECTORY


    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime).19s] %(levelname)s\t %(message)s')

    # pip install pylama
    # pip install radon
    # pip install bandit
    # pip install pycodestyle
    # pip install eradicate
    # pip install mccabe
    # pip install pyflakes
    # pip install pylint
    # pip install isort
    # pip install pydocstyle
    #
    # ## setup.cfg
    #
    # [pylama:pycodestyle]
    # max_line_length = 300


    COMMANDS = [
        {'name': 'bandit',      'timeout': 180, 'command': 'bandit --recursive {directory}'},
        {'name': 'cloc',        'timeout': 180, 'command': 'cloc --fullpath --not-match-d="(migrations|tinymce|jquery)" {directory}'},
        {'name': 'pycodestyle', 'timeout': 180, 'command': 'pylama --format parsable --linters pycodestyle --skip="*/migrations/*" {directory}'},
        {'name': 'eradicate',   'timeout': 180, 'command': 'pylama --format parsable --linters eradicate --skip="*/migrations/*" {directory}'},
        {'name': 'mccabe',      'timeout': 180, 'command': 'pylama --format parsable --linters mccabe --skip="*/migrations/*" {directory}'},
        {'name': 'radon',       'timeout': 180, 'command': 'pylama --format parsable --linters radon --skip="*/migrations/*" {directory}'},
        {'name': 'pyflakes',    'timeout': 180, 'command': 'pylama --format parsable --linters pyflakes --skip="*/migrations/*" {directory}'},
        {'name': 'isort',       'timeout': 180, 'command': 'pylama --format parsable --linters isort --skip="*/migrations/*" {directory}'},
        {'name': 'pydocstyle',  'timeout': 180, 'command': 'pylama --format parsable --linters pydocstyle --skip="*/migrations/*" --ignore=D100,D101,D102,D103,D104,D105,D106,D107,D200,D205,D212,D400,D404 {directory}'},
        {'name': 'pylint',      'timeout': 180, 'command': 'pylama --format parsable --linters pylint --skip="*/migrations/*" {directory}'},
    ]


    os.chdir(PROJECT_DIRECTORY)


    for app_name in APPS:
        logging.warning('Processing: "{}"'.format(app_name))
        stdout_dir = os.path.join(STDOUT_DIRECTORY, app_name)
        os.makedirs(stdout_dir, exist_ok=True)

        for command in COMMANDS:
            linter = command['name']
            cmd = command['command'].format(directory=app_name)
            header = '``{}``'.format(linter)
            underscore = '-' * len(header)
            stdout_file = os.path.join(stdout_dir, linter+'.txt')
            logging.info(cmd)

            try:
                result = subprocess.run(
                    cmd,
                    shell=True,
                    timeout=command['timeout'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding='utf-8')
            except subprocess.TimeoutExpired:
                logging.error('Timeout exceeded')
                continue

            if result.stderr:
                logging.debug(result.stderr)

            with open(stdout_file, mode='w') as file:
                file.write(result.stdout)


    HEADER = """

    Static Analysis
    ===============
    """

    REPORT = """
    .. code-block:: console
        :caption: Running static analysis ``{linter}`` for module ``{app}``

        {command}

    .. literalinclude:: /_stdout/{app}/{linter}.txt
        :caption: Result of static analysis ``{linter}`` for module ``{app}``
        :language: text
    """

    for app_name in APPS:
        logging.warning('Adding reports: "{}"'.format(app_name))
        report_file = os.path.join(STDOUT_DIRECTORY, '..', 'code-review', app_name + '.rst')

        with open(report_file, mode='a') as file:
            file.write(HEADER)
            file.write('\n')

        for command in COMMANDS:
            linter = command['name']
            cmd = command['command'].format(directory=app_name)
            header = '``{}``'.format(linter)
            underscore = '-' * len(header)

            with open(report_file, mode='a') as file:
                file.write(header)
                file.write('\n')
                file.write(underscore)
                file.write('\n')
                file.write(REPORT.format(linter=linter, command=cmd, app=app_name))
                file.write('\n')
