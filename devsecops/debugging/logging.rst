*******
Logging
*******


Logging levels
==============
* Critical - Critical Error, and cannot continue
* Error - Error, but can continue
* Warning - Warning, will do something important
* Info - I will do something
* Debug - This is how I am doing this

.. code-block:: python

    import logging

    logging.critical('Permission Denied, cannot continue')
    logging.error('File not found, will create a new one')
    logging.warning('Warning, will overwrite the file')
    logging.info('Writing to file')
    logging.debug('Data {DATA} will be written to file {path}')


Use Case
========
.. code-block:: python

    import logging


    print('Program start')

    for number in range(0,3):
        print(f'Current number: {number}')

    print('Program end')

    # Program start
    # Current number: 0
    # Current number: 1
    # Current number: 2
    # Program end

.. code-block:: python

    import logging


    logging.warning('Program start')

    for number in range(0,3):
        logging.debug(f'Current number: {number}')

    logging.warning('Program end')

    # WARNING:root:Program start
    # WARNING:root:Program end

Konfiguracja logowania
----------------------

.. code-block:: python

    import logging

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    log.warning('warning!')  # zostanie zapisana do pliku
    log.debug('wiadomosc debuggingowa')  # nie zostanie zapisana, bo level jest INFO, czyli powyżej DEBUG

.. code-block:: python

    import logging

    logging.basicConfig(
        level=logging.INFO,
        filename='/tmp/logging.csv',
        format='"%(asctime).19s", "%(levelname)s", "%(message)s"'
    )

    log = logging.getLogger(__name__)

    log.warning('warning!')  # zostanie zapisana do pliku
    log.debug('wiadomosc debuggingowa')  # nie zostanie zapisana, bo level jest INFO, czyli powyżej DEBUG


.. code-block:: python

    import logging


    logging.basicConfig(
        level=logging.DEBUG,
        format='"%(asctime).19s", "%(levelname)s", "%(message)s"',
        filename="log.csv",
    )

    logging.info('Rozpoczynam pętlę')

    i = 0
    while i <= 3:
        logging.info(f'Przetwarzam {i}')
        i += 1

    logging.info('Skończyłem pętlę')

.. code-block:: python

    import logging

    logging.basicConfig(
        level=logging.INFO,
        filename='/tmp/logging.csv',
        format='"%(asctime).19s", "%(levelname)s", "%(message)s"'
    )

    log = logging.getLogger(__name__)

    log.warning('warning!')  # zostanie zapisana do pliku
    log.debug('wiadomosc debuggingowa')  # nie zostanie zapisana, bo level jest INFO, czyli powyżej DEBUG

.. code-block:: python

    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='"%Y-%m-%d" "%H:%M:%S"',
        format='{asctime}, "{levelname}", "{message}"',
        style='{'
    )

Logowanie zdarzeń
-----------------
.. code-block:: python

    import logging
    log = logging.getLogger(__name__)

    def sum(a, b):
        log.debug('Function `sum()` executed with: %s', locals())
        value = a + b
        log.debug(f'Will produce "{value}" as result')
        return value

    sum(1, 2)
    # Function `sum()` executed with: {'b': 2, 'a': 1}
    # Will produce "3" as result
    # 3

Wyciszanie logowania
--------------------
.. code-block:: python

    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime).19s] [%(levelname)s] %(message)s')

    logging.getLogger('requests').setLevel(logging.WARNING)
    log = logging.getLogger(__name__)

    log.debug('to jest moja debugowa wiadomosc')


Konfiguracja formatowania logów
===============================
.. todo:: convert table to CSV

+-------------------------+-----------------------------------------------+
| Format                  | Description                                   |
+=========================+===============================================+
| args                    | The tuple of arguments merged into ``msg`` to |
|                         | produce ``message``, or a dict whose values   |
|                         | are used for the merge (when there is only one|
|                         | argument, and it is a dictionary).            |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(asctime)s``         | Human-readable time when the                  |
|                         | `LogRecord` was created.  By default          |
|                         | this is of the form '2003-07-08 16:49:45,896' |
|                         | (the numbers after the comma are millisecond  |
|                         | portion of the time).                         |
+-------------------------+-----------------------------------------------+
| ``%(created)f``         | Time when the `LogRecord` was created         |
|                         | (as returned by `time.time`).                 |
+-------------------------+-----------------------------------------------+
| exc_info                | Exception tuple (à la ``sys.exc_info``) or,   |
|                         | if no exception has occurred, ``None``.       |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(filename)s``        | Filename portion of ``pathname``.             |
+-------------------------+-----------------------------------------------+
| ``%(funcName)s``        | Name of function containing the logging call. |
+-------------------------+-----------------------------------------------+
| ``%(levelname)s``       | Text logging level for the message            |
|                         | (``'DEBUG'``, ``'INFO'``, ``'WARNING'``,      |
|                         | ``'ERROR'``, ``'CRITICAL'``).                 |
+-------------------------+-----------------------------------------------+
| ``%(levelno)s``         | Numeric logging level for the message         |
|                         | (`DEBUG`, `INFO`,                             |
|                         | `WARNING`, `ERROR`,                           |
|                         | `CRITICAL`).                                  |
+-------------------------+-----------------------------------------------+
| ``%(lineno)d``          | Source line number where the logging call was |
|                         | issued (if available).                        |
+-------------------------+-----------------------------------------------+
| ``%(module)s``          | Module (name portion of ``filename``).        |
+-------------------------+-----------------------------------------------+
| ``%(msecs)d``           | Millisecond portion of the time when the      |
|                         | `LogRecord` was created.                      |
+-------------------------+-----------------------------------------------+
| ``%(message)s``         | The logged message, computed as ``msg %       |
|                         | args``. This is set when                      |
|                         | `Formatter.format` is invoked.                |
+-------------------------+-----------------------------------------------+
| msg                     | The format string passed in the original      |
|                         | logging call. Merged with ``args`` to         |
|                         | produce ``message``, or an arbitrary object   |
|                         | (see `arbitrary-object-messages`).            |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(name)s``            | Name of the logger used to log the call.      |
+-------------------------+-----------------------------------------------+
| ``%(pathname)s``        | Full pathname of the source file where the    |
|                         | logging call was issued (if available).       |
+-------------------------+-----------------------------------------------+
| ``%(process)d``         | Process ID (if available).                    |
+-------------------------+-----------------------------------------------+
| ``%(processName)s``     | Process name (if available).                  |
+-------------------------+-----------------------------------------------+
| ``%(relativeCreated)d`` | Time in milliseconds when the LogRecord was   |
|                         | created, relative to the time the logging     |
|                         | module was loaded.                            |
+-------------------------+-----------------------------------------------+
| stack_info              | Stack frame information (where available)     |
|                         | from the bottom of the stack in the current   |
|                         | thread, up to and including the stack frame   |
|                         | of the logging call which resulted in the     |
|                         | creation of this record.                      |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(thread)d``          | Thread ID (if available).                     |
+-------------------------+-----------------------------------------------+
| ``%(threadName)s``      | Thread name (if available).                   |
+-------------------------+-----------------------------------------------+

``DictConfig``
--------------
.. code-block:: python

    {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': True
            },
            'django.request': {
                'handlers': ['default'],
                'level': 'WARN',
                'propagate': False
            },
        }
    }

.. csv-table:: DictConfig
    :header-rows: 1

    "Format", "Description"
    "filename", "Specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler"
    "filemode", "If filename is specified, open the file in this mode. Defaults to 'a'"
    "format", "Use the specified format string for the handler"
    "datefmt", "Use the specified date/time format, as accepted by time.strftime()"
    "style", "If format is specified, use this style for the format string. One of '%', '{' or '$' for printf-style, str.format() or string.Template respectively. Defaults to '%'"
    "level", "Set the root logger level to the specified level"
    "stream", "Use the specified stream to initialize the StreamHandler. Note that this argument is incompatible with filename - if both are present, a ValueError is raised"
    "handlers", "If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don’t already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with filename or stream - if both are present, a ValueError is raised"


Rotate
======
* ``logging.handlers.WatchedFileHandler``
* ``logging.handlers.RotatingFileHandler``
* ``logging.handlers.TimedRotatingFileHandler``

.. code-block:: python

    from logging import handlers

    handler = handlers.TimedRotatingFileHandler(filename, when=LOG_ROTATE)

    handler.setFormatter(logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S'))

    #LOG_ROTATE = midnight
    #set your log format

Examples
========
.. code-block:: python

    import logging
    import os

    logging.basicConfig(
        format='"{asctime}", "{levelname}", "{message}"',
        filename='...',
        style='{'
    )

    log = logging.getLogger(__name__)
    level = os.getenv('LOG_LEVEL', 'INFO')
    log.setLevel(level)


    log.critical('Błąd krytyczny')
    log.error('Błąd')
    log.warning('Uwaga')
    log.info('Informacja')
    log.debug('Wiadomość debugowa')


    logging.getLogger('requests').setLevel('DEBUG')
    logging.getLogger('_tmp').setLevel('ERROR')


.. code-block:: python
    :caption: Decorators

    from datetime import datetime
    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='%Y-%m-%d %H:%M:%S',
        format='[{levelname}] {message}',
        style='{'
    )


    def timeit(func):
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            result = func(*args, **kwargs)
            time_end = datetime.now()
            time = time_end - time_start
            logging.debug(f'Time: {time}')
            return result

        return wrapper


    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            logging.debug(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            logging.debug(f'Result: {result}')
            return result

        return wrapper


    @timeit
    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # [DEBUG] Calling: function='add_numbers', args=(1, 2), kwargs={}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000105

    add_numbers(1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(1,), kwargs={'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000042

    add_numbers(a=1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(), kwargs={'a': 1, 'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000040


Further Reading
===============
* https://pyvideo.org/pycon-au-2018/a-guided-tour-of-python-logging.html
