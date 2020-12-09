.. _Files Append:

***********
File Append
***********


Rationale
=========
* Appends data at the end of file
* Creates file if not exists
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* ``mode`` parameter to ``open()`` function is required
* ``.writelines()`` does not add a line separator!!


Appending to File
=================
* Append to the end of file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = 'We choose to go to the Moon...'

    with open(FILE, mode='a') as file:
        file.write(DATA)
