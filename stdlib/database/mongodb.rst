****************
Database MongoDB
****************

* http://api.mongodb.com/python/current/tutorial.html


Install
=======
.. code-block:: console

    $ pip install pymongo


Insert data
===========
.. code-block:: python

    from datetime import datetime, timezone
    from pymongo import MongoClient

    DATA = {
        "name": "José Jiménez",
        "catchphrase": "My name... José Jiménez",
        "tags": ["astronaut", "nasa", "space"],
        "date": datetime.now(tz=timezone.utc)
    }


    client = MongoClient('mongodb://example.com:27017/')
    db = client.test_database
    astronauts = db.astronauts

    obj = astronauts.insert_one(DATA)
    obj.inserted_id
    # ObjectId('...')

Select data
===========

Select all records
------------------
.. code-block:: python

    for astro in astronauts.find():
        print(astro)

Filter records
--------------
.. code-block:: python

    for astro in astronauts.find({"name": "José Jiménez"}):
        print(astro)
