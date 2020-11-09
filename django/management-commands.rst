*******************
Management Commands
*******************

Built-in
========
.. code-block:: text

    [auth]
        changepassword
        createsuperuser

    [contenttypes]
        remove_stale_contenttypes

    [dashboard]
        customdashboard

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

    [sessions]
        clearsessions

    [staticfiles]
        collectstatic
        findstatic
        runserver

Writing own management commands
===============================

Structure
---------
.. code-block:: text

    app
        management
        __init__.py
            commands
            __init__.py
            my_command.py

Minimal command boilerplate code
--------------------------------
.. code-block:: python

    from django.core.management.base import BaseCommand


    class Command(BaseCommand):
        help = 'What my command does?'

        def handle(self, *args, **options):
            pass

Cleaning data in database
-------------------------
.. code-block:: python

    from django.core.management.base import BaseCommand
    from addressbook.models import Person


    class Command(BaseCommand):
        help = 'Clean data in database'

        def handle(self, *args, **options):
            for p in Person.objects.all():
                p.firstname = p.firstname.title()
                p.lastname = p.lastname.title()
                p.save()

Parse file line by line
-----------------------
.. code-block:: python

    from django.core.management.base import BaseCommand
    from addressbook.models import Person


    class Command(BaseCommand):
        help = 'Moj tekst pomocy'

        def add_arguments(self, parser):
            parser.add_argument(
                '--file',
                dest='file',
                nargs='?',
                help='Log File',
            )

            parser.add_argument(
                '--format',
                nargs='?',
                dest='format',
                help='Log File Format',
            )

        def parse_line(self, line, format):
            if format == 'text':
                return line.upper()

        def handle(self, *args, **options):
            filename = options['file']
            format = options['format']
            content = []

            with open(filename, encoding='utf-8') as file:
                for line in file:
                    line = self.parse_line(line, format)
                    content.append(line)

            print('\n'.join(content))

Use cases
---------
.. literalinclude:: src/django-management-commands.py
    :language: python
    :caption: Writing own management commands
