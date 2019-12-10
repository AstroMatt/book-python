.. _Stdlib Exam:

***********
Stdlib Exam
***********


Relational Files Database
=========================
* Complexity level: medium
* Lines of code to write: 100-150 lines
* Estimated time of completion: 60 min
* Filename: :download:`solution/exam.py`

:English:
    #. Save listings content to files:

        - ``etc_passwd.txt`` - :numref:`code-exam-etc-passwd`
        - ``etc_shadow.txt`` - :numref:`code-exam-etc-shadow`
        - ``etc_group.txt`` - :numref:`code-exam-etc-group`

    #. Copy also comments and empty lines
    #. Parse files and convert it to ``OUTPUT: List[dict]``
    #. Return list of users with ``UID`` greater than 1000
    #. User dict should contains data collected from all files

:Polish:
    #. Zapisz treści listingów do plików:

        - ``etc_passwd.txt`` - :numref:`code-exam-etc-passwd`
        - ``etc_shadow.txt`` - :numref:`code-exam-etc-shadow`
        - ``etc_group.txt`` - :numref:`code-exam-etc-group`

    #. Skopiuj również komentarze i puste linie
    #. Sparsuj plik i przedstaw go w formacie ``OUTPUT: List[dict]``
    #. Zwróć listę użytkowników, których ``UID`` jest większy niż 1000
    #. Dict użytkownika powinien zawierać dane z wszystkich plików

:Input:
    .. literalinclude:: data/etc-passwd.txt
        :name: code-exam-etc-passwd
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/passwd``

    .. literalinclude:: data/etc-shadow.txt
        :name: code-exam-etc-shadow
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/shadow``

    .. literalinclude:: data/etc-group.txt
        :name: code-exam-etc-group
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/group``

:Output:
    .. code-block:: python

        OUTPUT: List[dict] = [
            {
                'username': 'twardowski',
                'uid': 1001,
                'gid': 1001,
                'home': '/home/twardowski',
                'shell': '/bin/bash',
                'algorithm': 'SHA-512',
                'password': 'tgfvvFWJJ5...k4kijuhE50',
                'salt': 'P9zn0KwR',
                'groups': {'astronauts', 'sysadmin'},
                'last_changed': datetime.date(2015, 7, 16),
                'locked': False,
            },
            ...
        ]

:The whys and wherefores:
    * :ref:`Basic Conditionals`
    * :ref:`Basic Files`
    * :ref:`Basic Sequences`
    * :ref:`Basic Comprehensions`
    * :ref:`Loop For`
    * :ref:`Str methods`
