from datetime import date

from django.db import IntegrityError
from django.test import TestCase
from .models import Person


class PersonTest(TestCase):

    def test_create_person(self):
        p = Person.objects.create(firstname='Jan', lastname='Twardowski')
        self.assertEqual(p.firstname, 'Jan')
        self.assertEqual(p.lastname, 'Twardowski')

    def test_is_adult(self):
        p1 = Person.objects.create(
            firstname='First',
            lastname='Twardowski',
            date_of_birth=date(2018, 12, 6))
        self.assertFalse(p1.is_adult())

        # p2 = Person.objects.create(
        #     firstname='Second',
        #     lastname='Twardowski',
        #     date_of_birth=date(2000, 12, 5))
        # self.assertTrue(p2.is_adult())
        #
        # p3 = Person.objects.create(
        #     firstname='Third',
        #     lastname='Twardowski',
        #     date_of_birth=date(2000, 12, 6))
        # self.assertTrue(p3.is_adult())
        #
        # p4 = Person.objects.create(
        #     firstname='Fourth',
        #     lastname='Twardowski',
        #     date_of_birth=date(2000, 12, 7))
        # self.assertFalse(p3.is_adult())

    def test_create_invalid_person(self):
        with self.assertRaises(IntegrityError):
            p1 = Person.objects.create(firstname='F1', lastname='L1')
            p2 = Person.objects.create(firstname='F1', lastname='L1')

    def test_connection(self):
        self.client.get('...')
