*************
i18n and l10n
*************

Timezone
========
* django.utils.timezone
* from django.conf.locale.en import formats as en_formats

.. code-block:: python

    en_formats.DATETIME_FORMAT = 'Y-m-d H:i'
    en_formats.DATE_FORMAT = 'Y-m-d'
    en_formats.TIME_FORMAT = 'H:i'
    USE_TZ = True
    TIME_ZONE = 'UTC'


Gettext
=======
* ``.po`` files
* ``.mo`` files
* Using ``gettext`` in code
* Generating translation files
* Compiling translation files
* Updating translation files
* Transifex (``tx push`` and ``tx pull``)


i18n - internationalization
===========================
* ``django-admin makemessages -l en``
* ``django-admin compilemessages``
* ``{% blocktranslate %}`` and ``{% endblocktranslate %}``
* ``{% translate %}``
* ``from django.utils.translation import gettext_lazy as _``
* transifex-client
* gettext
* poedit

.. code-block:: python

    # Internationalization
    # https://docs.djangoproject.com/en/dev/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    USE_I18N = True
    USE_L10N = True

.. code-block:: console

    $ cd botnet/heartbeat
    $ mkdir locale

    $ django-admin makemessages -l en
    processing locale en

    $ django-admin makemessages -l pl
    processing locale pl

    $ django-admin compilemessages
    processing file django.po in /private/tmp/botnet/botnet/heartbeat/locale/en/LC_MESSAGES
    processing file django.po in /private/tmp/botnet/botnet/heartbeat/locale/pl/LC_MESSAGES
