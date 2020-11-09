***
ORM
***

QuerySet
========
* sklejanie zapytań
* Tworzenie obiektów
* Zapisywanie ``save()`` ForeignKey

.. code-block:: python

    Model.save()
    Model.objects.all()
    Model.objects.get()
    Model.objects.filter()
    Model.objects.exclude()
    Model.objects.distinct()
    Model.objects.get().sql
    Model.objects.all()[:5]
    Model.objects.all()[5:10]
    Model.objects.order_by('headline')[0]

Filtered QuerySets are unique
-----------------------------
.. code-block:: python

    q1 = Entry.objects.filter(headline__startswith="What")
    q2 = q1.exclude(pub_date__gte=datetime.date.today())
    q3 = q1.filter(pub_date__gte=datetime.date.today())

QuerySets are lazy
------------------
.. code-block:: python

    q = Entry.objects.filter(headline__startswith="What")
    q = q.filter(pub_date__lte=datetime.date.today())
    q = q.exclude(body_text__icontains="food")
    print(q)

Field lookups
=============
.. code-block:: python

    Model.objects.filter(pub_date__lte='1969-07-24')
    Model.objects.get(title__exact='Man walk on Moon!')
    Model.objects.get(title__iexact='man walk on moon!')
    Model.objects.get(headline__contains='Moon')
    Model.objects.filter(title__startswith='Important')
    Model.objects.filter(title__istartswith='Important')
    Model.objects.filter(title__endswith='Important')
    Model.objects.filter(title__iendswith='Important')

Lookups that span relationships
-------------------------------
.. code-block:: python

    Entry.objects.filter(blog__name='Beatles Blog')
    Blog.objects.filter(entry__headline__contains='Lennon')
    Blog.objects.filter(entry__authors__name='Lennon')
    Blog.objects.filter(entry__authors__name__isnull=True)
    Blog.objects.exclude(
        entry__headline__contains='Lennon',
        entry__pub_date__year=2008,
    )
    Blog.objects.exclude(
        entry__in=Entry.objects.filter(
            headline__contains='Lennon',
            pub_date__year=2008,
        ),
    )

Filters can reference fields on the model
=========================================
.. code-block:: python

    from django.db.models import F
    Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
    Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
    Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
    Entry.objects.filter(authors__name=F('blog__name'))

.. code-block:: python

    from datetime import timedelta
    Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))

The pk lookup shortcut
----------------------
.. code-block:: python

    Blog.objects.get(id__exact=14)  # Explicit form
    Blog.objects.get(id=14)         # __exact is implied
    Blog.objects.get(pk=14)         # pk implies id__exact

    # Get blogs entries with id 1, 4 and 7
    Blog.objects.filter(pk__in=[1,4,7])

    # Get all blog entries with id > 14
    Blog.objects.filter(pk__gt=14)

    # pk lookups also work across joins
    Entry.objects.filter(blog__id__exact=3) # Explicit form
    Entry.objects.filter(blog__id=3)        # __exact is implied
    Entry.objects.filter(blog__pk=3)        # __pk implies __id__exact

Complex lookups with Q objects
==============================
.. code-block:: python

    from django.db.models import Q
    Q(question__startswith='What')
    Q(question__startswith='Who') | Q(question__startswith='What')
    # WHERE question LIKE 'Who%' OR question LIKE 'What%'

    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )
    # SELECT * from polls WHERE question LIKE 'Who%'
    # AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')

Comparing objects
=================
.. code-block:: python

    some_entry == other_entry
    some_entry.id == other_entry.id

    some_obj == other_obj
    some_obj.name == other_obj.name

``Q()`` expressions
===================
.. code-block:: python

    from django.db.models import Q


    Q(question__startswith='What')

    Q(question__startswith='Who') | Q(question__startswith='What')
    Q(question__startswith='Who') | ~Q(pub_date__year=2005)     # negated query

.. code-block:: python

    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )

``F()`` expressions
===================
An F() object represents the value of a model field or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.

.. code-block:: python

    Iris.objects.all().update(petal_length=F('petal_length') + 1)

Aggregations
============
.. literalinclude:: src/django-orm-cheatsheet.py
    :language: python
    :name: listing-django-orm-cheatsheet
    :caption: Django ORM Cheat sheet

