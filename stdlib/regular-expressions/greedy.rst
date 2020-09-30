*****************
Regexp Non-Greedy
*****************


About
=====
* Adding ``?`` after the qualifier makes it non-greedy
* Non-greedy - as few as possible
* Greedy - as many as possible

.. csv-table:: Regular Expression Greedy and Non-Greedy Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``?``", "zero or one (greedy)"
    "``*``", "zero or more (greedy)"
    "``+``", "one or more (greedy)"
    "``??``", "zero or one (non greedy)"
    "``*?``", "zero or more (non greedy)"
    "``+?``", "one or more (non greedy)"


Examples
========
.. code-block:: python
    :caption: Usage of greedy and non-greedy search in ``re.findall()``

    import re

    TEXT = '<strong>Ehlo World</strong>'

    re.findall(r'<.*>', TEXT)         # ['<strong>Ehlo World</strong>']
    re.findall(r'<.*?>', TEXT)        # ['<strong>', '</strong>']

.. code-block:: python
    :caption: Usage of greedy and non-greedy search with groups

    re.findall(r'<(.*)>', TEXT)       # ['strong>Ehlo World</strong']
    re.findall(r'<(.*?)>', TEXT)      # ['strong', '/strong']
    re.findall(r'</?(.*?)>', TEXT)    # ['strong', 'strong']


Assignments
===========

Regexp Greedy Moon Speech
-------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/regexp_greedy_moon_speech.py`
* Last update: 2020-10-01
* References: "Moon Speech" by John F. Kennedy at Rice Stadium, Houston, TX on 1962-09-12 :cite:`RegexpKennedy1962`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``re.findall()`` and non-greedy qualifier split text by paragraphs
    #. Print paragraph starting with "We choose to go to the moon"

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``re.findall()`` i non-greedy qualifier podziel tekst na paragrafy
    #. Wyświetl paragraf zaczynający się od słów "We choose to go to the moon"

:Input:
    .. code-block:: python

        DATA = """<html><body> <bgsound src="jfktalk.wav" loop="2"><p></p><center><h3>John F. Kennedy Moon Speech - Rice Stadium</h3><img src="jfkrice.jpg"><h3>September 12, 1962</h3></center><p></p><hr><p></p><center>Movie clips of JFK speaking at Rice University: <a href="JFKatRice.mov">(.mov)</a> or <a href="jfkrice.avi">(.avi)</a> (833K)</center><p><a href="jfkru56k.asf">See and hear</a> the entire speech for 56K modem download [8.7 megabytes in a .asf movie format which requires Windows Media Player 7 (speech lasts about 33 minutes)].<br><a href="jfkru100.asf">See and hear</a> the entire speech for higher speed access [25.3 megabytes in .asf movie format which requires Windows Media Player 7].<br><a href="jfkslide.asf">See and hear</a> a five minute audio version of the speech with accompanying slides and music. This is a most inspirational presentation of, perhaps, the most famous space speech ever given. The file is a streaming video Windows Media Player 7 format. [11 megabytes in .asf movie format which requires Windows Media Player 7]. <br><a href="jfk_rice_speech.mpg">See and hear</a> the 17 minute 48 second speech in the .mpg format. This is a very large file of 189 megabytes and only suggested for those with DSL, ASDL, or cable modem access as the download time on a 28.8K or 56K modem would be many hours duration.</p><p></p><hr><p></p><center><h4>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h4></center><p>President Pitzer, Mr. Vice President, Governor, CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, Mr.Bell, scientists, distinguished guests, and ladies and gentlemen:</p><p>We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills,because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win,and the others, too.</p><p>It is for these reasons that I regard the decision last year to shift our efforts in space from low to high gear as among the most important decisions that will be made during my incumbency in the office of the Presidency.</p><p>In the last 24 hours we have seen facilities now being created for the greatest and most complex exploration in man's history.We have felt the ground shake and the air shattered by the testing of a Saturn C-1 booster rocket, many times as powerful as the Atlas which launched John Glenn, generating power equivalent to 10,000 automobiles with their accelerators on the floor.We have seen the site where the F-1 rocket engines, each one as powerful as all eight engines of the Saturn combined, will be clustered together to make the advanced Saturn missile, assembled in a new building to be built at Cape Canaveral as tall as a48 story structure, as wide as a city block, and as long as two lengths of this field.</p><p></p><hr><p></p><center><a href="movies.html">Return to Space Movies Cinema</a></center></body></html>"""
