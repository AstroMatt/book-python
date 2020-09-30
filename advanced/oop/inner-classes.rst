*************
Inner Classes
*************


.. code-block:: python

    class User:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def find_in_database(self):
            if not in DATABASE:
                raise User.DoesNotExist

        class DoesNotExist(Exception):
            pass


    try:
        user = User('Mark', 'Watney')
        user.find_in_database()
    except User.DoesNotExists:
        print('User does not exist')

.. code-block:: python

    class Person(models.Model):
        firstname = ...
        lastname = ...

        class Meta:
            ordering = ['lastname']


Assignments
===========
.. todo:: Create assignments
