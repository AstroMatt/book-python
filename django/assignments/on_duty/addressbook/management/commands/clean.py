from django.core.management.base import BaseCommand
from addressbook.models import Person


class Command(BaseCommand):
    help = 'My help text'

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

    def handle(self, *args, **options):
        filename = options['file']
        format = options['format']
        content = []

        with open(filename) as file:
            for line in file:
                line = self.parse_line(line)
                content.append(line)

        print('\n'.join(content))
        return

        for p in Person.objects.all():
            p.firstname = p.firstname.title()
            p.lastname = p.lastname.title()
            p.save()

    def parse_line(self, line):
        return line.upper()
