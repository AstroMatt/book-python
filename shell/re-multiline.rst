****************
Regexp Multiline
****************

About
=====
* ``re.MULTILINE`` - Flag turns on Multiline search
* ``^`` - Matches the start of the string, and immediately after each newline
* ``$`` - Matches the end of the string or just before the newline at the end of the string also matches before a newline

.. csv-table:: Regular Expression Flags
    :widths: 15, 85
    :header: "Flag", "Description"

    "``re.IGNORECASE``", "Case-insensitive (Unicode support i.e. Ü and ü)"
    "``re.MULTILINE``",  "``^`` matches beginning of the string and each line"
    "``re.MULTILINE``",  "``$`` matches end of the string and each line"
    "``re.DOTALL``",     "``.`` matches newlines"


Examples
========
.. code-block:: python
    :caption: Usage of regexp

    import re


    PATTERN = r'^[A-Z]{2,10}-[0-9]{1,6}'
    TEXT = """
    MYPROJ-1337 MYPROJ-31337 Fixed inspectdb crash;
    MYPROJ-997 Remove commented out code
    """

    re.findall(PATTERN, TEXT)
    # []

    re.findall(PATTERN, TEXT, flags=re.MULTILINE)
    # ['MYPROJ-1337', 'MYPROJ-997']

.. code-block:: python
    :caption: Usage of regexp

    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    TEXT = """
    MYPROJ-1337 MYPROJ-31337 Fixed inspectdb crash;
    MYPROJ-997 Remove commented out code
    """

    re.findall(PATTERN, TEXT)
    # ['MYPROJ-1337', 'MYPROJ-31337', 'MYPROJ-997']

    re.findall(PATTERN, TEXT, flags=re.MULTILINE)
    ['MYPROJ-1337', 'MYPROJ-31337', 'MYPROJ-997']
