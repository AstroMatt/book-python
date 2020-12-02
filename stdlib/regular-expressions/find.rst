************************
Regexp Findall, Finditer
************************


About
=====
* ``re.findall()``
* ``re.finditer()``


Examples
========
.. code-block:: python
    :caption: Usage of ``re.findall()`` and ``re.finditer()``

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    DATA = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, DATA)
    # ['MYPROJ-1337', 'MYPROJ-997']

.. code-block:: python
    :caption: Finding All Adverbs

    import re


    TEXT = 'He was carefully disguised but captured quickly by police.'
    ADVERBS = r'\w+ly'

    re.findall(ADVERBS, TEXT)
    # ['carefully', 'quickly']


Assignments
===========

Regexp Find Dates
-----------------
* Assignment: Regexp Find Dates
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 8 min
* Filename: :download:`solution/regexp_find_dates.py`
* References: :cite:`RegexpWikipediaApollo11`

English:
    #. Use data from "Given" section (see below)
    #. Using regular expressions find dates in US format (example: "April 12, 1961")
    #. Print all dates
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Używając wyrażeń regularnych wyszukaj dat w formacie US (przykład: "April 12, 1961")
    #. Wyświetl wszystkie daty
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    ['October 4, 1957',
     'April 12, 1961',
     'May 5, 1961',
     'May 25, 1961',
     'September 12, 1962',
     'September 12, 1962']
