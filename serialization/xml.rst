***
XML
***


xml
===
.. code-block:: python

    import xml.etree.ElementTree

    FILE = '../serialization/data/xml-commands.xml'
    # <execute>
    #     <command timeout="2">/bin/ls -la /etc/</command>
    #     <command>/bin/ls -l /home/ /tmp/</command>
    #     <command timeout="1">/bin/sleep 2</command>
    #     <command timeout="2">/bin/echo 'juz wstalem'</command>
    # </execute>

    root = xml.etree.ElementTree.parse(FILE).getroot()

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


``lxml``
========

Creating elements
-----------------
.. code-block:: python
    :caption: Creating elements

    from lxml.etree import tostring, Element


    root = Element("iris")

    print(tostring(root))
    # b'<iris/>'

Adding elements using list interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python
    :caption: Adding elements using list interface

    from lxml.etree import tostring, Element


    root = Element("iris")

    root.append(Element("setosa"))
    root.append(Element("versicolor"))

    print(tostring(root))
    # b'<iris><setosa/><versicolor/></iris>'

Adding elements using objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python
    :caption: Adding elements using objects


    from lxml.etree import tostring, Element, SubElement


    root = Element("iris")

    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    print(tostring(root))
    # b'<iris><setosa/><versicolor/><virginica/></iris>'

Length of a subtree
-------------------
.. code-block:: python

    from lxml.etree import Element


    root = Element("iris")

    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    print(len(root))
    # 3

Selecting subtree
-----------------
.. code-block:: python

    from lxml.etree import Element

    root = Element("iris")

    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    selected = root[2]

    print(selected.tag)
    # virginica

Where is selected element
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from lxml.etree import Element


    root = Element("iris")

    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    selected = root[1]
    root.index(selected)
    # 1

    selected = root[2]
    root.index(selected)
    # 2

Elements are lists
------------------
.. code-block:: python

    from lxml.etree import tostring, Element


    root = Element("iris")

    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    children = list(root)
    print(children)
    # [
    #     <Element setosa at 0x113cd4048>,
    #     <Element versicolor at 0x113cd4188>,
    #     <Element virginica at 0x113cd41c8>
    # ]

Iterating over elements
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

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

Slicing elements
^^^^^^^^^^^^^^^^
.. code-block:: python

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

Elements carry attributes as a dict
-----------------------------------
.. code-block:: python

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")

    print(tostring(tag))
    # b'<iris kingdom="plantae"/>'

.. code-block:: python

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")

    print(tag.get("kingdom"))          # plantae
    print(tag.get("not-existing"))     # None

.. code-block:: python

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    print(tag.get("kind"))
    # flower

    print(tostring(tag))
    # b'<iris kingdom="plantae" kind="flower"/>'

.. code-block:: python

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

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    for key, value in tag.items():
        print(f'{key} -> {value}')

    # kingdom -> plantae
    # kind -> flower

.. code-block:: python

    attributes = root.attrib
    print(attributes["interesting"])            # totally
    print(attributes.get("no-such-attribute"))  # None

    attributes["hello"] = "Guten Tag"
    print(attributes["hello"])                  # Guten Tag

    d = dict(root.attrib)
    sorted(d.items())
    # [('hello', 'Guten Tag'), ('interesting', 'totally')]

Elements contain text
---------------------
.. code-block:: python

    >>> root = etree.Element("root")
    >>> root.text = "TEXT"

    >>> print(root.text)
    TEXT

    >>> etree.tostring(root)
    b'<root>TEXT</root>'

.. code-block:: html

    <html><body>Hello<br/>World</body></html>

.. code-block:: python

    >>> html = etree.Element("html")
    >>> body = etree.SubElement(html, "body")
    >>> body.text = "TEXT"

    >>> etree.tostring(html)
    b'<html><body>TEXT</body></html>'

    >>> br = etree.SubElement(body, "br")
    >>> etree.tostring(html)
    b'<html><body>TEXT<br/></body></html>'

    >>> br.tail = "TAIL"
    >>> etree.tostring(html)
    b'<html><body>TEXT<br/>TAIL</body></html>'

XPATH
-----
.. code-block:: python

    >>> print(html.xpath("string()")) # lxml.etree only!
    TEXTTAIL
    >>> print(html.xpath("//text()")) # lxml.etree only!
    ['TEXT', 'TAIL']

Tree iteration
--------------
.. code-block:: python

    >>> root = etree.Element("root")
    >>> etree.SubElement(root, "child").text = "Child 1"
    >>> etree.SubElement(root, "child").text = "Child 2"
    >>> etree.SubElement(root, "another").text = "Child 3"

    >>> print(etree.tostring(root, pretty_print=True))
    <root>
      <child>Child 1</child>
      <child>Child 2</child>
      <another>Child 3</another>
    </root>

    >>> for element in root.iter():
    ...     print("%s - %s" % (element.tag, element.text))
    root - None
    child - Child 1
    child - Child 2
    another - Child 3

.. code-block:: python

    >>> for element in root.iter("child"):
    ...     print("%s - %s" % (element.tag, element.text))
    child - Child 1
    child - Child 2

    >>> for element in root.iter("another", "child"):
    ...     print("%s - %s" % (element.tag, element.text))
    child - Child 1
    child - Child 2
    another - Child 3

.. code-block:: python

    >>> root.append(etree.Entity("#234"))
    >>> root.append(etree.Comment("some comment"))

    >>> for element in root.iter():
    ...     if isinstance(element.tag, basestring):  # or 'str' in Python 3
    ...         print("%s - %s" % (element.tag, element.text))
    ...     else:
    ...         print("SPECIAL: %s - %s" % (element, element.text))
    root - None
    child - Child 1
    child - Child 2
    another - Child 3
    SPECIAL: &#234; - &#234;
    SPECIAL: <!--some comment--> - some comment

    >>> for element in root.iter(tag=etree.Element):
    ...     print("%s - %s" % (element.tag, element.text))
    root - None
    child - Child 1
    child - Child 2
    another - Child 3

    >>> for element in root.iter(tag=etree.Entity):
    ...     print(element.text)
    &#234;

Serialization
-------------
.. code-block:: python

    >>> root = etree.XML('<root><a><b/></a></root>')

    >>> etree.tostring(root)
    b'<root><a><b/></a></root>'

    >>> print(etree.tostring(root, xml_declaration=True))
    <?xml version='1.0' encoding='ASCII'?>
    <root><a><b/></a></root>

    >>> print(etree.tostring(root, encoding='iso-8859-1'))
    <?xml version='1.0' encoding='iso-8859-1'?>
    <root><a><b/></a></root>

    >>> print(etree.tostring(root, pretty_print=True))
    <root>
      <a>
        <b/>
      </a>
    </root>

.. code-block:: python

    >>> root = etree.XML(
    ...    '<html><head/><body><p>Hello<br/>World</p></body></html>')

    >>> etree.tostring(root) # default: method = 'xml'
    b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    >>> etree.tostring(root, method='xml') # same as above
    b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    >>> etree.tostring(root, method='html')
    b'<html><head></head><body><p>Hello<br>World</p></body></html>'

    >>> print(etree.tostring(root, method='html', pretty_print=True))
    <html>
    <head></head>
    <body><p>Hello<br>World</p></body>
    </html>

    >>> etree.tostring(root, method='text')
    b'HelloWorld'

xslt
====

Example 1
---------
.. code-block:: python

    import io
    from lxml import etree


    XSLT = '''
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
        <foo><xsl:value-of select="/a/b/text()" /></foo>
        </xsl:template>
    </xsl:stylesheet>
    '''

    xslt_root = etree.XML(XSLT)
    transform = etree.XSLT(xslt_root)

    f = io.StringIO('<a><b>Text</b></a>')
    doc = etree.parse(f)
    result_tree = transform(doc)

    print(result_tree)

Example 2
---------
.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <CATALOG>
        <PLANT>
            <COMMON>Bloodroot</COMMON>
            <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
            <ZONE>4</ZONE>
            <LIGHT>Mostly Shady</LIGHT>
            <PRICE>$2.44</PRICE>
            <AVAILABILITY>031599</AVAILABILITY>
        </PLANT>
    </CATALOG>

.. code-block:: xslt

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
        <p>
            <xsl:value-of select="description"/>
            <span> (<xsl:value-of select="AVAILABILITY"/> will be available)</span>
        </p>
      </div>

    </xsl:for-each>


Assignments
===========

XML Parsing
-----------
* Filename: ``xml_parse.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 20 min
* Input data: :numref:`listing-xml_plants.xml`

#. Przekonwertuj dane do struktur Pythonowych ``list`` of ``dict``

.. literalinclude:: data/xml_plants.xml
    :name: listing-xml_plants.xml
    :language: xml
    :caption: XML Parsing

XSLT Transformation
-------------------
* Filename: ``xml_xslt.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-xml_transform.xml`

#. Przekonwertuj dane do struktur Pythonowych ``list`` of ``dict``

.. literalinclude:: data/xml_transform.xml
    :name: listing-xml_transform.xml
    :language: xml
    :caption: XML data for XSLT transformation
