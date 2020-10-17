*************
Regexp Syntax
*************


Rationale
=========
* Regular Expressions are also known as ``regexp``, ``regex`` or ``re``
* Identifiers - what to find
* Qualifiers - range to find
* Quantifiers - how many occurrences of preceding qualifier or identifier

* Recall information about raw strings ``r'...'``
* Recall information about escape characters, i.e.:

    * ``\n`` - newline,
    * ``\\n`` - string of characters with ``\`` and then ``n``
    * ``.`` - in regexp means any character
    * ``\.`` - just a dot
    * ``*`` - in regexp means any times
    * ``\*`` - just asterisk character


Identifiers
===========
* What to find

* ``\s`` - whitespace (space, tab, newline)
* ``\S`` - anything but whitespace
* ``\d`` - digit
* ``\D`` - anything but digit
* ``\b`` - whitespace around words
* ``\B`` - anything but whitespace around words
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...)
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)

* ``\t`` - tab
* ``\n`` - newline
* ``\v`` - vertical space
* ``\f`` - form feed


Qualifier
=========
* Range to find

* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`
* ``[abc]`` - letter `a` or `b` or `c`
* ``a|b`` - letter `a` or `b` (also works with expressions)
* ``[a-z]|[0-9]`` - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`

* ``.`` - any character besides newline
* ``^`` - start of a string
* ``$`` - end of a string

Examples:

    * ``[d-m]`` - dowolna mała litera z przedziału: d-m
    * ``[3-7]`` - dowolna cyfra z przedziału 3-7
    * ``[d-mK-P3-8]`` - dowolna mała litera z przedziału d-m oraz dowolna duża litera K-P oraz dowolna cyfra 3-8
    * ``[xz2]`` - x lub z lub 2
    * ``d|x`` - d lub x
    * ``[d-k]|[ABC]|[3-8]`` - dowolna mała litera d-k lub duża A,B,C lub cyfra 3-8
    * ``[A-Z][a-z]+`` - jedna duża litera, a później mała minimum raz


Quantifier
==========
* How many occurrences of preceding qualifier or identifier

Greedy (prefer longest matches):

    * ``{n}`` - exactly `n` times
    * ``{,n}`` - maximum `n` times
    * ``{n,}`` - minimum `n` times
    * ``{n,m}`` - minimum `n` times, maximum `m` times
    * ``*`` - minimum 0 times, no maximum
    * ``+`` - minimum 1 time, no maximum
    * ``?`` - minimum 0 times, maximum 1 time (could be)

Non-Greedy (prefer shortest matches):

    * ``{,n}?`` - maximum `n` times, but prefer shorter
    * ``{n,}?`` - minimum `n` times, but prefer shorter
    * ``{n,m}?`` - minimum `n` times, maximum `m` times, but prefer shorter
    * ``*?`` - minimum 0 times, no maximum, but prefer shorter
    * ``+?`` - minimum 1 time, no maximum, but prefer shorter
    * ``??`` - minimum 0 times, maximum 1 time (could be), but prefer shorter


Examples:

    * ``[0-9]{2}`` - exactly two digits from `0` to `9`
    * ``\d{2}`` - exactly two digits from `0` to `9`
    * ``[A-Z]{2,10}`` - duża litera A-Z minimalnie 2, maksymalnie 10
    * ``[A-Z]{2-10}-[0-9]{,5}`` - duża litera A-Z minimalnie 2, maksymalnie 10 później myślnik `-` później maksymalnie 5 cyfr
    * ``[a-z]+`` - minimalnie jedna litera, ale staraj się dopasowywać jak najwięcej liter
    * ``\d+`` - liczba
    * ``\d+\.\d+`` - ułamek dziesiętny


Negation
========
* Logically inverts qualifier
* ``[^abc]`` - anything but letter `a` or `b` or `c`


Groups
======
* Catch expression results
* Can be named or positional
* można się odwoływać pozycyjnie oraz keyword

* ``()`` - group

Define:

    * ``(...)`` - grupa nie nazwana
    * ``(?P<name>...)`` - grupa nazwana `name`

Backreference:

    * ``\1`` - odwołaj się pozycyjnie do pierwszej grupy
    * ``$1`` - odwołaj się pozycyjnie do pierwszej grupy (niektóre języki programowania)
    * ``(?P=name)`` - odwołaj się do grupy nazwanej ``name``

Examples:

    * ``(\w+)`` - słowa lub całe cyfry
    * ``\d+(\.\d+)?`` - liczba z częścią ułamka dziesiętnego lub bez
    * ``\d+(,\d+)?`` - liczba wraz z separatorem tysięcznym (US) - czyli przecinek ``,``
    * ``(?P<word>\w+)`` - grupa nazwana `word` składająca się z ``\w+`` (dowolny unicode minimum raz)

.. code-block:: python

    DATA = 'Mark Watney'
    result = re.search(r'(?P<firstname>\w+) (?P<lastname>\w+)', DATA)

    result.groupdict()
    # {'firstname': 'Mark', 'lastname': 'Watney'}


Flags
=====
* ``re.IGNORECASE`` - bez względu na wielkość liter
* ``re.MULTILINE`` - wyrażenie może zacząć się w jednej linii i skończyć w innej; zmienia znaczenie: ``^`` - początek linii, ``$`` - koniec linii
* ``re.DOTALL`` - ``.`` również łapie końce linii


Extensions
==========
* In other programming languages

* ``[:allnum:]`` == ``[a-zA-Z0-9]``
* ``[:alpha:]`` == ``[a-zA-Z]``
* ``[a-Z]`` == ``[a-zA-Z]``
* ``[a-9]`` == ``[a-zA-Z0-9]``







Matching
========
* ``\`` - Escapes special characters (allows matching ``*``, ``?``, etc)

.. csv-table:: Regular Expression Pattern Matching
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``[a-z]``", "One small letter form ``a`` to ``z``"
    "``[A-Z]``", "One capital letter form ``A`` to ``Z``"
    "``[0-9]``", "One digit from ``0`` to ``9``"
    "``[a-zA-Z0-9]``", "One of the following: small or capital letter or digit"
    "``[abc]``", "One of the following: ``a``, ``b`` or ``c``"
    "``A|B``", "One of either A or B patterns"


Negation
========
.. csv-table:: Regular Expression Pattern Negation
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``[^abc]``", "None of the following: ``a``, ``b`` or ``c``"
    "``^(?!.*word).*$``", "Not containing ``word``"


Unicode
=======
* ``\w`` - Includes most characters that can be part of a word in any language, as well as numbers and the underscore

.. csv-table:: Regular Expression Patterns
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``\w``", "Unicode word character"
    "``\d``", "Unicode decimal digit ``[0-9]``, and many other digit characters"
    "``\s``", "Unicode whitespace characters ``[\t\n\r\f\v]`` and non-breaking spaces"


Qualifiers
==========
.. csv-table:: Regular Expression Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``.``", "Any character except a newline"
    "``^``", "Start of the string"
    "``$``", "End of the string"
    "``*``", "Zero or more repetitions of the preceding pattern (as many as possible)"
    "``+``", "One or more repetitions of the preceding pattern"
    "``?``", "Zero or one repetitions of the preceding pattern"


Quantifiers
===========
.. csv-table:: Regular Expression Quantifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``{m}``", "Exactly ``m`` copies of the previous RE should be matched"
    "``{m,}``", "At least ``m`` repetitions"
    "``{,n}``", "At most ``n`` repetitions"
    "``{m,n}``", "Match from ``m`` to ``n`` repetitions of the preceding RE (as many as possible)"
    "``{m,n}?``", "Match from ``m`` to ``n`` repetitions of the preceding RE (as few as possible)"


Non-Greedy
==========
* Adding ``?`` after the qualifier makes it non-greedy
* Non-greedy - as few as possible
* Greedy - as many as possible

.. csv-table:: Regular Expression Greedy and Non-Greedy Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``?``", "zero or one (greedy)"
    "``*``", "zero or more (greedy)"
    "``+``", "one or more (greedy)"
    "``??``", "zero or one (non greedy)"
    "``*?``", "zero or more (non greedy)"
    "``+?``", "one or more (non greedy)"


Flags
=====
.. csv-table:: Regular Expression Flags
    :widths: 15, 85
    :header: "Flag", "Description"

    "``re.IGNORECASE``", "Case-insensitive (Unicode support i.e. Ü and ü)"
    "``re.MULTILINE``",  "``^`` matches beginning of the string and each line"
    "``re.MULTILINE``",  "``$`` matches end of the string and each line"
    "``re.DOTALL``",     "``.`` matches newlines"


Multiline
=========
* ``re.MULTILINE`` - Flag turns on Multiline search
* ``^`` - Matches the start of the string, and immediately after each newline
* ``$`` - Matches the end of the string or just before the newline at the end of the string also matches before a newline


Groups
======
* ``(?P<name>...)``- Define named group
* ``(?P=name)``- Backreferencing by group name
* ``\number`` - Backreferencing by group number

.. csv-table:: Regular Expression Groups
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``(...)``", "Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group"
    "``(?P<name>...)``", "substring matched by the group is accessible via the symbolic group name name"
    "``(?P=name)``", "A backreference to a named group"
    "``\number``", "Matches the contents of the group of the same number"

Example:

    * ``(?P<tag><.*?>)text(?P=tag)``
    * ``(?P<tag><.*?>)text\1``
    * ``(.+) \1`` matches ``the the`` or ``55 55``
    * ``(.+) \1`` not matches ``thethe`` (note the space after the group)


.. code-block:: python

    import string

    string.punctuation
    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    string.whitespace
    # ' \t\n\r\x0b\x0c'

    string.ascii_lowercase
    # 'abcdefghijklmnopqrstuvwxyz'

    string.ascii_uppercase
    # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    string.ascii_letters
    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    string.digits
    # '0123456789'

    string.hexdigits
    # '0123456789abcdefABCDEF'

    string.octdigits
    # '01234567'

    string.printable
    # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

Examples
========
* ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``


Visualization
=============
* https://regexper.com/
* https://regex101.com/

.. figure:: img/regexp-vizualization.png
    :width: 75%
    :align: center

    Visualization for pattern ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``
