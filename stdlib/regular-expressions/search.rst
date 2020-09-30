*************
Regexp Search
*************


About
=====
* ``re.search()``
* Searches if pattern contains a string


Examples
========
.. code-block:: python
    :caption: Usage of ``re.search()``

    import re


    def contains(pattern, text)
        if re.search(pattern, text):
            return True
        else:
            return False


    COMMIT_MESSAGE = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'
    JIRA_ISSUEKEY = r'[A-Z]{2,10}-[0-9]{1,6}'
    REDMINE_NUMBER = r'#[0-9]+'

    contains(JIRA_ISSUEKEY, COMMIT_MESSAGE)      # True
    contains(REDMINE_NUMBER, COMMIT_MESSAGE)     # False


Assignments
===========

Regexp Search Astronauts
------------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/regexp_search_astronauts.py`
* Last update: 2020-10-01
* References: First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

:English:
    #. Use data from "Input" section (see below)
    #. Use ``re.search()`` to check if Astronaut first and last names are in the text
    #. Astronauts to find:

        * Neil Armstrong
        * Buzz Aldrin
        * Michael Collins
        * Jan Twardowski
        * Mark Watney

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj ``re.search()`` do sprawdzenia czy imiona i nazwiska Astronautów występują w tekście
    #. Astronauci do znalezienia:

        * Neil Armstrong
        * Buzz Aldrin
        * Michael Collins
        * Jan Twardowski
        * Mark Watney

:Input:
    .. code-block:: python

        DATA = """Apollo 11 was the spaceflight that first landed humans on the Moon.
        Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American
        crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:17 UTC.
        Armstrong became the first person to step onto the lunar surface six hours and
        39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later.
        They spent about two and a quarter hours together outside the spacecraft,
        and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth.
        Command module pilot Michael Collins flew the command module Columbia alone
        in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent
        21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base
        before lifting off to rejoin Columbia in lunar orbit."""

Regexp Search Moon Speech
-------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/regexp_search_moon_speech.py`
* Last update: 2020-10-01
* References: "Moon Speech" by John F. Kennedy at Rice Stadium, Houston, TX on 1962-09-12 :cite:`RegexpKennedy1962`

:English:
    #. Use data from "Input" section (see below)
    #. Save as ``moon_speech.html``
    #. Using ``re.search()`` split text by paragraphs
    #. Print paragraph starting with "We choose to go to the moon"

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz jako ``moon_speech.html``
    #. Za pomocą ``re.search()`` podziel tekst na paragrafy
    #. Wyświetl paragraf zaczynający się od słów "We choose to go to the moon"

.. code-block:: python

    DATA = """<html><body> <bgsound src="jfktalk.wav" loop="2"><p></p><center><h3>John F. Kennedy Moon Speech - Rice Stadium</h3><img src="jfkrice.jpg"><h3>September 12, 1962</h3></center><p></p><hr><p></p><center>Movie clips of JFK speaking at Rice University: <a href="JFKatRice.mov">(.mov)</a> or <a href="jfkrice.avi">(.avi)</a> (833K)</center><p><a href="jfkru56k.asf">See and hear</a> the entire speech for 56K modem download [8.7 megabytes in a .asf movie format which requires Windows Media Player 7 (speech lasts about 33 minutes)].<br><a href="jfkru100.asf">See and hear</a> the entire speech for higher speed access [25.3 megabytes in .asf movie format which requires Windows Media Player 7].<br><a href="jfkslide.asf">See and hear</a> a five minute audio version of the speech with accompanying slides and music. This is a most inspirational presentation of, perhaps, the most famous space speech ever given. The file is a streaming video Windows Media Player 7 format. [11 megabytes in .asf movie format which requires Windows Media Player 7]. <br><a href="jfk_rice_speech.mpg">See and hear</a> the 17 minute 48 second speech in the .mpg format. This is a very large file of 189 megabytes and only suggested for those with DSL, ASDL, or cable modem access as the download time on a 28.8K or 56K modem would be many hours duration.</p><p></p><hr><p></p><center><h4>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h4></center><p>President Pitzer, Mr. Vice President, Governor, CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, Mr.Bell, scientists, distinguished guests, and ladies and gentlemen:</p><p>We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills,because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win,and the others, too.</p><p>It is for these reasons that I regard the decision last year to shift our efforts in space from low to high gear as among the most important decisions that will be made during my incumbency in the office of the Presidency.</p><p>In the last 24 hours we have seen facilities now being created for the greatest and most complex exploration in man's history.We have felt the ground shake and the air shattered by the testing of a Saturn C-1 booster rocket, many times as powerful as the Atlas which launched John Glenn, generating power equivalent to 10,000 automobiles with their accelerators on the floor.We have seen the site where the F-1 rocket engines, each one as powerful as all eight engines of the Saturn combined, will be clustered together to make the advanced Saturn missile, assembled in a new building to be built at Cape Canaveral as tall as a48 story structure, as wide as a city block, and as long as two lengths of this field.</p><p></p><hr><p></p><center><a href="movies.html">Return to Space Movies Cinema</a></center></body></html>"""

Regexp Search Time
------------------
* Complexity level: medium
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/regexp_search_time.py`
* Last update: 2020-10-01
* References: First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

:English:
    #. Use data from "Input" section (see below)
    #. Use regular expressions to check text contains time in UTC (format: ``%H:%M UTC``)
    #. Use simplified checking: ``##:## UTC``, where ``#`` is a digit
    #. Print found time

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj wyrażeń regularnych do sprawdzenia czy tekst zawiera godzinę w UTC (format: ``%H:%M UTC``)
    #. Użyj uproszczonego sprawdzania: ``##:## UTC``, gdzie ``#`` to dowolna cyfra
    #. Print found time

:Input:
    .. code-block:: python

        DATA = """Apollo 11 was the spaceflight that first landed humans on the Moon.
        Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American
        crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:17 UTC.
        Armstrong became the first person to step onto the lunar surface six hours and
        39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later.
        They spent about two and a quarter hours together outside the spacecraft,
        and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth.
        Command module pilot Michael Collins flew the command module Columbia alone
        in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent
        21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base
        before lifting off to rejoin Columbia in lunar orbit."""


Regexp Search Datetime
----------------------
* Complexity level: hard
* Lines of code to write: 4 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/regexp_search_datetime.py`
* Last update: 2020-10-01
* References: (modified) First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

:English:
    #. Use data from "Input" section (see below)
    #. Use regular expressions to check text contains time in UTC (format: ``%H:%M UTC``)
    #. Note, that this is slightly modified text than previously
    #. Check if text contains time in UTC (format: ``%H:%M UTC``)
    #. Found match must be a valid time
    #. Print found time

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj wyrażeń regularnych do sprawdzenia czy tekst zawiera godzinę w UTC (format: ``%H:%M UTC``)
    #. Zwróć uwagę, że to lekko zmodyfikowany tekst niż poprzednio
    #. Sprawdź czy tekst zawiera godzinę w UTC (format: ``%H:%M UTC``)
    #. Znalezisko musi być poprawnym czasem
    #. Wyświetl znaleziony czas

:Input:
    .. code-block:: text
        :caption: (modified) First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

        Apollo 11 was the spaceflight that first landed humans on the Moon. Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:67 UTC. Armstrong became the first person to step onto the lunar surface six hours and 39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent about two and a quarter hours together outside the spacecraft, and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth. Command module pilot Michael Collins flew the command module Columbia alone in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base before lifting off to rejoin Columbia in lunar orbit.
