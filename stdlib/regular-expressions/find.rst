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
* Assignment name: Regexp Find Dates
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/regexp_find_dates.py`
* Last update: 2020-10-01
* References: :cite:`RegexpWikipediaApollo11`

:English:
    #. Use data from "Input" section (see below)
    #. Using regular expressions find dates in US format (example: "April 12, 1961")
    #. Print all dates
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Używając wyrażeń regularnych wyszukaj dat w formacie US (przykład: "April 12, 1961")
    #. Wyświetl wszystkie daty
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        ['October 4, 1957',
         'April 12, 1961',
         'May 5, 1961',
         'May 25, 1961',
         'September 12, 1962',
         'September 12, 1962']
