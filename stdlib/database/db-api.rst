************
Database API
************

Rationale
=========
* DB API v2

.. code-block:: python

    sqlite3.connect(...) -> connection

    connection.execute(...) -> result
    connection.executemany(...) -> list[result]
    connection.fetchmany(...) -> list[result]
    connection.fetchone(...) -> result
    connection.cursor(...) -> cursor
