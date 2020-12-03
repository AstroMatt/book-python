.. _OOP Enum:

********
OOP Enum
********


Rationale
=========
* List of finite choices
* Enumerations
* ``Enum``
* ``IntEnum``
* ``Flag``
* ``IntFlag``


Definition
==========
.. code-block:: python
    :caption: Defining ``enum``

    from enum import Enum


    class Color(Enum):
        RED = '#00FF00'
        GREEN = '#00FF00'
        BLUE = '#0000FF'


    color = Color.RED

.. code-block:: python
    :caption: Defining ``enum``

    from enum import Enum

    class Status(Enum):
        ALIVE = 'alive'
        DEAD = 'dead'


Accessing names and values
==========================
.. code-block:: python
    :caption: Accessing names and values

    from enum import Enum

    class Color(Enum):
        RED = '#FF0000'
        GREEN = '#00FF00'
        BLUE = '#0000FF'


    print(Color.RED)        # Color.RED
    print(Color.RED.name)   # RED
    print(Color.RED.value)  # '#FF0000'

.. code-block:: python

    from enum import Enum


    class Status(Enum):
        FULL_HEALTH = 100
        DEAD = 0


    hit_points = 100
    status = Status(hit_points)
    print(status)
    # Status.FULL_HEALTH


    hit_points = 0
    status = Status(hit_points)
    print(status)
    # Status.DEAD


Iterating over ``Enum``
=======================
.. code-block:: python
    :caption: Iterating over ``Enum``

    from enum import Enum

    class Color(Enum):
        RED = '#00FF00'
        GREEN = '#00FF00'
        BLUE = '#0000FF'

    for color in Color:
        print(color)

    # Color.RED
    # Color.GREEN
    # Color.BLUE


Identity check
==============
.. code-block:: python
    :caption: Identity check

    color = Color('#00FF00')     # <Color.GREEN: '#00FF00'>
    color is Color.RED           # False
    color is Color.GREEN         # True



Use cases
=========
* https://docs.python.org/3/library/os.html#os.stat

.. code-block:: python
    :caption: ``enum`` - Example usage

    from enum import Enum

    class Permission(Enum):
        READ_WRITE_EXECUTE = 0b111
        READ_WRITE = 0b110
        READ_EXECUTE = 0b101
        READ = 0b100
        WRITE_EXECUTE = 0b011
        WRITE = 0b010
        EXECUTE = 0b001
        NONE = 0b000

.. code-block:: python

    import os
    from enum import Enum

    class Permission(Enum):
        READ_WRITE_EXECUTE = 0b111
        READ_WRITE = 0b110
        READ_EXECUTE = 0b101
        READ = 0b100
        WRITE_EXECUTE = 0b011
        WRITE = 0b010
        EXECUTE = 0b001
        NONE = 0b000


    os.stat('/tmp/myfile.txt')
    # os.stat_result(
    #   st_mode=33260,
    #   st_ino=44792722,
    #   st_dev=16777222,
    #   st_nlink=1,
    #   st_uid=501,
    #   st_gid=0,
    #   st_size=2930,
    #   st_atime=1587481434,
    #   st_mtime=1587481422,
    #   st_ctime=1587484635)

    permissions = os.stat('/tmp/myfile.txt').st_mode

    print(f'dec={permissions}, oct={oct(permissions)}, bin={bin(permissions)}')
    # dec=33260, oct=0o100754, bin=0b1000000111101100

    *_, user, group, others = oct(permissions)

    print(f'{user=} {group=} {others=}')
    # user='7' group='5' others='4'

    Permission(int(user))
    # <Permission.READ_WRITE_EXECUTE: 7>

    Permission(int(group))
    # <Permission.READ_EXECUTE: 5>

    Permission(int(others))
    # <Permission.READ: 4>

.. code-block:: python
    :caption: ``enum`` - Example usage

    from enum import IntEnum

    class IndexDrives(IntEnum):
        """ This enum holds the index value of drive object entries
        """
        ControlWord = 0x6040
        StatusWord = 0x6041
        OperationMode = 0x6060


Pattern Matching
================
.. versionadded:: Python 3.10
    :pep:`636` -- Structural Pattern Matching: Tutorial

.. code-block:: python
    :force:

    request = 'GET 1.1 /index.html'

    match request.split():
        case ['GET', version, uri]:
            server.get(uri)
        case ['POST', version, uri]:
            server.post(uri)
        case ['PUT', version, uri]:
            server.put(uri)
        case ['DELETE', version, uri]:
            server.delete(uri)

.. code-block:: python
    :force:

    def http_error(status):
        match status:
            case 400:
                return 'Bad request'
            case 401 | 403 | 404:
                return 'Not allowed'
            case 404:
                return 'Not found'
            case 418:
                return "I'm a teapot"
            case _:
                return 'Unexpected status'

.. code-block:: python
    :force:

    match hero.action():
        case ['move', ('up'|'down'|'left'|'right') as direction, value]:
            hero.move(direction, value)
        case ['make_damage', value]:
            hero.make_damage(value)
        case ['take_damage', value]:
            hero.take_damage(value)

.. code-block:: python
    :force:

    from enum import Enum

    class Key(Enum):
        ESC = 27
        ARROW_LEFT = 37
        ARROW_UP = 38
        ARROW_RIGHT = 39
        ARROW_DOWN = 40

    match keyboard.on_key_press():
        case Key.ESC:
            game.quit()
        case Key.ARROW_LEFT:
            game.move_left()
        case Key.ARROW_UP:
            game.move_up()
        case Key.ARROW_RIGHT:
            game.move_right()
        case Key.ARROW_DOWN:
            game.move_down()
        case _:
            raise ValueError(f'Unrecognized key')

.. code-block:: python
    :force:

    from enum import Enum

    class Color(Enum):
        RED = 0
        BLUE = 1
        BLACK = 2

    match color:
        case Color.RED:
            print('Soviet')
        case Color.BLUE:
            print('Allies')
        case Color.BLACK:
            print('Axis')

.. code-block:: python
    :force:

    from enum import Enum

    class SpaceMan(Enum):
        NASA = 'Astronaut'
        ESA = 'Astronaut'
        ROSCOSMOS = 'Cosmonaut'
        CNSA = 'Taikonaut'
        ISRO = 'GaganYatri'

    match agency:
        case SpaceMan.NASA:
            print('USA')
        case SpaceMan.ESA:
            print('Europe')
        case SpaceMan.ROSCOSMOS:
            print('Russia')
        case SpaceMan.CNSA:
            print('China')
        case SpaceMan.ISRO:
            print('India')


Assignments
===========
.. todo:: Create assignments
