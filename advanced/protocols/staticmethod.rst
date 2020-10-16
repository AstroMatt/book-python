.. _Protocol Staticmethod:

************
Staticmethod
************


Rationale
=========
* Should **not** be in a class: method which don't use ``self`` in its body
* Should be in class: if method takes ``self`` and use it (it requires instances to work)
* If a method don't use ``self`` but uses class as a namespace use ``@staticmethod`` decorator
* Using class as namespace
* No need to create a class instance
* Will not pass instance (``self``) as a first method argument

.. code-block:: python

    class MyClass:

        @staticmethod
        def mymethod():
            pass


     MyClass.mymethod()


Example
=======
.. code-block:: python
    :caption: Functions on a high level of a module lack namespace

    def echo(name):


    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b


    add(1, 2)
    sub(8, 4)

.. code-block:: python
    :caption: When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get instance (``self``) as a first argument. Instantiating Calculator is not needed, as of functions do not read or write to instance variables.

    class Calculator:

        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b


    Calculator.add(10, 20)
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() missing 1 required positional argument: 'b'

    Calculator.sub(8, 4)
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() missing 1 required positional argument: 'b'

    calc = Calculator()
    calc.add(1, 2)
    # 3
    calc.sub(8, 4)
    # 4

.. code-block:: python
    :caption: Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove instance (``self``) argument to method.

    class Calculator:

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def sub(a, b):
            return a - b


    Calculator.add(1, 2)
    Calculator.sub(8, 4)


Use Cases
=========

Http Client
-----------
.. code-block:: python

    class http:

        @staticmethod
        def get(url):
            ...

        @staticmethod
        def post(url, data):
            ...

    http.get('https://python.astrotech.io')
    http.post('https://python.astrotech.io', data={'astronaut': 'Mark Watney'})

Astronaut Hello
---------------
.. code-block:: python

    def astronaut_say_hello():
        print('hello')

    def astronaut_say_goodbye():
        print('goodbye')


    class Astronaut:
        pass


    a = Astronaut()
    astronaut_say_hello()
    # hello
    astronaut_say_goodbye()
    # 'goodbye'

.. code-block:: python

    class Astronaut:
        def say_hello(self):
            print('hello')

        def say_goodbye(self):
            print('goodbye')


    a = Astronaut()
    a.say_hello()
    # hello
    a.say_goodbye()
    # 'goodbye'

    Astronaut.say_hello()
    # Traceback (most recent call last):
    #     ...
    # TypeError: say_hello() missing 1 required positional argument: 'self'

    Astronaut.say_goodbye()
    # Traceback (most recent call last):
    #     ...
    # TypeError: say_goodbye() missing 1 required positional argument: 'self'

.. code-block:: python

    class Astronaut:

        @staticmethod
        def say_hello():
            print('hello')

        @staticmethod
        def say_goodbye():
            print('goodbye')


    Astronaut.say_hello()
    # hello

    Astronaut.say_goodbye()
    # 'goodbye'

    astro = Astronaut()
    astro.say_hello()
    # hello
    astro.say_goodbye()
    # goodbye

Helper
------
.. code-block:: python
    :caption: `HabitatOS <https://www.habitatos.space>`_ Z-Wave sensor model

    from datetime import datetime, timezone
    from decimal import Decimal, InvalidOperation
    import logging

    from django.db import models
    from django.utils.translation import ugettext_lazy as _

    from habitat._common.models import HabitatModel
    from habitat._common.models import MissionDateTime
    from habitat.time import MissionTime

    log = logging.getLogger('habitat.sensor')


    def clean_unit(unit: str) -> str:
        try:
            return {
                'C': 'celsius',
                'F': 'fahrenheit',
                'dB': 'decibel',
                'lux': 'lux',
                '%': 'percent',
            }[unit]
        except KeyError:
            return None


    def clean_type(type: str) -> str:
        return type.lower().replace(' ', '-')


    def clean_value(value: str) -> Decimal:
        try:
            return Decimal(value)
        except InvalidOperation:
            return Decimal(0)


    def clean_device(device: str) -> str:
        return device


    def clean_datetime(dt: str) -> datetime:
        try:
            return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f+00:00').replace(tzinfo=timezone.utc)
        except ValueError:
            return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')


    class ZWaveSensor(HabitatModel, MissionDateTime):
        TYPE_BATTERY_LEVEL = 'battery-level'
        TYPE_POWER_LEVEL = 'powerlevel'
        TYPE_TEMPERATURE = 'temperature'
        TYPE_LUMINANCE = 'luminance'
        TYPE_RELATIVE_HUMIDITY = 'relative-humidity'
        TYPE_ULTRAVIOLET = 'ultraviolet'
        TYPE_BURGLAR = 'burglar'
        TYPE_CHOICES = [
            (TYPE_BATTERY_LEVEL, _('Battery Level')),
            (TYPE_POWER_LEVEL, _('Power Level')),
            (TYPE_TEMPERATURE, _('Temperature')),
            (TYPE_LUMINANCE, _('Luminance')),
            (TYPE_RELATIVE_HUMIDITY, _('Relative Humidity')),
            (TYPE_ULTRAVIOLET, _('Ultraviolet')),
            (TYPE_BURGLAR, _('Burglar'))]

        UNIT_CELSIUS = 'celsius'
        UNIT_KELVIN = 'kelvin'
        UNIT_FAHRENHEIT = 'fahrenheit'
        UNIT_DECIBEL = 'decibel'
        UNIT_LUMINANCE = 'lux'
        UNIT_PERCENT = 'percent'
        UNIT_DIMENSIONLESS = None
        UNIT_CHOICES = [
            (UNIT_DIMENSIONLESS, _('n/a')),
            (UNIT_PERCENT, _('%')),
            (UNIT_LUMINANCE, _('Lux')),
            (UNIT_DECIBEL, _('dB')),
            (UNIT_CELSIUS, _('°C')),
            (UNIT_KELVIN, _('K')),
            (UNIT_FAHRENHEIT, _('°F'))]

        DEVICE_ATRIUM = 'c1344062-2'
        DEVICE_ANALYTIC_LAB = 'c1344062-3'
        DEVICE_OPERATIONS = 'c1344062-4'
        DEVICE_TOILET = 'c1344062-5'
        DEVICE_DORMITORY = 'c1344062-6'
        DEVICE_STORAGE = 'c1344062-7'
        DEVICE_KITCHEN = 'c1344062-8'
        DEVICE_BIOLAB = 'c1344062-9'
        DEVICE_AIRLOCK = None
        DEVICE_CHOICES = [
            (DEVICE_ATRIUM, _('Atrium')),
            (DEVICE_ANALYTIC_LAB, _('Analytic Lab')),
            (DEVICE_OPERATIONS, _('Operations')),
            (DEVICE_TOILET, _('Toilet')),
            (DEVICE_DORMITORY, _('Dormitory')),
            (DEVICE_STORAGE, _('Storage')),
            (DEVICE_KITCHEN, _('Kitchen')),
            (DEVICE_BIOLAB, _('Biolab'))]

        datetime = models.DateTimeField(verbose_name=_('Datetime [UTC]'), db_index=True)
        device = models.CharField(verbose_name=_('Sensor Location'), max_length=30, choices=DEVICE_CHOICES, db_index=True)
        type = models.CharField(verbose_name=_('Type'), max_length=30, choices=TYPE_CHOICES)
        value = models.DecimalField(verbose_name=_('Value'), max_digits=7, decimal_places=2, default=None)
        unit = models.CharField(verbose_name=_('Unit'), max_length=15, choices=UNIT_CHOICES, null=True, blank=True, default=None)

        def __str__(self) -> str:
            return f'[{self.date} {self.time}] (device: {self.device}) {self.type}: {self.value} {self.unit}'

        class Meta:
            verbose_name = _('Data')
            verbose_name_plural = _('Zwave Sensors')

        @staticmethod
        def add(datetime: str, device: str, type: str, value: str, unit: str):
            dt = clean_datetime(datetime)
            time = MissionTime().get_time_dict(from_datetime=dt)

            return ZWaveSensor.objects.update_or_create(
                datetime=dt,
                defaults={
                    'date': time['date'],
                    'time': time['time'],
                    'device': clean_device(device),
                    'type': clean_type(type),
                    'value': clean_value(value),
                    'unit': clean_unit(unit),
                }
            )

.. code-block:: python

    ZWaveSensor.add(datetime, device, type, value, unit)


Assignments
===========
.. todo:: Create assignments
