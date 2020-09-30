.. _Database SQL:

************
Database SQL
************


ACID
====
* Atomicity
* Consistency
* Isolation
* Durability

Atomicity
---------
Transactions are often composed of multiple statements. Atomicity guarantees that each transaction is treated as a single "unit", which either succeeds completely, or fails completely: if any of the statements constituting a transaction fails to complete, the entire transaction fails and the database is left unchanged. An atomic system must guarantee atomicity in each and every situation, including power failures, errors and crashes.

Consistency
-----------
Consistency ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants: any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof. This prevents database corruption by an illegal transaction, but does not guarantee that a transaction is correct.

Isolation
---------
Transactions are often executed concurrently (e.g., reading and writing to multiple tables at the same time). Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially. Isolation is the main goal of concurrency control; depending on the method used, the effects of an incomplete transaction might not even be visible to other transactions.

Durability
----------
Durability guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure (e.g., power outage or crash). This usually means that completed transactions (or their effects) are recorded in non-volatile memory.


CREATE
======
.. literalinclude:: src/sql-create.sql
    :language: sql
    :caption: CREATE

INSERT
======
.. literalinclude:: src/sql-insert.sql
    :language: sql
    :caption: INSERT

AUTOINCREMENT
=============
.. literalinclude:: src/sql-autoincrement.sql
    :language: sql
    :caption: Auto Increment

COMMIT and ROLLBACK
===================
.. literalinclude:: src/sql-commit-rollback.sql
    :language: sql
    :caption: COMMIT and ROLLBACK

SELECT
======
.. literalinclude:: src/sql-select.sql
    :language: sql
    :caption: SELECT

UPDATE
======
.. literalinclude:: src/sql-update.sql
    :language: sql
    :caption: UPDATE

GROUP BY
========
.. literalinclude:: src/sql-group.sql
    :language: sql
    :caption: GROUP BY

HAVING
======
.. literalinclude:: src/sql-having.sql
    :language: sql
    :caption: HAVING

ALTER
=====
* write your statement starting with ``--``
* after you're sure, remove comments

.. literalinclude:: src/sql-alter.sql
    :language: sql
    :caption: ALTER

DROP
====
* https://www.youtube.com/watch?v=1aEqd4bl6Bs
* write your statement starting with ``--``
* after you're sure, remove comments

.. literalinclude:: src/sql-drop.sql
    :language: sql
    :caption: DROP

DELETE
======
* write your statement starting with ``--``
* after you're sure, remove comments

.. literalinclude:: src/sql-delete.sql
    :language: sql
    :caption: DELETE

JOIN
====
.. figure:: img/sql-joins.png
    :width: 75%
    :align: center

    Joins

INNER JOIN
----------
.. figure:: img/sql-innerjoin.gif
    :align: center
    :width: 75%

.. literalinclude:: src/sql-join-inner.sql
    :language: sql
    :caption: INNER JOIN

LEFT JOIN
---------
.. figure:: img/sql-leftjoin.gif
    :align: center
    :width: 75%

.. literalinclude:: src/sql-join-left.sql
    :language: sql
    :caption: LEFT JOIN

RIGHT JOIN
----------
.. figure:: img/sql-rightjoin.gif
    :align: center
    :width: 75%

.. literalinclude:: src/sql-join-right.sql
    :language: sql
    :caption: RIGHT JOIN

FULL OUTER JOIN
---------------
.. figure:: img/sql-fulljoin.gif
    :align: center
    :width: 75%

.. literalinclude:: src/sql-join-outer.sql
    :language: sql
    :caption: FULL OUTER JOIN

SELF JOIN
---------
.. literalinclude:: src/sql-join-self.sql
    :language: sql
    :caption: SELF JOIN

TRUNCATE
========
.. literalinclude:: src/sql-truncate.sql
    :language: sql
    :caption: TRUNCATE


Assignments
===========

Database SQL Relations
----------------------
* Complexity level: medium
* Lines of code to write: 0 lines
* Estimated time of completion: 13 min
* Solution: TODO
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. How to write input data in one table without using relations?
    #. There are at least four methods
    #. Discuss pros and cons of each method
    #. Which methods is ACID compliant?

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Jak zapisać w jednej tabeli bez wykorzystania relacji?
    #. Są przynajmniej cztery metody
    #. Przeprowadź dyskusję na temat zalet i wad każdej metody
    #. Która metody jest zgodna z ACID?

:Input:
    .. code-block:: text

        José, Jiménez
            2101 E NASA Pkwy, 77058, Houston, Texas, USA
            , Kennedy Space Center, 32899, Florida, USA

        Mark, Watney
            4800 Oak Grove Dr, 91109, Pasadena, California, USA
            2825 E Ave P, 93550, Palmdale, California, USA

        Иван, Иванович
            Kosmodrom Bajkonur, Bajkonur, Kazachstan

        Melissa Lewis,
            <NO ADDRESS>

        Alex Vogel
            Linder Hoehe, 51147, Köln, Germany
