******************************
Serialization XML, XSLT, XPath
******************************


``xml`` module from standard library
====================================
.. code-block:: python
    :caption: ``xml`` module from standard library

    from xml.etree.ElementTree import parse


    FILE = r'../_data/xml/commands.xml'
    # <execute>
    #     <command timeout="2">/bin/ls -la /etc/</command>
    #     <command>/bin/ls -l /home/ /tmp/</command>
    #     <command timeout="1">/bin/sleep 2</command>
    #     <command timeout="2">/bin/echo 'juz wstalem'</command>
    # </execute>

    root = parse(FILE).getroot()

    for command in root.findall('./command'):
        print(command.tag)
        print(command.text)
        print(command.attrib)
        print()

    # command
    # /bin/ls -la /etc/
    # {'timeout': '2'}
    #
    # command
    # /bin/ls -l /home/ /tmp/
    # {}
    #
    # command
    # /bin/sleep 2
    # {'timeout': '1'}
    #
    # command
    # /bin/echo 'juz wstalem'
    # {'timeout': '2'}


``lxml`` module
===============

* ``pip install lxml``

Creating elements
-----------------
.. code-block:: python
    :caption: Creating elements

    from lxml.etree import tostring, Element


    root = Element("iris")

    print(tostring(root))
    # b'<iris/>'

.. code-block:: python
    :caption: Adding elements using list interface

    from lxml.etree import tostring, Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    print(tostring(root))
    # b'<iris><setosa/><versicolor/><virginica/></iris>'

Length of a subtree
-------------------
.. code-block:: python
    :caption: Length of a subtree

    from lxml.etree import Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    print(len(root))
    # 3

Selecting subtree
-----------------
.. code-block:: python
    :caption: Selecting subtree

    from lxml.etree import Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    selected = root[2]
    print(selected.tag)
    # virginica

.. code-block:: python
    :caption: Where is selected element

    from lxml.etree import Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    selected = root[1]
    root.index(selected)
    # 1

    selected = root[2]
    root.index(selected)
    # 2

Element tree as a lists
-----------------------
.. code-block:: python
    :caption: Elements are lists

    from lxml.etree import tostring, Element


    root = Element('iris")
    root.append(Element('setosa"))
    root.append(Element('versicolor"))
    root.append(Element('virginica"))

    children = list(root)
    print(children)
    # [
    #     <Element setosa at 0x113cd4048>,
    #     <Element versicolor at 0x113cd4188>,
    #     <Element virginica at 0x113cd41c8>
    # ]

.. code-block:: python
    :caption: Iterating over elements

    from lxml.etree import Element


    root = Element("iris")
    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    for child in root:
        print(child.tag)

    # setosa
    # versicolor
    # virginica

.. code-block:: python
    :caption: Slicing elements

    from lxml.etree import Element


    root = Element("iris")
    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    root.insert(0, Element("arctica"))

    start = root[:1]
    end = root[-1:]

    print(start[0].tag)  # arctica
    print(end[0].tag)    # virginica

Elements as a dict
------------------
.. code-block:: python
    :caption: Create element using ``dict`` interface

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")

    print(tostring(tag))
    # b'<iris kingdom="plantae"/>'

.. code-block:: python
    :caption: Get element attributes and values

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")

    print(tag.get("kingdom"))          # plantae
    print(tag.get("not-existing"))     # None

.. code-block:: python
    :caption: Set element attributes and values

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    print(tag.get("kind"))
    # flower

    print(tostring(tag))
    # b'<iris kingdom="plantae" kind="flower"/>'

.. code-block:: python
    :caption: Elements carry attributes as a dict

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    tag.keys()
    # ['kind', 'kingdom']

    tag.values()
    # ['plantae', 'flower']

    tag.items()
    # [('kingdom', 'plantae'), ('kind', 'flower')]

.. code-block:: python
    :caption: Iterating over element attributes and values

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    for key, value in tag.items():
        print(f'{key} -> {value}')

    # kingdom -> plantae
    # kind -> flower

.. code-block:: python
    :caption: Elements carry attributes as a dict

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    tag.attrib['kingdom']
    # 'plantae'

    tag.attrib['not-existing']
    # KeyError: 'not-existing'

    tag.attrib['species'] = 'Setosa'
    tag.attrib.get('species')
    # 'Setosa'

    tag.attrib
    # {'kingdom': 'plantae', 'kind': 'flower'}

    tag.attrib.items()
    # [('kingdom', 'plantae'), ('kind', 'flower'), ('species', 'Setosa')]

Elements contain text
---------------------
.. code-block:: python

    from lxml.etree import tostring, Element

    tag = Element("iris")
    tag.text = "Setosa"

    tag.text
    # 'Setosa'

    tostring(tag)
    # b'<iris>Setosa</iris>'

Tree iteration
--------------
.. code-block:: python

    from lxml.etree import tostring, Element, SubElement

    root = Element("iris")
    SubElement(root, "species").text = "Setosa"
    SubElement(root, "species").text = "Virginica"
    SubElement(root, "flower").text = "Versicolor"

    print(tostring(root, pretty_print=True))
    # b'<iris>
    #       <species>Setosa</species>
    #       <species>Virginica</species>
    #       <flower>Versicolor</flower>
    # </iris>'


    for element in root.iter():
        print(f'{element.tag} -> {element.text}')

    # iris -> None
    # species -> Setosa
    # species -> Virginica
    # flower -> Versicolor


    for element in root.iter("species"):
        print(f'{element.tag} -> {element.text}')

    # species -> Setosa
    # species -> Virginica


    for element in root.iter("species", "flower"):
        print(f'{element.tag} -> {element.text}')

    # species -> Setosa
    # species -> Virginica
    # flower -> Versicolor

Entities
--------
.. code-block:: python

    from lxml.etree import tostring, Element, SubElement, Entity

    root = Element("iris")
    print(tostring(root))
    # b'<iris/>'

    root.append(Entity("#234"))
    print(tostring(root))
    # b'<iris>&#234;</iris>'

Comments
--------
.. code-block:: python

    from lxml.etree import tostring, Element, SubElement, Comment

    root = Element("iris")
    print(tostring(root))
    # b'<iris/>'

    root.append(Comment("Hello World"))
    print(tostring(root))
    # b'<iris><!--Hello World--></iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, SubElement

    root = Element('iris')
    SubElement(root, 'species').text = 'setosa'
    SubElement(root, 'species').text = 'virginica'
    SubElement(root, 'flower').text = 'versicolor'

    print(tostring(root))
    # b'<iris><species>setosa</species><species>virginica</species><flower>versicolor</flower></iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, Entity

    root = Element('iris')
    root.append(Entity('#234'))

    print(tostring(root))
    # b'<iris>&#234;</iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, Comment

    root = Element('iris')
    root.append(Comment('Hello World'))
    print(tostring(root))
    # b'<iris><!--Hello World--></iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, Entity, Comment

    root = Element('iris')
    root.append(Element('species'))
    root.append(Element('species'))
    root.append(Element('flower'))
    root.append(Entity('#234'))
    root.append(Comment('Hello World'))

    print(tostring(root))
    # b'<iris><species/><species/><flower/>&#234;<!--Hello World--></iris>'


    for element in root.iter():
        if isinstance(element.tag, str):
            print(f'TAG: {element.tag} -> {element.text}')
        else:
            print(f'SPECIAL: {element} -> {element.text}')

    # TAG: iris -> None
    # TAG: species -> None
    # TAG: species -> None
    # TAG: flower -> None
    # SPECIAL: &#234; -> &#234;
    # SPECIAL: <!--Hello World--> -> Hello World


    for element in root.iter(tag=Element):
            print(f'{element.tag} -> {element.text}')

    # iris -> None
    # species -> None
    # species -> None
    # flower -> None


    for element in root.iter(tag=Entity):
        print(element.text)

    # &#234;


    for element in root.iter(tag=Comment):
        print(element.text)

    # Hello World

Serialization
-------------
.. code-block:: python

    from lxml.etree import tostring, XML


    root = XML('<root><a><b/></a></root>')

    tostring(root)
    # b'<root><a><b/></a></root>'

    print(tostring(root, xml_declaration=True))
    # b"<?xml version='1.0' encoding='ASCII'?>\n<root><a><b/></a></root>"

    print(tostring(root, encoding='utf-8'))
    # b'<root><a><b/></a></root>'

    print(tostring(root, encoding='iso-8859-2'))
    # b"<?xml version='1.0' encoding='iso-8859-2'?>\n<root><a><b/></a></root>"

    print(tostring(root, pretty_print=True))
    # b'<root>\n  <a>\n    <b/>\n  </a>\n</root>\n'

    print(tostring(root, pretty_print=True).decode())
    # <root>
    #   <a>
    #     <b/>
    #   </a>
    # </root>

.. code-block:: python

    from lxml.etree import tostring, XML

    root = XML('<html><head/><body><p>Hello<br/>World</p></body></html>')

    # default: method = 'xml'
    tostring(root)
    # b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    tostring(root, method='xml')
    # b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    tostring(root, method='html')
    # b'<html><head></head><body><p>Hello<br>World</p></body></html>'

    print(tostring(root, method='html', pretty_print=True))
    # b'<html>\n<head></head>\n<body><p>Hello<br>World</p></body>\n</html>\n'

    print(tostring(root, method='html', pretty_print=True).decode())
    # <html>
    # <head></head>
    # <body><p>Hello<br>World</p></body>
    # </html>

    tostring(root, method='text')
    # b'HelloWorld'


Working with HTML
=================
* Using ``lxml`` module

.. code-block:: html

    <html><body>Iris<br/>Setosa</body></html>

.. code-block:: python

    from lxml.etree import tostring, Element, SubElement


    html = Element("html")
    body = SubElement(html, "body")

    body.text = "Iris"
    tostring(html)
    # b'<html><body>Iris</body></html>'

    br = SubElement(body, "br")
    tostring(html)
    # b'<html><body>Iris<br/></body></html>'

    br.tail = 'Setosa'
    tostring(html)
    # b'<html><body>Iris<br/>Setosa</body></html>'


XPATH
=====
* Using ``lxml`` module

.. code-block:: python

    print(html.xpath("string()")) # lxml.etree only!
    # TEXTTAIL

    print(html.xpath("//text()")) # lxml.etree only!
    # ['TEXT', 'TAIL']


XSLT
====
* Using ``lxml`` module

Example 1
---------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    TEMPLATE = """
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <xsl:template match="/">

                <my_tag>
                    <xsl:value-of select="/outer/inner/text()" />
                </my_tag>

            </xsl:template>
        </xsl:stylesheet>
    """

    DATA = """
        <outer>
            <inner>Hello World</inner>
        </outer>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    result = transform(data)

    print(result)
    # <?xml version="1.0"?>
    # <my_tag>Hello World</my_tag>

Example 2
---------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    DATA = """
        <astronauts>
            <astro>
                <firstname>Jan</firstname>
                <lastname>Twardowski</lastname>
            </astro>
            <astro>
                <firstname>Mark</firstname>
                <lastname>Watney</lastname>
            </astro>
        </astronauts>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <table>
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                    </tr>
                </thead>
                <tbody>

                    <xsl:for-each select="astronauts/astro">
                        <tr>
                            <td><xsl:value-of select="firstname"/></td>
                            <td><xsl:value-of select="lastname"/></td>
                        </tr>
                    </xsl:for-each>

                </tbody>
            </table>
        </html>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    result = transform(data)

    print(result)
    # <html><table>
    # <thead><tr>
    # <th>First Name</th>
    # <th>Last Name</th>
    # </tr></thead>
    # <tbody>
    # <tr>
    # <td>Jan</td>
    # <td>Twardowski</td>
    # </tr>
    # <tr>
    # <td>Mark</td>
    # <td>Watney</td>
    # </tr>
    # </tbody>
    # </table></html>

Example 3
---------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    DATA = """
        <CATALOG>
            <PLANT>
                <COMMON>Bloodroot</COMMON>
                <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
                <ZONE>4</ZONE>
                <LIGHT>Mostly Shady</LIGHT>
                <PRICE>$2.44</PRICE>
                <AVAILABILITY>031599</AVAILABILITY>
            </PLANT>
            <PLANT>
                <COMMON>Columbine</COMMON>
                <BOTANICAL>Aquilegia canadensis</BOTANICAL>
                <ZONE>3</ZONE>
                <LIGHT>Mostly Shady</LIGHT>
                <PRICE>$9.37</PRICE>
                <AVAILABILITY>030699</AVAILABILITY>
            </PLANT>
        </CATALOG>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <style>
            body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
            div.title {background-color: teal; color: white; padding: 4px}
            div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
            span {font-weight: bold}
        </style>

        <body>

        <xsl:for-each select="CATALOG/PLANT">

            <div class="title">
                <span><xsl:value-of select="BOTANICAL"/></span>
                <xsl:value-of select="PRICE"/>
            </div>

            <div class="description">
                    <xsl:value-of select="description"/>
                    <span> (<xsl:value-of select="AVAILABILITY"/> will be available)</span>
            </div>

        </xsl:for-each>
        </body>
        </html>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    result = transform(data)

    print(result)
    # <html>
    # <style>
    #     body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
    #     div.title {background-color: teal; color: white; padding: 4px}
    #     div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
    #     span {font-weight: bold}
    # </style>
    # <body>
    # <div class="title">
    # <span>Sanguinaria canadensis</span>$2.44</div>
    # <div class="description"><span> (031599 will be available)</span></div>
    # <div class="title">
    # <span>Aquilegia canadensis</span>$9.37</div>
    # <div class="description"><span> (030699 will be available)</span></div>
    # </body>
    # </html>


Assignments
===========

XML Parsing
-----------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/xml_parse.py`

:English:
    #. Use data from "Input" section (see below)
    #. Convert input data to Python ``List[dict]``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj dane wejściowe do Pythonowego ``List[dict]``

:Input:
    .. literalinclude:: data/xml_plants.xml
        :language: xml

XSLT Transformation
-------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/xml_xslt.py`

:English:
    #. Use data from "Input" section (see below)
    #. Convert input data to Python ``List[dict]``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj dane wejściowe do Pythonowego ``List[dict]``

:Input:
    .. literalinclude:: data/xml_transform.xml
        :language: xml
