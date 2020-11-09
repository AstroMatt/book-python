*****
Views
*****

Class Based Views
=================

Generic Views
=============
* ``DetailView``
* ``EditView``
* ``ListView``

TemplateView
------------
.. literalinclude:: src/django-views-generic-templateview.py
    :language: python
    :caption: TemplateView


RedirectView
------------
.. literalinclude:: src/django-views-generic-redirectview.py
    :language: python
    :caption: RedirectView

View
----
.. literalinclude:: src/django-views-generic-view.py
    :language: python
    :caption: View

Responses
=========
* ``HttpResponse``
* ``JsonResponse``


Permissions in Views
====================

Class Based Views
-----------------
* https://docs.djangoproject.com/en/2.1/topics/auth/default/#the-permissionrequiredmixin-mixin

.. code-block:: python

    from django.contrib.auth.mixins import PermissionRequiredMixin

    class MyView(PermissionRequiredMixin, View):
        permission_required = 'polls.can_vote'
        # Or multiple of permissions:
        permission_required = ('polls.can_open', 'polls.can_edit')

Decorators
----------
* ``@login_required``
