*************
Regexp Groups
*************


About
=====
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


Examples
========
.. code-block:: python
    :caption: Usage of group in ``re.match()``

    import re

    PATTERN = r'(?P<firstname>\w+) (?P<lastname>\w+)'
    TEXT = 'Jan Twardowski'

    matches = re.match(PATTERN, TEXT)

    matches.group('firstname')     # 'Jan'
    matches.group('lastname')      # 'Twardowski'
    matches.group(1)                # 'Jan'
    matches.group(2)                # 'Twardowski'
    matches.groups()                # ('Jan', 'Twardowski')
    matches.groupdict()             # {'firstname': 'Jan', 'lastname': 'Twardowski'}
